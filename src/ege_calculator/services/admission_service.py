from ege_calculator.services.scoring_service import calculate_total_score
from ege_calculator.schemas.dto import ScoreResponse
import math


def admission_probability(user_score: int, passing_score: int) -> float:
    diff = user_score - passing_score
    k = 0.08
    p = 1 / (1 + math.exp(-k * diff))
    return round(p * 100, 1)


def calculate_chance(repo, request):
    program = repo.find_program(
        request.university,
        request.program
    )

    if program is None:
        raise ValueError("Program not found")

    total = calculate_total_score(
        request.russian,
        request.math,
        request.physics
    )

    required = program["min_score"]

    diff = total - required

    chance = max(0, min(100, 50 + diff * 2))

    return ScoreResponse(
        total_score=total,
        required_score=required,
        chance_percent=chance
    )
