# Claude Architectural Decisions and Planning

## Claude Code New Features (July 31, 2025)

### 🎉 Claude Code is Now Generally Available!
As of July 30, 2025, Claude Code has transitioned from research preview to general availability, powered by Claude Opus 4.

### Key New Features:

#### 1. IDE Integration & Background Tasks
- **Native VS Code and JetBrains integrations** - Run `claude-code` in your IDE terminal
- **Background tasks via GitHub Actions** - Long-running operations continue even when offline
- **Real-time file edits** - Changes appear directly in your editor for seamless pair programming

#### 2. GitHub Integration (Beta) 
- Tag Claude Code on PRs to:
  - Respond to reviewer feedback
  - Fix CI errors automatically
  - Modify code based on review comments
- Install with: `/install-github-app`

#### 3. Enhanced MCP (Model Context Protocol) Support
- **OAuth 2.0 authentication** with `/mcp` command
- **Remote MCP server support** with native OAuth
- **Resource referencing** using `@server:protocol://path` format
- **SSE and HTTP transports** for MCP servers

#### 4. Claude Code SDK
- Available in **TypeScript and Python**
- Build custom agents on top of Claude Code
- Extensible architecture for enterprise integrations

#### 5. Enterprise Features
- **Administrative dashboard** with real-time metrics
- Track AI tool usage, lines of code accepted, and costs per user
- Team visibility and analytics

#### 6. Platform Updates
- **Windows support** (as of July 16, 2025)
- Available on Pro ($20/month) and Max ($100-200/month) plans
- New weekly rate limits effective August 28, 2025

### Testing Commands
When working with Claude Code features:
- `npm test` - Run unit tests
- `npm run typecheck` - Check TypeScript types  
- `npm run lint` - Check code style
- `/install-github-app` - Set up GitHub integration
- `/mcp` - Configure MCP OAuth connections

## MCP Server Architecture (claude-conduit)

### Purpose
Create an educational MCP server that demonstrates how to connect external models to the Algocratic system, allowing students to interact with slope calculations and transformation functions through Claude Code.

### Key Architectural Decisions

1. **Server Type**: stdio-based MCP server (simplest for students to understand and deploy)
2. **Language**: TypeScript/Node.js (matches Algocratic's tech stack)
3. **Core Features**:
   - Resources: Access to slope calculations, transformation functions, loyalty points
   - Tools: Calculate slopes, apply transformations, simulate loyalty rewards
   - Prompts: Pre-built queries for common student exercises

4. **Project Structure**:
   ```
   claude-conduit/
   ├── src/
   │   ├── index.ts          # MCP server entry point
   │   ├── resources/        # Resource handlers
   │   ├── tools/           # Tool implementations
   │   └── algocratic/      # Integration with Algocratic logic
   ├── examples/            # Student examples
   ├── docs/               # Setup and usage guides
   └── package.json
   ```

5. **Integration Strategy**:
   - Import core algorithms from Algocratic as npm dependency
   - Expose simplified interfaces suitable for teaching
   - Include comprehensive error handling with educational messages

6. **Student Experience**:
   - Single command installation: `npm install -g claude-conduit`
   - Simple configuration in Claude settings
   - Progressive examples from basic to advanced

### Testing Commands
When working on this project, always run:
- `npm test` - Run unit tests
- `npm run typecheck` - Check TypeScript types
- `npm run lint` - Check code style

### Development Philosophy
- **Educational First**: Every design choice should make the system easier for students to understand
- **Progressive Disclosure**: Start simple, reveal complexity gradually
- **Real-World Connection**: Show how MCP servers enable AI to interact with production systems