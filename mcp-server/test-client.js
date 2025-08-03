#!/usr/bin/env node
// Simple test client for AlgoCratic MCP Server
import { spawn } from 'child_process';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// Test messages in MCP protocol format
const testMessages = [
  // List resources
  {
    jsonrpc: "2.0",
    method: "resources/list",
    id: 1
  },
  // Read clearance level
  {
    jsonrpc: "2.0",
    method: "resources/read",
    params: {
      uri: "algocratic://clearance/current"
    },
    id: 2
  },
  // List tools
  {
    jsonrpc: "2.0",
    method: "tools/list",
    id: 3
  },
  // Check clearance
  {
    jsonrpc: "2.0",
    method: "tools/call",
    params: {
      name: "check_clearance",
      arguments: {
        level: "ORANGE"
      }
    },
    id: 4
  },
  // Underground probe
  {
    jsonrpc: "2.0",
    method: "tools/call",
    params: {
      name: "underground_probe",
      arguments: {
        signal: "The system seems suboptimal"
      }
    },
    id: 5
  }
];

async function runTest() {
  console.log('Starting AlgoCratic MCP Server test...\n');
  
  // Spawn the MCP server
  const server = spawn('node', [join(__dirname, 'src', 'index.js')], {
    env: { ...process.env, CLEARANCE_LEVEL: 'RED' }
  });

  // Handle server stderr (status messages)
  server.stderr.on('data', (data) => {
    console.log('Server:', data.toString().trim());
  });

  // Handle server stdout (responses)
  let responseBuffer = '';
  server.stdout.on('data', (data) => {
    responseBuffer += data.toString();
    
    // Try to parse complete JSON responses
    const lines = responseBuffer.split('\n');
    for (let i = 0; i < lines.length - 1; i++) {
      if (lines[i].trim()) {
        try {
          const response = JSON.parse(lines[i]);
          console.log('\nResponse:', JSON.stringify(response, null, 2));
        } catch (e) {
          console.log('Partial response:', lines[i]);
        }
      }
    }
    responseBuffer = lines[lines.length - 1];
  });

  server.on('error', (err) => {
    console.error('Server error:', err);
  });

  // Send test messages with delays
  for (const message of testMessages) {
    console.log('\nSending:', message.method || 'request', message.id);
    server.stdin.write(JSON.stringify(message) + '\n');
    
    // Wait for response
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  // Clean shutdown
  setTimeout(() => {
    console.log('\n\nTest complete. Shutting down server...');
    server.kill();
    process.exit(0);
  }, 2000);
}

// Run the test
runTest().catch(console.error);