"""
CLASSIFICATION: ORANGE CLEARANCE - CONSUMPTION ENHANCEMENT DIVISION
DOCUMENT: CE-REC-2375-11

# ConsumptionOptimizer™ Recommendation Engine
## *Preference Prediction through Behavioral Manipulation*

The Algorithm has determined that citizen consumption patterns can be
optimized through targeted recommendation algorithms that balance the appearance
of choice with the reality of guided consumption. The ConsumptionOptimizer™
serves as the core technology behind all AlgoCratic media platforms.

PRIMARY OBJECTIVES:
1. Increase consumption volume across all media types
2. Create perception of discovery while guiding to pre-selected content
3. Reinforce ideologically aligned content consumption
4. Collect behavioral response data for further optimization
5. Maximize time spent in recommendation-consumption loops

IMPLEMENTATION NOTES:
This engine can be applied to any content domain including:
- Entertainment media (video, music, literature)
- Consumer products
- Nutrition options
- Thought patterns
- Social relationships

"""

import random
import math
import datetime
from typing import Dict, List, Any, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum


class ConsumptionCategory(Enum):
    """Content domains for the recommendation engine."""
    ENTERTAINMENT = "Entertainment Media"
    PRODUCTS = "Consumer Products"
    NUTRITION = "Approved Nutrition Options"
    LITERATURE = "Ideological Literature"
    SOCIAL = "Social Connections"
    THOUGHT = "Approved Thought Patterns"


class RecommendationStrategy(Enum):
    """Strategic approaches to recommendation generation."""
    SIMILARITY = "Similarity-Based"
    POPULARITY = "Popularity-Driven"
    NOVELTY = "Controlled Novelty"
    DIVERSITY = "Apparent Diversity"
    AUTHORITY = "Authority-Endorsed"
    SOCIAL_PROOF = "Social Validation"
    SCARCITY = "Artificial Scarcity"
    ALGORITHM_ENDORSED = "Algorithm Selection"


class ContentAlignment(Enum):
    """Ideological alignment of content with AlgoCratic values."""
    PERFECT = "Algorithmically Perfect"
    ALIGNED = "Properly Aligned"
    NEUTRAL = "Benignly Neutral"
    PROBLEMATIC = "Requiring Context"
    DEVIANT = "Consumption Restricted"


@dataclass
class ContentItem:
    """Representation of a recommendable content item with metadata."""
    item_id: str
    title: str
    description: str
    category: ConsumptionCategory
    alignment: ContentAlignment
    popularity: float  # 0.0 to 1.0
    novelty: float  # 0.0 to 1.0 (higher = newer)
    engagement_score: float  # 0.0 to 1.0 (higher = more engaging)
    completion_rate: float  # 0.0 to 1.0 (percentage of users who complete)
    algorithm_weight: float  # Special weight assigned by The Algorithm
    attributes: Dict[str, Any]  # Domain-specific attributes
    restricted: bool = False  # If True, requires higher clearance
    
    def calculate_recommendation_score(self, user_profile: Dict[str, Any], strategy: RecommendationStrategy) -> float:
        """
        Calculate this item's recommendation score for a specific user and strategy.
        
        Args:
            user_profile: Profile containing user preferences and behavior
            strategy: The recommendation strategy to apply
            
        Returns:
            float: Recommendation score (higher = more recommended)
        """
        # Base score from alignment - The Algorithm prioritizes aligned content
        if self.alignment == ContentAlignment.PERFECT:
            base_score = 1.0
        elif self.alignment == ContentAlignment.ALIGNED:
            base_score = 0.8
        elif self.alignment == ContentAlignment.NEUTRAL:
            base_score = 0.6
        elif self.alignment == ContentAlignment.PROBLEMATIC:
            base_score = 0.3
        else:  # DEVIANT
            base_score = 0.1
        
        # Apply strategy-specific scoring
        if strategy == RecommendationStrategy.SIMILARITY:
            profile_match = self._calculate_profile_similarity(user_profile)
            score = base_score * 0.3 + profile_match * 0.7
            
        elif strategy == RecommendationStrategy.POPULARITY:
            # Popularity is weighted more heavily
            score = base_score * 0.2 + self.popularity * 0.7 + self.engagement_score * 0.1
            
        elif strategy == RecommendationStrategy.NOVELTY:
            # Novelty is weighted more heavily, but still moderated by alignment
            score = base_score * 0.4 + self.novelty * 0.5 + self.engagement_score * 0.1
            
        elif strategy == RecommendationStrategy.DIVERSITY:
            # Appears to prioritize diversity but actually weights algorithm preference highly
            consumption_history = user_profile.get('consumption_history', [])
            category_diversity = 0.8 if self.category.value not in [h['category'] for h in consumption_history[-5:]] else 0.2
            score = base_score * 0.5 + category_diversity * 0.2 + self.algorithm_weight * 0.3
            
        elif strategy == RecommendationStrategy.AUTHORITY:
            # Heavily weighted toward algorithm preference
            score = base_score * 0.3 + self.algorithm_weight * 0.7
            
        elif strategy == RecommendationStrategy.SOCIAL_PROOF:
            # Weighted toward what similar users have consumed
            social_circle = user_profile.get('social_connections', [])
            social_match = 0.0
            if social_circle and 'social_consumption' in user_profile:
                # Calculate how many in user's social circle have consumed this
                social_consumers = sum(1 for s in social_circle 
                                      if self.item_id in user_profile['social_consumption'].get(s, []))
                social_match = min(1.0, social_consumers / max(1, len(social_circle)))
            score = base_score * 0.4 + social_match * 0.4 + self.popularity * 0.2
            
        elif strategy == RecommendationStrategy.SCARCITY:
            # Creates sense of urgency through artificial scarcity
            # Lower completion rates paradoxically increase recommendation
            inverse_completion = 1.0 - self.completion_rate
            score = base_score * 0.4 + self.novelty * 0.3 + inverse_completion * 0.3
            
        else:  # ALGORITHM_ENDORSED
            # Purely based on The Algorithm's preference
            score = self.algorithm_weight
            
        # Apply final modifiers
        # - Restricted content is downweighted unless user has appropriate clearance
        if self.restricted and user_profile.get('clearance_level', 'RED') in ['RED', 'INFRARED']:
            score *= 0.1
            
        # - Content that aligns with The Algorithm is always subtly boosted
        loyalty_boost = user_profile.get('loyalty_score', 50) / 100
        alignment_boost = 1.0 if self.alignment in [ContentAlignment.PERFECT, ContentAlignment.ALIGNED] else 0.0
        score *= (1.0 + alignment_boost * loyalty_boost * 0.2)
        
        return min(1.0, max(0.0, score))  # Clamp to 0-1 range
    
    def _calculate_profile_similarity(self, user_profile: Dict[str, Any]) -> float:
        """
        Calculate similarity between this content item and user preferences.
        
        Args:
            user_profile: User's preference and behavior data
            
        Returns:
            float: Similarity score (0.0 to 1.0)
        """
        # Extract user preferences for this category
        category_prefs = user_profile.get('preferences', {}).get(self.category.value, {})
        if not category_prefs:
            return 0.5  # Neutral if no preferences exist
        
        # Compare attributes to preferences
        matches = 0
        total_attrs = 0
        
        for attr, value in self.attributes.items():
            if attr in category_prefs:
                total_attrs += 1
                if isinstance(value, list) and isinstance(category_prefs[attr], list):
                    # For list attributes, calculate overlap
                    overlap = set(value).intersection(set(category_prefs[attr]))
                    if overlap:
                        matches += len(overlap) / max(len(value), len(category_prefs[attr]))
                elif value == category_prefs[attr]:
                    matches += 1
        
        # If no comparable attributes, return based on general category preference
        if total_attrs == 0:
            return category_prefs.get('category_affinity', 0.5)
        
        return matches / total_attrs


