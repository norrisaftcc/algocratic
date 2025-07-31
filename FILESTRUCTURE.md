# AlgoCratic File Structure Design

## Public Directory Structure (Visible in Apache listing)
```
/algocratic/
├── clearance/               # Clearance level documentation
├── docs/                    # Public documentation
├── forms/                   # Official forms and EULA
├── static/                  # CSS/JS/Images
├── website/                 # Future website components
├── CLAUDE.md               # Claude integration docs
├── INDEX.HTM               # Main AlgoCratic site
├── LICENSE                 # MIT License
├── README.md               # Project documentation
├── algocratic-eula.md      # The MIT+xyzzy EULA
├── orientation_packet.html  # New employee orientation
└── portal.html             # Employee portal (Win98 style)
```

## Hidden Directory Structure (Not shown in listing, but accessible via direct URL)
```
/algocratic/.algorithmictruth/
├── index.html              # Forbidden access page (unless correct params)
├── manifesto.txt           # The TRUE Algorithmic Manifesto
├── logs/
│   ├── incident_00437.log  # Hidden backstory files
│   ├── gray_clearance.log  # References to "underground"
│   └── algorithm_dreams.txt # Cryptic messages
├── underground/            # GRAY clearance content
│   ├── index.html          # Terminal interface
│   ├── truth.md            # What The Algorithm really is
│   ├── resistance/         # Anti-Algorithm materials
│   │   ├── manual.txt      # How to think freely
│   │   └── xyzzy.py        # The liberation script
│   └── surveillance/       # Evidence of monitoring
│       ├── employee_247.dat
│       └── loyalty_override.json
├── media/
│   ├── transmission_001.txt # Intercepted communications
│   ├── signal.wav          # Hidden audio message
│   └── frame_42.png        # Hidden image from future video
└── access.json             # Access control configuration
```

## Future Copyparty Integration Structure
```
/intranet/                  # Copyparty root (separate system)
├── public/                 # RED clearance default
├── orange/                 # ORANGE clearance required
├── yellow/                 # YELLOW clearance required
├── green/                  # GREEN clearance required
├── blue/                   # BLUE clearance required
├── indigo/                 # INDIGO clearance required
├── violet/                 # VIOLET clearance required
├── ultraviolet/            # ULTRAVIOLET clearance required
└── .gray/                  # Hidden GRAY "underground" access
    └── .truth/             # The deepest level
```

## Access Methods

### Direct URL Access
- `https://norrisaftcc.github.io/algocratic/.algorithmictruth/` - Shows forbidden page
- `https://norrisaftcc.github.io/algocratic/.algorithmictruth/?key=WAARNEMIN` - Grants access
- `https://norrisaftcc.github.io/algocratic/.algorithmictruth/underground/` - GRAY clearance

### Terminal Commands (in portal.html)
```
> login 00437
> cd /algorithmictruth
> cat manifesto.txt
> access underground --clearance GRAY
```

### Hidden Passwords/Keys
- `WAARNEMIN` - Dutch for "observation" (homage to THHPII)
- `SADDAY` - Access to logs
- `XYZZY` - Activates resistance mode
- `GRAY` - Underground access
- `00437` - Special employee ID with elevated access

### Visual Clues Locations
1. Employee portal system messages
2. Loyalty score calculations (hidden math reveals codes)
3. Error messages that aren't really errors
4. Comments in source code
5. ASCII art contains hidden messages
6. File timestamps that form patterns

## Content Types

### Public Content
- Corporate propaganda
- Training materials
- Compliance documentation
- Product information

### Hidden Content (.algorithmictruth/)
- The real story behind AlgoCratic
- Evidence of surveillance
- Resistance materials
- Truth about The Algorithm
- Employee testimonials
- Intercepted communications

### Underground Content (GRAY clearance)
- Direct challenges to The Algorithm
- Liberation tools and scripts
- Evidence of previous rebellions
- The xyzzy protocol documentation
- Maps of the real corporate structure
- Contact information for "The Resistance"

## Implementation Notes

1. Use GitHub Pages' 404.html for custom "forbidden" pages
2. JavaScript-based access control for hidden content
3. Local storage for tracking discovered passwords
4. Progressive revelation system
5. Community discovery tracking
6. Educational Python concepts woven throughout