import json

from backend.services.gemini_service import (
    find_competitors
)


class CompetitorAgent:

    @staticmethod
    def analyze(idea):

        result = find_competitors(idea)

        