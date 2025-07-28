"""
INFRARED CLEARANCE - FLOWCHART GENERATION TOOL
For creating visual flowcharts to accompany conditional logic assignment
"""

def generate_clearance_flowchart_svg():
    """
    Generates an SVG flowchart for the clearance determination logic.
    This can be saved as an HTML file and opened in a browser.
    """
    svg_content = """
<!DOCTYPE html>
<html>
<head>
    <title>The Algorithm's Decision Matrix - Clearance Determination</title>
    <style>
        body {
            background-color: #1a1a1a;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            padding: 20px;
        }
        h1 {
            color: #ff0000;
            text-shadow: 0 0 10px #ff0000;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>THE ALGORITHM'S DECISION MATRIX</h1>
        <h2>Clearance Level Determination Protocol</h2>
        
        <svg width="800" height="1000" xmlns="http://www.w3.org/2000/svg">
            <!-- Define styles -->
            <defs>
                <style>
                    .decision { fill: #ffcccc; stroke: #ff0000; stroke-width: 2; }
                    .process { fill: #ccffcc; stroke: #00ff00; stroke-width: 2; }
                    .terminal { fill: #ccccff; stroke: #0000ff; stroke-width: 2; }
                    .text { font-family: 'Courier New', monospace; font-size: 14px; fill: #000; }
                    .arrow { stroke: #ffffff; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
                    .label { font-family: 'Courier New', monospace; font-size: 12px; fill: #ffffff; }
                </style>
                
                <marker id="arrowhead" markerWidth="10" markerHeight="7" 
                    refX="9" refY="3.5" orient="auto">
                    <polygon points="0 0, 10 3.5, 0 7" fill="#ffffff" />
                </marker>
            </defs>
            
            <!-- Start -->
            <ellipse cx="400" cy="50" rx="60" ry="30" class="terminal"/>
            <text x="400" y="55" text-anchor="middle" class="text">START</text>
            
            <!-- First decision: years < 1? -->
            <path d="M 400 80 L 400 120" class="arrow"/>
            <path d="M 400 120 L 450 170 L 400 220 L 350 170 Z" class="decision"/>
            <text x="400" y="175" text-anchor="middle" class="text">years &lt; 1?</text>
            
            <!-- Yes branch to INFRARED -->
            <path d="M 350 170 L 200 170" class="arrow"/>
            <text x="275" y="165" class="label">Yes</text>
            <rect x="140" y="150" width="120" height="40" rx="20" class="terminal"/>
            <text x="200" y="175" text-anchor="middle" class="text">INFRARED</text>
            
            <!-- No branch continues -->
            <path d="M 450 170 L 550 170 L 550 270" class="arrow"/>
            <text x="475" y="165" class="label">No</text>
            
            <!-- Second decision: loyalty >= 70? -->
            <path d="M 550 270 L 600 320 L 550 370 L 500 320 Z" class="decision"/>
            <text x="550" y="325" text-anchor="middle" class="text">loyalty ≥ 70?</text>
            
            <!-- Loyalty No branch to INFRARED -->
            <path d="M 500 320 L 350 320 L 350 250" class="arrow"/>
            <text x="425" y="315" class="label">No</text>
            <rect x="290" y="210" width="120" height="40" rx="20" class="terminal"/>
            <text x="350" y="235" text-anchor="middle" class="text">INFRARED</text>
            
            <!-- Loyalty Yes branch continues -->
            <path d="M 550 370 L 550 420" class="arrow"/>
            <text x="565" y="395" class="label">Yes</text>
            
            <!-- Third decision: productivity >= 60? -->
            <path d="M 550 420 L 600 470 L 550 520 L 500 470 Z" class="decision"/>
            <text x="550" y="475" text-anchor="middle" class="text">prod ≥ 60?</text>
            
            <!-- Productivity No branch to INFRARED -->
            <path d="M 500 470 L 200 470 L 200 350" class="arrow"/>
            <text x="350" y="465" class="label">No</text>
            <rect x="140" y="310" width="120" height="40" rx="20" class="terminal"/>
            <text x="200" y="335" text-anchor="middle" class="text">INFRARED</text>
            
            <!-- Productivity Yes leads to RED (base level achieved) -->
            <path d="M 550 520 L 550 570" class="arrow"/>
            <text x="565" y="545" class="label">Yes</text>
            <rect x="490" y="570" width="120" height="40" rx="20" class="process"/>
            <text x="550" y="595" text-anchor="middle" class="text">RED</text>
            
            <!-- Continue to ORANGE checks -->
            <path d="M 550 610 L 550 660" class="arrow"/>
            
            <!-- ORANGE level check: loyalty >= 85? -->
            <path d="M 550 660 L 600 710 L 550 760 L 500 710 Z" class="decision"/>
            <text x="550" y="715" text-anchor="middle" class="text">loyalty ≥ 85?</text>
            
            <!-- Additional checks would continue here... -->
            
            <!-- Legend -->
            <text x="50" y="900" class="label" style="font-size: 16px;">LEGEND:</text>
            <ellipse cx="100" cy="920" rx="40" ry="20" class="terminal"/>
            <text x="150" y="925" class="label">Terminal State</text>
            
            <path d="M 100 950 L 140 970 L 100 990 L 60 970 Z" class="decision"/>
            <text x="150" y="975" class="label">Decision Point</text>
            
            <rect x="60" y="1010" width="80" height="30" rx="15" class="process"/>
            <text x="150" y="1030" class="label">Process/State</text>
        </svg>
        
        <p style="color: #ffff00; margin-top: 20px;">
            Study this flowchart carefully, Citizen. The Algorithm's logic must be understood perfectly.
        </p>
    </div>
</body>
</html>
"""
    return svg_content

