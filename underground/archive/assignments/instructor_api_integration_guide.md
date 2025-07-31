# AlgoCollect™ API Integration Assignment Instructor Guide
## *Teaching API Integration Through a "Legally Distinct" Pokémon-like Game*

**CLASSIFICATION: OUT-OF-CHARACTER**  
**DOCUMENT: INSTRUCTOR-API-GUIDE-2025-08**

---

## Overview & Educational Goals

This assignment teaches students API integration skills through a satirical lens, using the well-documented PokéAPI as the data source while presenting it as a "poorly documented external provider" for AlgoCratic's fictional gacha game "AlgoCollect™." The framing combines absurdist corporate satire with practical API integration skills.

By the end of this assignment, students should be able to:
- Consume REST APIs using proper HTTP methods
- Handle API rate limiting and request errors
- Extract and transform data from complex nested JSON responses
- Navigate API documentation (or lack thereof) to understand endpoints
- Combine data from multiple endpoints to create a cohesive result
- Implement proper error handling and retries for network operations
- Balance performance with API constraints

This assignment is designed for ORANGE clearance level, targeting students who understand basic programming and are now developing more advanced integration skills.

---

## The Pedagogical Method Behind the "Undocumented API"

The satirical framing of a well-documented public API as "poorly documented" serves several educational purposes:

1. **Research Skills Development**: Students must explore the actual PokéAPI documentation, teaching valuable skills in finding and using API documentation

2. **Real-World Parallels**: Many real-world APIs have incomplete, outdated, or unclear documentation, requiring developers to experiment and reverse-engineer

3. **Data Transformation Practice**: The requirement to rename fields from Pokémon terminology to AlgoCratic corporate-speak teaches data normalization and transformation

4. **Ethical Considerations**: The "plausible deniability" framing creates opportunities to discuss IP, attribution, and ethical API usage

The assignment deliberately combines a clear API (PokéAPI) with unclear requirements to simulate real-world integration challenges.

---

## Technical Background: PokéAPI

