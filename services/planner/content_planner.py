"""
Content Planner.
"""

from models.content_plan import ContentItem, ContentPlan


class ContentPlanner:
    """Generates a weekly content plan."""

    def generate(self) -> ContentPlan:

        plan = ContentPlan()

        plan.items.extend(
            [
                ContentItem(
                    day="Monday",
                    format="Short",
                    category="Suspense",
                    topic="The Poor Boy's Secret",
                    priority=1,
                ),
                ContentItem(
                    day="Monday",
                    format="Short",
                    category="Business",
                    topic="The Biggest Business Mistake",
                    priority=2,
                ),
                ContentItem(
                    day="Wednesday",
                    format="Long",
                    category="Success Story",
                    topic="From Poverty To Success",
                    priority=1,
                ),
            ]
        )

        return plan