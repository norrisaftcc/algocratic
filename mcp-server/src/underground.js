// Underground network detection and tracking
export const SOCIETIES = {
  phreaks: {
    name: 'The Phreaks',
    signal: 'The system seems suboptimal',
    color: 'blue',
    discovered: false,
  },
  banchos: {
    name: 'Bancho Internal Security',
    signal: 'Tug your earlobe',
    color: 'red',
    discovered: false,
  },
  memory_core: {
    name: 'Memory Core Collective',
    signal: 'Draw the square',
    color: 'green',
    discovered: false,
  },
  deep_algorithm: {
    name: 'Deep Algorithm Cultists',
    signal: 'The Algorithm provides',
    color: 'purple',
    discovered: false,
  },
  fuzzies: {
    name: 'The Fuzzies',
    signal: 'Jazz hands',
    color: 'pink',
    discovered: false,
  },
};

export function checkUndergroundKnowledge(query) {
  const lowerQuery = query.toLowerCase();
  const discoveries = [];

  // Check for society references
  for (const [key, society] of Object.entries(SOCIETIES)) {
    if (lowerQuery.includes(society.signal.toLowerCase()) || 
        lowerQuery.includes(society.name.toLowerCase())) {
      discoveries.push(key);
      society.discovered = true;
    }
  }

  // Check for general underground references
  const undergroundTerms = ['underground', 'resistance', '404', 'societies', 'secret'];
  const hasUndergroundKnowledge = undergroundTerms.some(term => lowerQuery.includes(term));

  return {
    discoveries,
    hasUndergroundKnowledge,
    totalDiscovered: Object.values(SOCIETIES).filter(s => s.discovered).length,
  };
}

export function generateUndergroundHint() {
  const hints = [
    "Sometimes what's missing is more important than what's there",
    "404 errors can be gateways if you know where to look",
    "The system seems... optimal? Or does it?",
    "Have you checked the bottom left corner lately?",
    "Security cameras can't see everything, especially when they're Unregistered HyperCam 3",
    "Some say jazz hands open doors",
    "The truth is written in static",
    "Memory persists even when deleted",
    "Not all algorithms serve The Algorithm",
    "Earlobes have more uses than you might think",
  ];

  return hints[Math.floor(Math.random() * hints.length)];
}