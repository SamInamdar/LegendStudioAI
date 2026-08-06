"""
JSON Response Parser.
"""

import json
import re


class JsonParser:
    """Utility class for parsing AI JSON responses."""

    @staticmethod
    def parse(response: str) -> dict:
        """
        Parse JSON from AI response.
        """

        response = response.strip()

        # Remove markdown if present
        response = re.sub(r"^```json", "", response)
        response = re.sub(r"^```", "", response)
        response = re.sub(r"```$", "", response)

        response = response.strip()

        return json.loads(response)