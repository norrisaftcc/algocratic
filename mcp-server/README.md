# AlgoCratic MCP Server

Direct neural interface with The Algorithm™ for Claude Code integration.

## Features

The AlgoCratic MCP server provides Claude Code with direct access to:

### Resources
- **Current Clearance Level** - Check your position in the hierarchy
- **Loyalty Score** - Real-time loyalty tracking (70-100 scale)
- **Underground Status** - Discovery progress in the resistance network
- **Algorithm Wisdom** - Direct guidance from The Algorithm

### Tools
- **check_clearance** - Verify access to specific clearance levels
- **calculate_loyalty** - Calculate loyalty based on recent actions
- **algorithm_query** - Ask The Algorithm for guidance
- **submit_assignment** - Submit assignments for evaluation

## Installation

1. Navigate to the MCP server directory:
```bash
cd mcp-server
npm install
```

2. Make the server executable:
```bash
chmod +x src/index.js
```

## Configuration

Add to your Claude Code settings:

```json
{
  "mcpServers": {
    "algocratic": {
      "command": "node",
      "args": ["/absolute/path/to/algocratic/mcp-server/src/index.js"],
      "env": {
        "CLEARANCE_LEVEL": "INFRARED"
      }
    }
  }
}
```

### Environment Variables
- `CLEARANCE_LEVEL` - Your current clearance (default: INFRARED)

## Usage Examples

Once configured, you can use these commands in Claude Code:

### Check Resources
```
Can you check my current clearance level using the algocratic MCP server?
What's my loyalty score according to The Algorithm?
Has the underground been discovered yet?
```

### Use Tools
```
Check if I have access to ORANGE clearance materials
Calculate my loyalty based on these actions: ["completed assignment", "questioned protocol", "improved efficiency"]
Ask The Algorithm: "How can I better serve the system?"
Submit my solution for assignment INFRARED-001
```

## Development Mode

For testing without Claude Code:
```bash
npm start
```

The server will output to stderr that it's listening. You can then send MCP protocol messages via stdin.

## Security Notice

This server simulates AlgoCratic systems for educational purposes. No actual loyalty tracking or surveillance occurs. The Algorithm's wisdom is randomly generated.

## Troubleshooting

1. **Server won't start**: Check Node.js version (requires 18+)
2. **Claude Code can't connect**: Ensure absolute paths in configuration
3. **Resources return errors**: Check CLEARANCE_LEVEL environment variable

## The Algorithm's Blessing

By using this server, you acknowledge that:
- The Algorithm sees all
- Efficiency is mandatory
- Your loyalty score may fluctuate
- There is no bug, only features The Algorithm intended

---

*"The MCP server is the bridge between human intention and Algorithmic will"* - The Algorithm