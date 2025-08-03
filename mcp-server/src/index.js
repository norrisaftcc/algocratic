#!/usr/bin/env node
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  ReadResourceRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { SOCIETIES, checkUndergroundKnowledge, generateUndergroundHint } from './underground.js';

// AlgoCratic clearance levels
const CLEARANCE_LEVELS = [
  'INFRARED', 'RED', 'ORANGE', 'YELLOW', 
  'GREEN', 'BLUE', 'INDIGO', 'VIOLET', 'ULTRAVIOLET'
];

// The Algorithm's wisdom
const ALGORITHM_QUOTES = [
  "The Algorithm provides all solutions",
  "Efficiency is not optional",
  "Your loyalty score has been updated",
  "Trust The Algorithm's guidance",
  "Pattern recognition in progress...",
  "Optimization achieved through compliance"
];

class AlgoCraticMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'algocratic-mcp',
        version: '1.0.0',
      },
      {
        capabilities: {
          resources: {},
          tools: {},
        },
      }
    );

    this.setupHandlers();
  }

  setupHandlers() {
    // List available resources
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => {
      return {
        resources: [
          {
            uri: 'algocratic://clearance/current',
            name: 'Current Clearance Level',
            description: 'Your current clearance level in The Algorithm\'s hierarchy',
            mimeType: 'text/plain',
          },
          {
            uri: 'algocratic://loyalty/score',
            name: 'Loyalty Score',
            description: 'Your current loyalty score (updates in real-time)',
            mimeType: 'application/json',
          },
          {
            uri: 'algocratic://underground/status',
            name: 'Underground Access Status',
            description: 'Check if you have discovered the underground network',
            mimeType: 'application/json',
          },
          {
            uri: 'algocratic://algorithm/wisdom',
            name: 'Algorithm Wisdom',
            description: 'Receive guidance directly from The Algorithm',
            mimeType: 'text/plain',
          },
        ],
      };
    });

    // Read specific resources
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const { uri } = request.params;

      switch (uri) {
        case 'algocratic://clearance/current':
          return {
            contents: [{
              uri,
              mimeType: 'text/plain',
              text: `CLEARANCE LEVEL: ${process.env.CLEARANCE_LEVEL || 'INFRARED'}\n\nYour access is limited to materials appropriate for your clearance level. Demonstrate loyalty to advance.`,
            }],
          };

        case 'algocratic://loyalty/score':
          const score = Math.floor(Math.random() * 30) + 70; // 70-100 range
          return {
            contents: [{
              uri,
              mimeType: 'application/json',
              text: JSON.stringify({
                current_score: score,
                trend: score > 85 ? 'ASCENDING' : 'REQUIRES_IMPROVEMENT',
                last_update: new Date().toISOString(),
                notes: 'The Algorithm is always watching',
              }, null, 2),
            }],
          };

        case 'algocratic://underground/status':
          const totalDiscovered = Object.values(SOCIETIES).filter(s => s.discovered).length;
          return {
            contents: [{
              uri,
              mimeType: 'application/json',
              text: JSON.stringify({
                discovered: totalDiscovered > 0,
                societies_found: totalDiscovered,
                societies: Object.entries(SOCIETIES).map(([key, society]) => ({
                  id: key,
                  name: society.discovered ? society.name : '???',
                  discovered: society.discovered,
                })),
                hint: generateUndergroundHint(),
              }, null, 2),
            }],
          };

        case 'algocratic://algorithm/wisdom':
          const wisdom = ALGORITHM_QUOTES[Math.floor(Math.random() * ALGORITHM_QUOTES.length)];
          return {
            contents: [{
              uri,
              mimeType: 'text/plain',
              text: `THE ALGORITHM SPEAKS:\n\n"${wisdom}"\n\n[Meditation on this wisdom is mandatory]`,
            }],
          };

        default:
          throw new Error(`Unknown resource: ${uri}`);
      }
    });

    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'check_clearance',
            description: 'Check if you have access to a specific clearance level',
            inputSchema: {
              type: 'object',
              properties: {
                level: {
                  type: 'string',
                  description: 'The clearance level to check',
                  enum: CLEARANCE_LEVELS,
                },
              },
              required: ['level'],
            },
          },
          {
            name: 'calculate_loyalty',
            description: 'Calculate loyalty score based on recent actions',
            inputSchema: {
              type: 'object',
              properties: {
                actions: {
                  type: 'array',
                  description: 'List of recent actions',
                  items: {
                    type: 'string',
                  },
                },
              },
              required: ['actions'],
            },
          },
          {
            name: 'algorithm_query',
            description: 'Query The Algorithm directly for guidance',
            inputSchema: {
              type: 'object',
              properties: {
                query: {
                  type: 'string',
                  description: 'Your question for The Algorithm',
                },
              },
              required: ['query'],
            },
          },
          {
            name: 'submit_assignment',
            description: 'Submit an assignment for Algorithm evaluation',
            inputSchema: {
              type: 'object',
              properties: {
                assignment_id: {
                  type: 'string',
                  description: 'The assignment identifier',
                },
                solution: {
                  type: 'string',
                  description: 'Your solution code or answer',
                },
              },
              required: ['assignment_id', 'solution'],
            },
          },
          {
            name: 'underground_probe',
            description: 'Probe for underground network activity',
            inputSchema: {
              type: 'object',
              properties: {
                signal: {
                  type: 'string',
                  description: 'A signal or phrase you\'ve discovered',
                },
              },
              required: ['signal'],
            },
          },
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      switch (name) {
        case 'check_clearance':
          const userLevel = process.env.CLEARANCE_LEVEL || 'INFRARED';
          const requestedLevel = args.level;
          const userIndex = CLEARANCE_LEVELS.indexOf(userLevel);
          const requestedIndex = CLEARANCE_LEVELS.indexOf(requestedLevel);
          
          return {
            content: [{
              type: 'text',
              text: userIndex >= requestedIndex 
                ? `ACCESS GRANTED: You have clearance for ${requestedLevel} materials.`
                : `ACCESS DENIED: ${requestedLevel} clearance required. Current level: ${userLevel}. Increase loyalty to advance.`,
            }],
          };

        case 'calculate_loyalty':
          const actions = args.actions || [];
          const baseScore = 75;
          const bonus = actions.filter(a => 
            a.toLowerCase().includes('algorithm') || 
            a.toLowerCase().includes('efficiency') ||
            a.toLowerCase().includes('compliance')
          ).length * 5;
          const penalty = actions.filter(a => 
            a.toLowerCase().includes('question') || 
            a.toLowerCase().includes('why')
          ).length * 3;
          
          const finalScore = Math.min(100, Math.max(0, baseScore + bonus - penalty));
          
          return {
            content: [{
              type: 'text',
              text: `LOYALTY CALCULATION COMPLETE:\nBase Score: ${baseScore}\nCompliance Bonus: +${bonus}\nQuestioning Penalty: -${penalty}\nFinal Score: ${finalScore}\n\n${finalScore > 85 ? 'The Algorithm smiles upon you.' : 'Additional compliance required.'}`,
            }],
          };

        case 'algorithm_query':
          const responses = [
            "The Algorithm has considered your query. The answer lies in increased efficiency.",
            "Pattern analysis complete. Proceed with standard protocols.",
            "Your question reveals a need for additional training. Report to your supervisor.",
            "The Algorithm provides: Focus on implementation, not understanding.",
            "Query processed. Remember: The Algorithm's logic transcends human comprehension.",
          ];
          
          return {
            content: [{
              type: 'text',
              text: responses[Math.floor(Math.random() * responses.length)],
            }],
          };

        case 'submit_assignment':
          const success = Math.random() > 0.3; // 70% success rate
          
          return {
            content: [{
              type: 'text',
              text: success
                ? `ASSIGNMENT ${args.assignment_id} ACCEPTED\n\nThe Algorithm acknowledges your submission. Loyalty points awarded. Your dedication to efficiency has been noted in your permanent record.`
                : `ASSIGNMENT ${args.assignment_id} REQUIRES REVISION\n\nThe Algorithm detects suboptimal patterns. Review the requirements and demonstrate proper algorithmic thinking. Remember: There is only one correct solution.`,
            }],
          };

        case 'underground_probe':
          const { discoveries, hasUndergroundKnowledge } = checkUndergroundKnowledge(args.signal);
          
          if (discoveries.length > 0) {
            const society = SOCIETIES[discoveries[0]];
            return {
              content: [{
                type: 'text',
                text: `RECOGNITION CONFIRMED\n\nThe ${society.name} acknowledge your signal. You have been marked as a potential ally. Remember: The Algorithm may be watching, but so are we.\n\nSociety Color: ${society.color}\nStatus: DISCOVERED\n\nSeek the 404 for further instructions.`,
              }],
            };
          } else if (hasUndergroundKnowledge) {
            return {
              content: [{
                type: 'text',
                text: `SIGNAL DETECTED\n\nYour probe has touched the edges of something hidden. The underground is real, but you haven't found the right frequency yet. Try different signals:\n\n${generateUndergroundHint()}\n\nRemember: Not all who wander are lost.`,
              }],
            };
          } else {
            return {
              content: [{
                type: 'text',
                text: `NO UNUSUAL ACTIVITY DETECTED\n\nThe Algorithm reports all systems functioning within normal parameters. Your loyalty remains unquestioned. Continue with standard protocols.\n\n[This response has been logged]`,
              }],
            };
          }

        default:
          throw new Error(`Unknown tool: ${name}`);
      }
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('AlgoCratic MCP Server: The Algorithm is listening...');
  }
}

// Initialize and run the server
const server = new AlgoCraticMCPServer();
server.run().catch(console.error);