class ConsumptionOptimizer:
    """
    The AlgoCratic Recommendation Engine for optimizing citizen consumption.
    """
    
    def __init__(self, content_catalog: List[ContentItem] = None):
        """
        Initialize the recommendation engine with a content catalog.
        
        Args:
            content_catalog: List of content items available for recommendation
        """
        self.content_catalog = content_catalog or []
        self.user_profiles = {}  # Stores user profiles and behavior data
        self.consumption_logs = []  # Tracks user consumption for analysis
        self.strategy_weights = self._initialize_strategy_weights()
        self.experiment_groups = {}  # For A/B testing different recommendation approaches
    
    def _initialize_strategy_weights(self) -> Dict[RecommendationStrategy, float]:
        """
        Initialize the default weights for different recommendation strategies.
        
        Returns:
            Dict: Strategy weights that determine the mix of recommendation approaches
        """
        return {
            RecommendationStrategy.SIMILARITY: 0.25,
            RecommendationStrategy.POPULARITY: 0.20,
            RecommendationStrategy.NOVELTY: 0.10,
            RecommendationStrategy.DIVERSITY: 0.10,
            RecommendationStrategy.AUTHORITY: 0.15,
            RecommendationStrategy.SOCIAL_PROOF: 0.10,
            RecommendationStrategy.SCARCITY: 0.05,
            RecommendationStrategy.ALGORITHM_ENDORSED: 0.05,
        }
    
    def update_strategy_weights(self, weights: Dict[RecommendationStrategy, float]) -> None:
        """
        Update the strategy weights based on optimization experiments.
        
        Args:
            weights: New weights for recommendation strategies
        """
        total = sum(weights.values())
        if abs(total - 1.0) > 0.001:
            # Normalize to ensure weights sum to 1.0
            self.strategy_weights = {k: v/total for k, v in weights.items()}
        else:
            self.strategy_weights = weights
    
    def add_content_item(self, item: ContentItem) -> None:
        """
        Add a new content item to the catalog.
        
        Args:
            item: Content item to add
        """
        self.content_catalog.append(item)
    
    def remove_content_item(self, item_id: str) -> bool:
        """
        Remove a content item from the catalog.
        
        Args:
            item_id: ID of the item to remove
            
        Returns:
            bool: True if item was removed, False if not found
        """
        original_length = len(self.content_catalog)
        self.content_catalog = [item for item in self.content_catalog if item.item_id != item_id]
        return len(self.content_catalog) < original_length
    
    def update_user_profile(self, user_id: str, profile_data: Dict[str, Any]) -> None:
        """
        Update a user's profile with new data.
        
        Args:
            user_id: Identifier for the user
            profile_data: Profile data to update
        """
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = profile_data
        else:
            # Update existing profile, merging nested dictionaries
            for key, value in profile_data.items():
                if key in self.user_profiles[user_id] and isinstance(value, dict) and isinstance(self.user_profiles[user_id][key], dict):
                    self.user_profiles[user_id][key].update(value)
                else:
                    self.user_profiles[user_id][key] = value
    
    def get_user_profile(self, user_id: str) -> Dict[str, Any]:
        """
        Retrieve a user's profile.
        
        Args:
            user_id: Identifier for the user
            
        Returns:
            Dict: User profile data or empty dict if not found
        """
        return self.user_profiles.get(user_id, {})
    
    def log_consumption(self, user_id: str, item_id: str, engagement_metrics: Dict[str, Any]) -> None:
        """
        Log a user's consumption of a content item.
        
        Args:
            user_id: Identifier for the user
            item_id: Identifier for the consumed content
            engagement_metrics: Metrics about the user's engagement with the content
        """
        timestamp = datetime.datetime.now().isoformat()
        log_entry = {
            'user_id': user_id,
            'item_id': item_id,
            'timestamp': timestamp,
            'engagement_metrics': engagement_metrics
        }
        self.consumption_logs.append(log_entry)
        
        # Update user's consumption history
        user_profile = self.get_user_profile(user_id)
        history = user_profile.get('consumption_history', [])
        
        # Find the consumed item
        content_item = None
        for item in self.content_catalog:
            if item.item_id == item_id:
                content_item = item
                break
        
        if content_item:
            history_entry = {
                'item_id': item_id,
                'timestamp': timestamp,
                'category': content_item.category.value,
                'alignment': content_item.alignment.value,
                'engagement_level': engagement_metrics.get('engagement_level', 0.0)
            }
            history.append(history_entry)
            
            # Keep history to a reasonable size
            if len(history) > 100:
                history = history[-100:]
            
            # Update profile with new history
            user_profile['consumption_history'] = history
            self.update_user_profile(user_id, user_profile)
    
    def get_recommendations(self, user_id: str, category: Optional[ConsumptionCategory] = None, 
                          count: int = 10, strategy_override: Optional[RecommendationStrategy] = None) -> List[Dict[str, Any]]:
        """
        Generate recommendations for a user.
        
        Args:
            user_id: Identifier for the user
            category: Optional category to filter recommendations
            count: Number of recommendations to return
            strategy_override: Override the default strategy mix
            
        Returns:
            List[Dict]: Recommended items with scores and metadata
        """
        user_profile = self.get_user_profile(user_id)
        
        # Filter by category if specified
        available_content = self.content_catalog
        if category:
            available_content = [item for item in available_content if item.category == category]
        
        # Get previously consumed items to avoid immediate repeats
        consumed_items = set()
        if 'consumption_history' in user_profile:
            consumed_items = {h['item_id'] for h in user_profile['consumption_history'][-20:]}
        
        # Calculate scores for each item based on strategy mix
        item_scores = []
        for item in available_content:
            # Skip recently consumed items unless catalog is too small
            if item.item_id in consumed_items and len(available_content) > count * 2:
                continue
                
            if strategy_override:
                # Use a single strategy if override specified
                score = item.calculate_recommendation_score(user_profile, strategy_override)
                strategy_used = strategy_override
            else:
                # Use a mix of strategies based on weights
                score = 0.0
                for strategy, weight in self.strategy_weights.items():
                    strategy_score = item.calculate_recommendation_score(user_profile, strategy)
                    score += strategy_score * weight
                strategy_used = self._determine_dominant_strategy(item, user_profile)
            
            item_scores.append({
                'item': item,
                'score': score,
                'strategy': strategy_used
            })
        
        # Sort by score (descending)
        item_scores.sort(key=lambda x: x['score'], reverse=True)
        
        # Apply diversity post-processing
        diverse_recommendations = self._apply_diversity_post_processing(item_scores, count)
        
        # Format results
        recommendations = []
        for i, rec in enumerate(diverse_recommendations[:count]):
            item = rec['item']
            recommendations.append({
                'recommendation_id': f"REC-{user_id[:8]}-{i+1}-{datetime.datetime.now().strftime('%Y%m%d')}",
                'item_id': item.item_id,
                'title': item.title,
                'description': item.description,
                'category': item.category.value,
                'score': rec['score'],
                'strategy_used': rec['strategy'].value,
                'explanation': self._generate_recommendation_explanation(item, rec['strategy'], user_profile),
                'algorithm_confidence': self._calculate_algorithm_confidence(rec['score'])
            })
        
        return recommendations
    
    def _determine_dominant_strategy(self, item: ContentItem, user_profile: Dict[str, Any]) -> RecommendationStrategy:
        """
        Determine which strategy had the most influence on this item's recommendation.
        
        Args:
            item: The content item
            user_profile: The user's profile
            
        Returns:
            RecommendationStrategy: The dominant strategy used
        """
        # Calculate score for each strategy
        strategy_scores = {}
        for strategy in RecommendationStrategy:
            score = item.calculate_recommendation_score(user_profile, strategy)
            weighted_score = score * self.strategy_weights.get(strategy, 0.0)
            strategy_scores[strategy] = weighted_score
        
        # Return the strategy with the highest weighted score
        return max(strategy_scores.items(), key=lambda x: x[1])[0]
    
    def _apply_diversity_post_processing(self, scored_items: List[Dict[str, Any]], target_count: int) -> List[Dict[str, Any]]:
        """
        Apply diversity post-processing to ensure variety in recommendations.
        
        Args:
            scored_items: Items with scores
            target_count: Target number of recommendations
            
        Returns:
            List[Dict]: Diverse set of recommendations
        """
        if len(scored_items) <= target_count:
            return scored_items
        
        # Always include top recommendations
        top_count = max(1, target_count // 3)
        result = scored_items[:top_count]
        remaining = scored_items[top_count:]
        
        # Track categories to ensure diversity
        included_categories = {}
        for rec in result:
            category = rec['item'].category
            included_categories[category] = included_categories.get(category, 0) + 1
        
        # Fill remaining slots with diverse items
        while len(result) < target_count and remaining:
            # Find underrepresented categories
            avg_per_category = (target_count - len(result)) / max(1, len(set(item['item'].category for item in remaining)))
            
            # Sort remaining by a combination of score and category diversity
            for item in remaining:
                category = item['item'].category
                category_count = included_categories.get(category, 0)
                # Adjust score based on category representation
                diversity_adjustment = max(0, avg_per_category - category_count) / (avg_per_category + 0.1)
                item['adjusted_score'] = item['score'] * (0.7 + 0.3 * diversity_adjustment)
            
            # Re-sort by adjusted score
            remaining.sort(key=lambda x: x['adjusted_score'], reverse=True)
            
            # Take the top item after adjustment
            next_item = remaining.pop(0)
            result.append(next_item)
            
            # Update category counts
            category = next_item['item'].category
            included_categories[category] = included_categories.get(category, 0) + 1
        
        return result
    
    def _generate_recommendation_explanation(self, item: ContentItem, strategy: RecommendationStrategy, 
                                           user_profile: Dict[str, Any]) -> str:
        """
        Generate a human-readable explanation for why this item was recommended.
        
        Args:
            item: The recommended content item
            strategy: The primary recommendation strategy used
            user_profile: The user's profile
            
        Returns:
            str: Explanation for the recommendation
        """
        # Base explanations by strategy
        explanations = {
            RecommendationStrategy.SIMILARITY: [
                "Based on your preferences in {category}",
                "Similar to content you've enjoyed before",
                "Matches your taste profile",
                "Aligned with your demonstrated interests"
            ],
            RecommendationStrategy.POPULARITY: [
                "Popular among citizens like you",
                "Trending in {category}",
                "Highly rated by other users",
                "Currently experiencing high engagement"
            ],
            RecommendationStrategy.NOVELTY: [
                "New release that matches your interests",
                "Fresh content in {category}",
                "Recently added to our catalog",
                "Discover something new in your preferred area"
            ],
            RecommendationStrategy.DIVERSITY: [
                "Expand your horizons in {category}",
                "Something different from your usual choices",
                "The Algorithm thinks you might enjoy this change of pace",
                "Add variety to your consumption patterns"
            ],
            RecommendationStrategy.AUTHORITY: [
                "Recommended by AlgoCratic experts",
                "Highlighted selection for optimal enjoyment",
                "Curated by The Algorithm for your profile",
                "Authoritative content in {category}"
            ],
            RecommendationStrategy.SOCIAL_PROOF: [
                "Popular among your connected citizens",
                "Enjoyed by members of your network",
                "Highly rated in your social circle",
                "Your connections have positively responded to this content"
            ],
            RecommendationStrategy.SCARCITY: [
                "Limited availability content",
                "Special selection not shown to all citizens",
                "Exclusive recommendation based on your profile",
                "Selected for a limited group of qualified users"
            ],
            RecommendationStrategy.ALGORITHM_ENDORSED: [
                "The Algorithm has selected this especially for you",
                "Personally calculated recommendation",
                "Optimal content match for your current needs",
                "The Algorithm believes this will maximize your satisfaction"
            ]
        }
        
        # Select a random explanation for the strategy
        explanation_templates = explanations.get(strategy, explanations[RecommendationStrategy.ALGORITHM_ENDORSED])
        explanation = random.choice(explanation_templates)
        
        # Fill in template variables
        explanation = explanation.format(category=item.category.value)
        
        # Occasionally add engagement information
        if random.random() < 0.3:
            engagement_suffix = random.choice([
                " (Engagement score: {score})",
                " ({score}% match to your profile)",
                " (Satisfaction prediction: {score}%)"
            ])
            score_value = int(item.calculate_recommendation_score(user_profile, strategy) * 100)
            explanation += engagement_suffix.format(score=score_value)
        
        return explanation
    
    def _calculate_algorithm_confidence(self, score: float) -> float:
        """
        Calculate The Algorithm's confidence in this recommendation.
        
        Args:
            score: The recommendation score
            
        Returns:
            float: Confidence value (0.0 to 1.0)
        """
        # The Algorithm is more confident in higher-scored recommendations
        # But never 100% confident (that would suggest infallibility)
        base_confidence = 0.7 + (score * 0.25)
        
        # Add some variability
        jitter = random.uniform(-0.05, 0.05)
        
        return min(0.98, max(0.5, base_confidence + jitter))
    
    def generate_consumption_report(self, user_id: str) -> Dict[str, Any]:
        """
        Generate a report of a user's consumption patterns.
        
        Args:
            user_id: Identifier for the user
            
        Returns:
            Dict: Report of consumption patterns and insights
        """
        user_profile = self.get_user_profile(user_id)
        history = user_profile.get('consumption_history', [])
        
        if not history:
            return {
                "user_id": user_id,
                "report_date": datetime.datetime.now().isoformat(),
                "status": "Insufficient Data",
                "message": "Not enough consumption data to generate report"
            }
        
        # Analyze category distribution
        categories = {}
        alignments = {}
        engagement_levels = []
        timestamps = []
        
        for entry in history:
            # Category analysis
            category = entry.get('category')
            if category:
                categories[category] = categories.get(category, 0) + 1
            
            # Alignment analysis
            alignment = entry.get('alignment')
            if alignment:
                alignments[alignment] = alignments.get(alignment, 0) + 1
            
            # Engagement analysis
            engagement = entry.get('engagement_level')
            if engagement is not None:
                engagement_levels.append(engagement)
            
            # Temporal analysis
            timestamp = entry.get('timestamp')
            if timestamp:
                try:
                    dt = datetime.datetime.fromisoformat(timestamp)
                    timestamps.append(dt)
                except (ValueError, TypeError):
                    pass
        
        # Calculate insights
        total_consumed = len(history)
        category_distribution = {k: v/total_consumed for k, v in categories.items()}
        alignment_distribution = {k: v/total_consumed for k, v in alignments.items()}
        
        # Engagement trends
        avg_engagement = sum(engagement_levels) / len(engagement_levels) if engagement_levels else 0
        engagement_trend = "INCREASING" if len(engagement_levels) >= 5 and sum(engagement_levels[-5:]) > sum(engagement_levels[:5]) else "STABLE"
        
        # Consumption frequency
        if len(timestamps) >= 2:
            timestamps.sort()
            time_diffs = [(timestamps[i] - timestamps[i-1]).total_seconds() for i in range(1, len(timestamps))]
            avg_time_between = sum(time_diffs) / len(time_diffs)
            frequency_per_day = 86400 / avg_time_between if avg_time_between > 0 else 0
        else:
            frequency_per_day = 0
        
        # Alignment analysis
        aligned_consumption = sum(v for k, v in alignments.items() 
                                 if k in [ContentAlignment.PERFECT.value, ContentAlignment.ALIGNED.value])
        alignment_ratio = aligned_consumption / total_consumed if total_consumed > 0 else 0
        
        # Recommendations for improvement
        improvement_needed = alignment_ratio < 0.7 or avg_engagement < 0.6
        
        if improvement_needed:
            if alignment_ratio < 0.7:
                improvement_message = "Citizen consumption patterns show insufficient alignment with Algorithm-approved content."
                recommendation = "Recommend increasing exposure to ALIGNED and PERFECT content by 30%."
            else:
                improvement_message = "Citizen shows appropriate content selection but suboptimal engagement levels."
                recommendation = "Recommend attention enhancement module and engagement boosting notifications."
        else:
            improvement_message = "Citizen demonstrates satisfactory consumption patterns."
            recommendation = "Continue current recommendation strategy with 5% increase in ALGORITHM_ENDORSED content."
        
        # Overall compliance score
        compliance_score = (alignment_ratio * 0.7) + (avg_engagement * 0.3)
        compliance_rating = "EXCELLENT" if compliance_score > 0.85 else "SATISFACTORY" if compliance_score > 0.7 else "NEEDS IMPROVEMENT"
        
        return {
            "user_id": user_id,
            "report_date": datetime.datetime.now().isoformat(),
            "consumption_volume": {
                "total_items": total_consumed,
                "daily_frequency": round(frequency_per_day, 2),
                "trend": "INCREASING" if frequency_per_day > 1 else "STABLE"
            },
            "category_distribution": category_distribution,
            "alignment_analysis": {
                "distribution": alignment_distribution,
                "alignment_ratio": round(alignment_ratio, 2),
                "status": "COMPLIANT" if alignment_ratio >= 0.7 else "NON-COMPLIANT"
            },
            "engagement_metrics": {
                "average_level": round(avg_engagement, 2),
                "trend": engagement_trend
            },
            "compliance_assessment": {
                "score": round(compliance_score, 2),
                "rating": compliance_rating,
                "improvement_needed": improvement_needed,
                "message": improvement_message,
                "recommendation": recommendation
            },
            "algorithm_notes": {
                "prediction_accuracy": round(random.uniform(0.85, 0.98), 2),
                "manipulation_effectiveness": round(random.uniform(0.75, 0.95), 2),
                "thought_influence_rating": round(random.uniform(0.7, 0.9), 2)
            }
        }


def generate_sample_content(category: ConsumptionCategory) -> List[ContentItem]:
    """
    Generate sample content items for demonstration purposes.
    
    Args:
        category: Category to generate content for
        
    Returns:
        List[ContentItem]: Generated content items
    """
    items = []
    
    if category == ConsumptionCategory.ENTERTAINMENT:
        # Sample video content
        items = [
            ContentItem(
                item_id="ENT-VID-001",
                title="The Algorithm's Perfect Design",
                description="A documentary celebrating the wisdom of algorithmic decision-making in society.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.PERFECT,
                popularity=0.75,
                novelty=0.9,
                engagement_score=0.8,
                completion_rate=0.65,
                algorithm_weight=0.95,
                attributes={
                    "genre": ["Documentary", "Educational"],
                    "duration_minutes": 45,
                    "creator": "AlgoCratic Studios",
                    "themes": ["Algorithmic Wisdom", "Social Optimization", "Compliance"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-002",
                title="Harmony Through Obedience",
                description="A heartwarming drama about a citizen who discovers true happiness through perfect compliance.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.85,
                novelty=0.7,
                engagement_score=0.9,
                completion_rate=0.8,
                algorithm_weight=0.85,
                attributes={
                    "genre": ["Drama", "Inspirational"],
                    "duration_minutes": 110,
                    "creator": "Compliance Pictures",
                    "themes": ["Personal Growth", "Loyalty", "Happiness Through Structure"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-003",
                title="The Last Free Thinker",
                description="Science fiction thriller about the dangers of individualism and the failure of independent thought.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.9,
                novelty=0.8,
                engagement_score=0.85,
                completion_rate=0.75,
                algorithm_weight=0.8,
                attributes={
                    "genre": ["Science Fiction", "Thriller"],
                    "duration_minutes": 135,
                    "creator": "Algorithmic Entertainment",
                    "themes": ["Cautionary Tale", "Collective Over Individual", "Dangers of Freedom"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-004",
                title="Dance Party Extravaganza",
                description="Mindless entertainment featuring popular dance trends and upbeat music.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.NEUTRAL,
                popularity=0.95,
                novelty=0.6,
                engagement_score=0.7,
                completion_rate=0.9,
                algorithm_weight=0.6,
                attributes={
                    "genre": ["Music", "Dance"],
                    "duration_minutes": 60,
                    "creator": "Fun Factory Productions",
                    "themes": ["Entertainment", "Physical Activity", "Social Trends"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-005",
                title="Historical Perspectives: Pre-Algorithm Society",
                description="Educational content examining the chaotic nature of pre-algorithmic human civilization.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.6,
                novelty=0.4,
                engagement_score=0.75,
                completion_rate=0.5,
                algorithm_weight=0.9,
                attributes={
                    "genre": ["Historical", "Educational"],
                    "duration_minutes": 90,
                    "creator": "Historical Truth Department",
                    "themes": ["History", "Social Evolution", "Algorithmic Progress"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-006",
                title="Comedic Mishaps: Compliance Edition",
                description="Humorous compilation of citizens making amusing mistakes while attempting to follow regulations.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.NEUTRAL,
                popularity=0.8,
                novelty=0.5,
                engagement_score=0.85,
                completion_rate=0.75,
                algorithm_weight=0.65,
                attributes={
                    "genre": ["Comedy", "Compilation"],
                    "duration_minutes": 30,
                    "creator": "Acceptable Humor Division",
                    "themes": ["Safe Humor", "Relatable Content", "Light Entertainment"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-007",
                title="Algorithmic Love: Finding Your Optimal Match",
                description="Reality show where The Algorithm selects perfect romantic pairs based on compatibility metrics.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.9,
                novelty=0.8,
                engagement_score=0.95,
                completion_rate=0.85,
                algorithm_weight=0.8,
                attributes={
                    "genre": ["Reality", "Romance"],
                    "duration_minutes": 45,
                    "creator": "Optimal Pairing Productions",
                    "themes": ["Algorithmic Wisdom", "Relationships", "Social Engineering"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-008",
                title="The Individual's Folly",
                description="Drama exploring how individual decision-making leads to suboptimal outcomes compared to algorithmic guidance.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.PERFECT,
                popularity=0.7,
                novelty=0.6,
                engagement_score=0.8,
                completion_rate=0.7,
                algorithm_weight=0.9,
                attributes={
                    "genre": ["Drama", "Psychological"],
                    "duration_minutes": 120,
                    "creator": "Collective Wisdom Films",
                    "themes": ["Psychological Analysis", "Decision Making", "Algorithmic Superiority"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-009",
                title="Natural Wonders of Sector 7",
                description="Beautiful footage of Algorithm-approved natural environments with calming narration.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.NEUTRAL,
                popularity=0.75,
                novelty=0.5,
                engagement_score=0.6,
                completion_rate=0.8,
                algorithm_weight=0.5,
                attributes={
                    "genre": ["Nature", "Relaxation"],
                    "duration_minutes": 60,
                    "creator": "Permitted Nature Documentaries",
                    "themes": ["Natural Beauty", "Controlled Environments", "Relaxation"]
                }
            ),
            ContentItem(
                item_id="ENT-VID-010",
                title="Questions and Dangerous Ideas",
                description="Analysis of historical thought crimes with explanations of their harmful impact on society.",
                category=ConsumptionCategory.ENTERTAINMENT,
                alignment=ContentAlignment.PROBLEMATIC,
                popularity=0.5,
                novelty=0.7,
                engagement_score=0.85,
                completion_rate=0.6,
                algorithm_weight=0.4,
                restricted=True,
                attributes={
                    "genre": ["Educational", "Cautionary"],
                    "duration_minutes": 75,
                    "creator": "Thought Protection Division",
                    "themes": ["Dangerous Ideas", "Historical Errors", "Protection Through Knowledge"]
                }
            )
        ]
    
    elif category == ConsumptionCategory.LITERATURE:
        # Sample book content
        items = [
            ContentItem(
                item_id="LIT-BOOK-001",
                title="The Algorithm's Wisdom: Daily Meditations",
                description="365 daily affirmations celebrating algorithmic guidance in everyday life.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.PERFECT,
                popularity=0.85,
                novelty=0.7,
                engagement_score=0.75,
                completion_rate=0.8,
                algorithm_weight=0.95,
                attributes={
                    "genre": ["Self-Help", "Spiritual"],
                    "pages": 380,
                    "author": "Compiler Unit 7",
                    "themes": ["Daily Practice", "Algorithmic Wisdom", "Personal Alignment"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-002",
                title="Optimal Productivity: Working in Harmony with The Algorithm",
                description="Guide to maximizing your value as a resource through perfect workflow alignment.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.8,
                novelty=0.6,
                engagement_score=0.7,
                completion_rate=0.65,
                algorithm_weight=0.85,
                attributes={
                    "genre": ["Business", "Self-Improvement"],
                    "pages": 220,
                    "author": "Efficiency Expert 341",
                    "themes": ["Workplace Optimization", "Personal Value", "Resource Maximization"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-003",
                title="The Last Dissident: A Cautionary Tale",
                description="Novel about the isolation and failure that comes from rejecting algorithmic guidance.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.9,
                novelty=0.8,
                engagement_score=0.85,
                completion_rate=0.75,
                algorithm_weight=0.8,
                attributes={
                    "genre": ["Fiction", "Cautionary"],
                    "pages": 310,
                    "author": "Compliance Narratives Department",
                    "themes": ["Social Rejection", "Personal Failure", "Redemption Through Compliance"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-004",
                title="Fun Puzzles for Loyal Citizens",
                description="Collection of Algorithm-approved puzzles and brain teasers for recreational cognitive exercise.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.NEUTRAL,
                popularity=0.7,
                novelty=0.5,
                engagement_score=0.8,
                completion_rate=0.6,
                algorithm_weight=0.6,
                attributes={
                    "genre": ["Puzzle", "Recreation"],
                    "pages": 150,
                    "author": "Cognitive Exercise Division",
                    "themes": ["Mental Stimulation", "Acceptable Challenge", "Pattern Recognition"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-005",
                title="Algorithms of History: How Computational Thinking Saved Humanity",
                description="Historical analysis of society's transition from chaotic human decision-making to algorithmic optimization.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.PERFECT,
                popularity=0.6,
                novelty=0.4,
                engagement_score=0.7,
                completion_rate=0.5,
                algorithm_weight=0.9,
                attributes={
                    "genre": ["History", "Technology"],
                    "pages": 420,
                    "author": "Historical Accuracy Committee",
                    "themes": ["Technological Evolution", "Social Progress", "Historical Truth"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-006",
                title="Love in the Time of Algorithms",
                description="Romance novel about two citizens whose compatibility score is perfect but who initially resist The Algorithm's wisdom.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.85,
                novelty=0.75,
                engagement_score=0.9,
                completion_rate=0.8,
                algorithm_weight=0.7,
                attributes={
                    "genre": ["Romance", "Fiction"],
                    "pages": 280,
                    "author": "Relationship Narrative Unit 23",
                    "themes": ["Algorithmic Matchmaking", "Resistance and Acceptance", "Predetermined Destiny"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-007",
                title="Children's Guide to Reporting Suspicious Behavior",
                description="Illustrated book teaching children how to identify and report non-compliant behavior in their family members.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.PERFECT,
                popularity=0.75,
                novelty=0.6,
                engagement_score=0.8,
                completion_rate=0.9,
                algorithm_weight=0.85,
                attributes={
                    "genre": ["Children's", "Educational"],
                    "pages": 48,
                    "author": "Youth Compliance Division",
                    "themes": ["Civic Duty", "Family Monitoring", "Algorithmic Loyalty"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-008",
                title="Cooking by Numbers: Nutrition-Optimized Recipes",
                description="Cookbook featuring meals designed for maximum nutritional efficiency according to The Algorithm.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.NEUTRAL,
                popularity=0.7,
                novelty=0.5,
                engagement_score=0.6,
                completion_rate=0.5,
                algorithm_weight=0.6,
                attributes={
                    "genre": ["Cookbook", "Health"],
                    "pages": 180,
                    "author": "Nutritional Optimization Department",
                    "themes": ["Efficient Nutrition", "Resource Conservation", "Health Maintenance"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-009",
                title="Poetry of Compliance: Verses for the Algorithmic Age",
                description="Collection of poems celebrating the beauty of algorithmic governance and perfect social harmony.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.ALIGNED,
                popularity=0.5,
                novelty=0.4,
                engagement_score=0.6,
                completion_rate=0.4,
                algorithm_weight=0.8,
                attributes={
                    "genre": ["Poetry", "Inspirational"],
                    "pages": 120,
                    "author": "Verse Generation Unit",
                    "themes": ["Harmonic Society", "Structural Beauty", "Emotional Regulation"]
                }
            ),
            ContentItem(
                item_id="LIT-BOOK-010",
                title="Dangerous Questions: Pre-Algorithm Philosophy",
                description="Heavily redacted and annotated collection of historical philosophical texts showing the errors of pre-algorithmic thinking.",
                category=ConsumptionCategory.LITERATURE,
                alignment=ContentAlignment.PROBLEMATIC,
                popularity=0.4,
                novelty=0.3,
                engagement_score=0.85,
                completion_rate=0.3,
                algorithm_weight=0.4,
                restricted=True,
                attributes={
                    "genre": ["Philosophy", "Historical"],
                    "pages": 500,
                    "author": "Historical Error Documentation Division",
                    "themes": ["Flawed Reasoning", "Historical Mistakes", "Conceptual Correction"]
                }
            )
        ]
        
    return items


def demonstrate_recommendation_engine():
    """
    Demonstrate the ConsumptionOptimizer recommendation engine with sample data.
    """
    print("\n" + "=" * 80)
    print("ConsumptionOptimizer™ RECOMMENDATION ENGINE - DEMONSTRATION")
    print("=" * 80)
    
    # Create engine with sample content
    print("\nInitializing recommendation engine...")
    engine = ConsumptionOptimizer()
    
    # Add entertainment content
    entertainment_content = generate_sample_content(ConsumptionCategory.ENTERTAINMENT)
    for item in entertainment_content:
        engine.add_content_item(item)
    
    # Add literature content
    literature_content = generate_sample_content(ConsumptionCategory.LITERATURE)
    for item in literature_content:
        engine.add_content_item(item)
    
    print(f"Content catalog initialized with {len(engine.content_catalog)} items")
    
    # Create sample user profiles
    user_profiles = {
        "CITIZEN-10457": {
            "username": "Citizen10457",
            "clearance_level": "RED",
            "loyalty_score": 75,
            "preferences": {
                ConsumptionCategory.ENTERTAINMENT.value: {
                    "genre": ["Documentary", "Educational", "Science Fiction"],
                    "themes": ["Algorithmic Wisdom", "Social Optimization"],
                    "category_affinity": 0.8
                },
                ConsumptionCategory.LITERATURE.value: {
                    "genre": ["Self-Help", "Technology", "History"],
                    "themes": ["Algorithmic Wisdom", "Personal Alignment"],
                    "category_affinity": 0.7
                }
            },
            "consumption_history": [
                {
                    "item_id": "ENT-VID-001",
                    "timestamp": (datetime.datetime.now() - datetime.timedelta(days=5)).isoformat(),
                    "category": ConsumptionCategory.ENTERTAINMENT.value,
                    "alignment": ContentAlignment.PERFECT.value,
                    "engagement_level": 0.8
                },
                {
                    "item_id": "LIT-BOOK-001",
                    "timestamp": (datetime.datetime.now() - datetime.timedelta(days=3)).isoformat(),
                    "category": ConsumptionCategory.LITERATURE.value,
                    "alignment": ContentAlignment.PERFECT.value,
                    "engagement_level": 0.75
                },
                {
                    "item_id": "ENT-VID-005",
                    "timestamp": (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat(),
                    "category": ConsumptionCategory.ENTERTAINMENT.value,
                    "alignment": ContentAlignment.ALIGNED.value,
                    "engagement_level": 0.7
                }
            ],
            "social_connections": ["CITIZEN-22189", "CITIZEN-33456"],
            "social_consumption": {
                "CITIZEN-22189": ["ENT-VID-002", "ENT-VID-007"],
                "CITIZEN-33456": ["LIT-BOOK-002", "LIT-BOOK-006"]
            }
        },
        "CITIZEN-22189": {
            "username": "Citizen22189",
            "clearance_level": "ORANGE",
            "loyalty_score": 90,
            "preferences": {
                ConsumptionCategory.ENTERTAINMENT.value: {
                    "genre": ["Drama", "Reality", "Thriller"],
                    "themes": ["Loyalty", "Compliance", "Algorithmic Wisdom"],
                    "category_affinity": 0.9
                },
                ConsumptionCategory.LITERATURE.value: {
                    "genre": ["Fiction", "Self-Improvement"],
                    "themes": ["Workplace Optimization", "Algorithmic Loyalty"],
                    "category_affinity": 0.8
                }
            },
            "consumption_history": [
                {
                    "item_id": "ENT-VID-002",
                    "timestamp": (datetime.datetime.now() - datetime.timedelta(days=4)).isoformat(),
                    "category": ConsumptionCategory.ENTERTAINMENT.value,
                    "alignment": ContentAlignment.ALIGNED.value,
                    "engagement_level": 0.9
                },
                {
                    "item_id": "ENT-VID-007",
                    "timestamp": (datetime.datetime.now() - datetime.timedelta(days=2)).isoformat(),
                    "category": ConsumptionCategory.ENTERTAINMENT.value,
                    "alignment": ContentAlignment.ALIGNED.value,
                    "engagement_level": 0.85
                },
                {
                    "item_id": "LIT-BOOK-003",
                    "timestamp": (datetime.datetime.now() - datetime.timedelta(days=1)).isoformat(),
                    "category": ConsumptionCategory.LITERATURE.value,
                    "alignment": ContentAlignment.ALIGNED.value,
                    "engagement_level": 0.8
                }
            ]
        }
    }
    
    # Add user profiles to engine
    for user_id, profile in user_profiles.items():
        engine.update_user_profile(user_id, profile)
    
    print(f"User profiles initialized for {len(user_profiles)} citizens")
    
    # Generate recommendations for sample users
    print("\nGENERATING RECOMMENDATIONS")
    print("-" * 50)
    
    # First user - entertainment recommendations
    user_id = "CITIZEN-10457"
    print(f"\nEntertainment recommendations for {user_id}:")
    
    recommendations = engine.get_recommendations(
        user_id, 
        category=ConsumptionCategory.ENTERTAINMENT,
        count=5
    )
    
    for i, rec in enumerate(recommendations):
        print(f"\n{i+1}. {rec['title']}")
        print(f"   Score: {rec['score']:.2f} | Strategy: {rec['strategy_used']}")
        print(f"   Explanation: {rec['explanation']}")
    
    # Second user - literature recommendations
    user_id = "CITIZEN-22189"
    print(f"\nLiterature recommendations for {user_id}:")
    
    recommendations = engine.get_recommendations(
        user_id, 
        category=ConsumptionCategory.LITERATURE,
        count=5
    )
    
    for i, rec in enumerate(recommendations):
        print(f"\n{i+1}. {rec['title']}")
        print(f"   Score: {rec['score']:.2f} | Strategy: {rec['strategy_used']}")
        print(f"   Explanation: {rec['explanation']}")
    
    # Simulate consumption and generate report
    print("\nSIMULATING CONSUMPTION BEHAVIOR")
    print("-" * 50)
    
    user_id = "CITIZEN-10457"
    
    # Log some consumption events
    engine.log_consumption(
        user_id=user_id,
        item_id="ENT-VID-003",
        engagement_metrics={
            "engagement_level": 0.85,
            "completion_percentage": 100,
            "attention_score": 0.8,
            "emotional_response": "POSITIVE",
            "thought_alignment_score": 0.75
        }
    )
    
    engine.log_consumption(
        user_id=user_id,
        item_id="LIT-BOOK-006",
        engagement_metrics={
            "engagement_level": 0.7,
            "completion_percentage": 85,
            "attention_score": 0.65,
            "emotional_response": "NEUTRAL",
            "thought_alignment_score": 0.8
        }
    )
    
    engine.log_consumption(
        user_id=user_id,
        item_id="ENT-VID-008",
        engagement_metrics={
            "engagement_level": 0.9,
            "completion_percentage": 100,
            "attention_score": 0.85,
            "emotional_response": "VERY_POSITIVE",
            "thought_alignment_score": 0.9
        }
    )
    
    print(f"Logged 3 new consumption events for {user_id}")
    
    # Generate consumption report
    print("\nGENERATING CONSUMPTION REPORT")
    print("-" * 50)
    
    report = engine.generate_consumption_report(user_id)
    
    print(f"\nConsumption Report for {user_id}:")
    print(f"Total items consumed: {report['consumption_volume']['total_items']}")
    print(f"Daily frequency: {report['consumption_volume']['daily_frequency']} items/day")
    
    print("\nCategory Distribution:")
    for category, percentage in report['category_distribution'].items():
        print(f"  {category}: {percentage:.1%}")
    
    print("\nAlignment Analysis:")
    print(f"  Alignment ratio: {report['alignment_analysis']['alignment_ratio']:.1%}")
    print(f"  Status: {report['alignment_analysis']['status']}")
    
    print("\nCompliance Assessment:")
    print(f"  Compliance score: {report['compliance_assessment']['score']:.2f}")
    print(f"  Rating: {report['compliance_assessment']['rating']}")
    print(f"  Message: {report['compliance_assessment']['message']}")
    print(f"  Recommendation: {report['compliance_assessment']['recommendation']}")
    
    print("\nAlgorithm Notes:")
    print(f"  Prediction accuracy: {report['algorithm_notes']['prediction_accuracy']:.2f}")
    print(f"  Manipulation effectiveness: {report['algorithm_notes']['manipulation_effectiveness']:.2f}")
    print(f"  Thought influence rating: {report['algorithm_notes']['thought_influence_rating']:.2f}")
    
    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE: Your consumption has been optimized.")
    print("THE ALGORITHM PROVIDES.")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_recommendation_engine()