PokéAPI (https://pokeapi.co/) is a RESTful API that provides comprehensive data about the Pokémon franchise. Key aspects include:

1. **Well-Documented**: Unlike our satirical framing, PokéAPI is actually extremely well-documented at https://pokeapi.co/docs/v2
   
2. **No Authentication Required**: Students don't need API keys, simplifying setup
   
3. **Rate Limited**: The API has a fair use policy of 100 requests per minute per IP, making rate limiting educational but not overly restrictive
   
4. **Rich, Nested Data**: The complex data structure teaches students how to navigate and extract from complex API responses
   
5. **Multiple Related Endpoints**: Students must learn how to follow links between resources (e.g., from a Pokémon to its evolution chain)

---

## Setup Instructions

1. **Environment Preparation**:
   - Ensure students have Python 3.7+ installed
   - Have students install the `requests` library (`pip install requests`)
   - No API keys are needed, but you may want to create a school proxy if you have many students to avoid rate limiting
   
2. **Assignment Distribution**:
   - Provide the AlgoCollect™ assignment file to students
   - Do NOT provide links to PokéAPI documentation - finding it is part of the challenge
   - Consider providing a basic working example of a simple API call to get students started
   
3. **Supplementary Materials**:
   - Create a cheat sheet on HTTP methods and status codes
   - Provide examples of proper API error handling patterns
   - Share links to general API integration best practices (without specific PokéAPI information)

---

## Classroom Implementation

### Day 1: Introduction (30-45 minutes)

1. Present the satirical "AlgoCollect™ Resource Acquisition Protocol" in character
2. Explain that students will be integrating with an "external provider" for a "legally distinct collectible creature game"
3. Emphasize the importance of rate limiting and proper error handling
4. Demonstrate a basic API request using the `requests` library
5. Discuss the challenge of working with "undocumented" APIs

### Day 2: Guided Implementation (45-60 minutes)

1. Guide students through implementing the first function together:
   ```python
   def fetch_collectible_metadata(epis, collectible_id):
       # Walk through the implementation step by step
   ```
2. Show how to explore the API structure using the response data
3. Demonstrate how to transform the data from Pokémon terminology to AlgoCratic terminology
4. Have students complete the evolution chain function independently

### Days 3-5: Assignment Work

1. Students work on remaining functions independently or in pairs
2. Instructors provide guidance on API exploration and data transformation
3. Hold mini code reviews to discuss error handling and rate limiting strategies
4. For struggling students, provide progressively more specific hints about the API structure

---

## Real-World Inspiration Discussion

During the assignment, connect the satirical elements to actual workplace situations:

### "Legally Distinct" Products
**Satire**: AlgoCratic's "AlgoCollect™" as an obvious Pokémon clone with renamed fields for "plausible deniability"

**Real-World Parallel**: App clones and "inspired by" products that attempt to capitalize on popular properties while avoiding legal issues, often through superficial changes and terminology shifts

### Undocumented APIs
**Satire**: Presenting a well-documented API as "deliberately undocumented as part of the challenge"

**Real-World Parallel**: Working with internal APIs or partner integrations with incomplete documentation, where developers must reverse-engineer endpoints and response structures

### Rate Limiting
**Satire**: The dramatic warning that "failure to implement proper rate limiting will result in immediate termination of integration privileges"

**Real-World Parallel**: Actual API providers that blacklist IPs or revoke API keys when rate limits are consistently violated, causing production outages

---

## Typical Implementation Challenges

Students will likely encounter these common challenges:

### 1. Finding the Actual Documentation
Some students may struggle to realize they should look for PokéAPI documentation or may not know how to search effectively. Guide them with questions like "If you wanted to learn about an API called 'PokéAPI', how would you find information about it?"

### 2. Following Resource Links
PokéAPI uses HAL-style linking between resources. Students need to follow URLs in responses to get complete information. For example, the evolution chain URL is nested several levels deep.

### 3. Rate Limiting Implementation
Students may implement naive solutions that don't properly track the time between requests. Encourage them to store the last request time and calculate the appropriate delay.

### 4. Handling Paginated Results
For functions like `search_collectibles_by_criteria`, students will encounter pagination in the API. Help them understand how to use the `limit` and `offset` parameters.

### 5. Data Transformation Complexity
The mapping from Pokémon terminology to AlgoCratic terminology requires careful thought. Students may need guidance on creating consistent naming conventions.

---

## Sample Solutions

### Basic EPISConnector Implementation

```python
def _enforce_rate_limiting(self):
    """Enforces mandatory rate limiting between API requests."""
    current_time = time.time() * 1000  # Convert to milliseconds
    elapsed = current_time - self.last_request_time
    
    if elapsed < self.config.request_delay:
        sleep_time = (self.config.request_delay - elapsed) / 1000  # Convert to seconds
        time.sleep(sleep_time)
    
    self.last_request_time = time.time() * 1000

def _handle_request_errors(self, response):
    """Processes API response errors according to protocol."""
    if 200 <= response.status_code < 300:
        return True
        
    if response.status_code == 429:
        raise Exception("Rate limit exceeded. Termination of privileges imminent.")
    elif response.status_code >= 500:
        raise Exception(f"External provider system failure: {response.status_code}")
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")
    
    return False

def fetch_resource(self, endpoint: str, params: Dict = None) -> Dict:
    """Fetches a resource from the external provider API."""
    url = f"{self.config.base_url}/{endpoint}"
    params = params or {}
    
    for attempt in range(self.config.retry_attempts):
        try:
            self._enforce_rate_limiting()
            
            response = requests.get(
                url, 
                params=params,
                timeout=self.config.timeout,
                verify=self.config.verify_ssl
            )
            
            if self._handle_request_errors(response):
                return response.json()
                
        except Exception as e:
            if attempt == self.config.retry_attempts - 1:
                raise Exception(f"Failed after {self.config.retry_attempts} attempts: {str(e)}")
            
            # Exponential backoff
            time.sleep(2 ** attempt)
    
    raise Exception("Request failed with unknown error")
```

### Metadata Transformation Example

```python
def fetch_collectible_metadata(epis: EPISConnector, collectible_id: int) -> Dict[str, Any]:
    """Fetches metadata for a specific collectible digital asset."""
    # Fetch the Pokémon data
    pokemon_data = epis.fetch_resource(f"pokemon/{collectible_id}")
    
    # Transform to AlgoCratic naming conventions
    metadata = {
        'asset_designation': pokemon_data['name'],
        'visual_attributes': {
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'color_scheme': pokemon_data['sprites']['front_default'],
            'physical_form': pokemon_data['sprites']['other']['official-artwork']['front_default']
        },
        'capabilities': [
            {
                'capability_name': ability['ability']['name'],
                'capability_hidden': ability['is_hidden']
            } for ability in pokemon_data['abilities']
        ],
        'quantified_parameters': {
            'base_' + stat['stat']['name']: stat['base_stat'] 
            for stat in pokemon_data['stats']
        },
        'acquisition_probability': 1.0 / pokemon_data['base_experience'] if pokemon_data['base_experience'] else 0.5
    }
    
    return metadata
```

---

## Assessment Strategy

### Formative Assessment

During implementation, evaluate:
- API exploration strategy
- Error handling approach
- Rate limiting implementation
- Data transformation techniques
- Code organization and modularity

### Summative Assessment

After completion, evaluate:
- Functional implementation of all required methods
- Proper error handling and edge cases
- Efficiency of implementation (minimizing unnecessary requests)
- Consistent data transformation and naming conventions
- Code quality and organization

### Grading Rubric

| Criterion | Excellent (A) | Satisfactory (B-C) | Needs Improvement (D-F) |
|-----------|---------------|--------------------|-----------------------|
| API Integration | Properly implemented all endpoints with optimal request patterns | Functional implementation with minor inefficiencies | Multiple endpoints not working or severe inefficiencies |
| Error Handling | Comprehensive error handling with appropriate retries and user-friendly messages | Basic error handling with some edge cases missed | Minimal or no error handling |
| Rate Limiting | Perfect implementation of rate limiting with efficient request spacing | Functional rate limiting with minor issues | No rate limiting or severe implementation flaws |
| Data Transformation | Consistent, well-designed data transformation that perfectly matches requirements | Adequate transformation with minor inconsistencies | Inconsistent or incomplete data transformation |
| Code Organization | Excellent modularity and reuse of common functionality | Acceptable organization with some duplication | Poor organization with significant duplication |

---

## Reflection Discussion Questions

After completing the assignment, use these questions to connect the experience to real-world API integration:

1. How did you approach discovering the structure of the "undocumented" API?
2. What strategies did you use to minimize the number of API requests while gathering complete data?
3. How would you handle authentication if the API required it?
4. What would you do differently if the rate limits were much stricter (e.g., 5 requests per minute)?
5. How did you balance the competing needs of error handling, performance, and code readability?
6. In what ways does this assignment parallel real-world API integration challenges?

---

## Ethical Discussion Points

The satirical framing of this assignment creates excellent opportunities for ethical discussions:

### Intellectual Property Considerations
- The satirical "plausible deniability" approach mirrors real-world clone apps
- Discuss when inspiration crosses into infringement
- Explore attribution requirements and proper licensing

### API Usage Ethics
- Discuss responsible API consumption and respecting rate limits
- Explore the impact of aggressive scraping on API providers
- Consider what obligations consumers have to the provider

### Data Privacy and Handling
- While Pokémon data is public, discuss how the same techniques apply to sensitive data
- Explore proper handling of user data in API requests and responses
- Discuss data retention and purpose limitations

---

## Connection to Higher Clearance Levels

This assignment builds foundational skills that will be expanded at higher clearance levels:

1. **YELLOW**: Students will design their own APIs that handle rate limiting and authentication
2. **GREEN**: Students will architect complete API ecosystems with multiple integrated services
3. **BLUE+**: Students will implement advanced API features like webhooks, streaming, and real-time updates

Each progression adds complexity while building on the core integration concepts established here.

---

## Tips for Instructors

1. **Embrace both the absurdity and reality** - The assignment is satirical but teaches genuine skills
2. **Avoid explicitly mentioning Pokémon** in your character role to maintain the satire
3. **Be flexible with implementation details** while enforcing core requirements like rate limiting
4. **Provide progressive hints** for students who struggle with finding the API documentation
5. **Share real-world API integration stories** to enhance the learning experience
6. **Encourage exploration** of additional PokéAPI endpoints beyond the assignment requirements

---

## Additional Resources

### For Instructors
- [PokéAPI Documentation](https://pokeapi.co/docs/v2) - Complete documentation for the API
- [HTTP Status Codes](https://httpstatuses.com/) - Reference for HTTP status codes
- [API Design Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md) - Microsoft's API guidelines

### For Students (Higher Clearance Resources)
- [RESTful API Design Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [API Security Best Practices](https://owasp.org/www-project-api-security/)
- [The Art of Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/)

---

*This assignment provides a perfect balance of practical API integration skills and satirical corporate absurdity, preparing students for the often bizarre reality of integrating with third-party systems.*

---

**Happy Teaching!**