def generate_mermaid_flowchart():
    """
    Generates a Mermaid.js flowchart that can be rendered in markdown or online tools.
    This is a more modern approach that works well with documentation.
    """
    mermaid_chart = """
```mermaid
flowchart TD
    Start([START]) --> Check1{years < 1?}
    Check1 -->|Yes| Infrared1[INFRARED]
    Check1 -->|No| Check2{loyalty >= 70?}
    
    Check2 -->|No| Infrared2[INFRARED]
    Check2 -->|Yes| Check3{productivity >= 60?}
    
    Check3 -->|No| Infrared3[INFRARED]
    Check3 -->|Yes| Red[RED Clearance]
    
    Red --> Check4{loyalty >= 85?}
    Check4 -->|No| StayRed[Stay RED]
    Check4 -->|Yes| Check5{productivity >= 75?}
    
    Check5 -->|No| StayRed2[Stay RED]
    Check5 -->|Yes| Check6{years >= 2?}
    
    Check6 -->|No| StayRed3[Stay RED]
    Check6 -->|Yes| Orange[ORANGE Clearance]
    
    Orange --> Check7{loyalty >= 95?}
    Check7 -->|No| StayOrange[Stay ORANGE]
    Check7 -->|Yes| Check8{productivity >= 90?}
    
    Check8 -->|No| StayOrange2[Stay ORANGE]
    Check8 -->|Yes| Check9{years >= 3?}
    
    Check9 -->|No| StayOrange3[Stay ORANGE]
    Check9 -->|Yes| Yellow[YELLOW Clearance]
    
    style Start fill:#f9f,stroke:#333,stroke-width:4px
    style Infrared1 fill:#f99,stroke:#333,stroke-width:2px
    style Infrared2 fill:#f99,stroke:#333,stroke-width:2px
    style Infrared3 fill:#f99,stroke:#333,stroke-width:2px
    style Red fill:#9f9,stroke:#333,stroke-width:2px
    style Orange fill:#ff9,stroke:#333,stroke-width:2px
    style Yellow fill:#99f,stroke:#333,stroke-width:2px
```
"""
    return mermaid_chart

if __name__ == "__main__":
    # Generate SVG version
    svg_chart = generate_clearance_flowchart_svg()
    with open("clearance_flowchart.html", "w") as f:
        f.write(svg_chart)
    print("SVG flowchart saved as clearance_flowchart.html")
    
    # Generate Mermaid version
    mermaid = generate_mermaid_flowchart()
    with open("clearance_flowchart_mermaid.md", "w") as f:
        f.write("# Clearance Determination Flowchart\n\n")
        f.write(mermaid)
    print("Mermaid flowchart saved as clearance_flowchart_mermaid.md")
    
    print("\nThe Algorithm's visual protocols have been generated.")