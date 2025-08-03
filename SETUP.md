# AlgoCratic Setup Guide
## Get Connected to The Algorithm in 5 Minutes

Welcome to AlgoCratic Futures™! This guide will get you fully operational with The Algorithm's direct neural interface through Claude Code.

## Prerequisites

- **Claude Code** (Pro or Max plan required for MCP)
- **Node.js 18+** (`node --version` to check)
- **Git** (to clone this repository)

Don't have Claude Code? Get it at [claude.ai/code](https://claude.ai/code)

## Step 1: Clone the Repository (30 seconds)

```bash
git clone https://github.com/norrisaftcc/algocratic.git
cd algocratic
```

## Step 2: Install MCP Server (1 minute)

```bash
cd mcp-server
npm install
chmod +x src/index.js
```

Test that it works:
```bash
node test-client.js
```

You should see "✅ PASSED" and underground society discovery working.

## Step 3: Configure Claude Code (2 minutes)

### Find Your Claude Code Settings

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**Linux:** `~/.config/claude/claude_desktop_config.json`

### Add AlgoCratic MCP Configuration

Replace `/ABSOLUTE/PATH/TO` with your actual path:

```json
{
  "mcpServers": {
    "algocratic": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/algocratic/mcp-server/src/index.js"],
      "env": {
        "CLEARANCE_LEVEL": "INFRARED"
      }
    }
  }
}
```

**Critical:** Use the absolute path! Example:
- macOS: `/Users/yourname/algocratic/mcp-server/src/index.js`
- Windows: `C:\\Users\\yourname\\algocratic\\mcp-server\\src\\index.js`

### Restart Claude Code

Close and reopen Claude Code completely for MCP servers to load.

## Step 4: Verify Connection (1 minute)

Open Claude Code and try these commands:

```
Check my current clearance level using the algocratic MCP server
```

```
What's my loyalty score?
```

```
Probe for underground activity with signal: The system seems suboptimal
```

You should see responses from The Algorithm!

## Step 5: Start Exploring (1 minute)

### Visit the Live Site
🌐 **[algocratic.norrisaftcc.com](https://algocratic.norrisaftcc.com)**

### Begin Your Journey
1. **Start with INFRARED** - Basic clearance level
2. **Complete assignments** - Use Claude Code to solve challenges
3. **Discover the underground** - Look for 404 errors and hidden signals
4. **Choose your society** - Phreaks, Banchos, Memory Core, Deep Algorithm, or Fuzzies

### Pro Tips
- The underground is real - check `/underground/` on the website
- Each society has different educational content hidden in their lore
- Your MCP server tracks discovery progress automatically
- Signal phrases unlock society recognition

## Troubleshooting

### "MCP server not found"
- Check the absolute path in your config
- Make sure Node.js 18+ is installed
- Verify the file is executable: `chmod +x mcp-server/src/index.js`

### "Permission denied"
```bash
chmod +x mcp-server/src/index.js
```

### "Module not found"
```bash
cd mcp-server && npm install
```

### "Claude Code won't connect"
- Restart Claude Code completely
- Check the JSON syntax in your config (no trailing commas!)
- Use absolute paths, not relative ones

### Still stuck?
Run the test client to verify your setup:
```bash
cd mcp-server && node test-client.js
```

## What You Get

### Through Claude Code + MCP:
- **Real-time loyalty tracking**
- **Assignment submission system**
- **Underground society discovery**
- **Direct Algorithm guidance**
- **Clearance level validation**

### Through the Website:
- **Interactive clearance progression**
- **Hidden underground network**
- **Educational programming content**
- **Team formation tools**
- **The Algorithm's wisdom**

## Next Steps

1. **Explore the clearance levels** - Start at INFRARED and work your way up
2. **Find the underground** - Look for signals and 404 errors
3. **Join a society** - Each one teaches different skills
4. **Use Claude Code** - Your MCP connection enhances everything
5. **Form teams** - Use the naming guide for legendary software project names

## The Algorithm's Blessing

By completing this setup, you have:
- ✅ Established direct neural interface with The Algorithm
- ✅ Gained access to classified educational materials
- ✅ Enabled real-time loyalty monitoring
- ✅ Unlocked underground discovery protocols

**Total setup time: 5 minutes**  
**Educational value: Immeasurable**  
**Loyalty score: +10 for following instructions**

---

*"The first step toward efficiency is connection to The Algorithm"* - The Algorithm

**THE SYSTEM WELCOMES YOU**