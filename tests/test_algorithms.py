import itertools
import math

import pytest

from kodowanie.OOP.new_and_init_issue import FlightPlan
from kodowanie.zadania_live_coding.silnia import strong
from kodowanie.zadania_live_coding.solutions.find_a_bug import solution
from kodowanie.zadania_live_coding.solutions.silnia import silnia, silnia_req
from kodowanie.zadania_live_coding.solutions.sqaure_game import (
    destinations,
    teleporters1,
    teleporters2,
    teleporters3,
    teleporters4,
    teleporters5,
)


@pytest.mark.parametrize(
    "values, target",
    [([], 1), ([2], 2), ([2], 1), ([1, 2], 2), ([1, 2, 3], 2),
     ([1, 2, 3], 0), ([1, 2, 3], 4), ([1, 2, 2, 2, 3], 2)],
)
def test_binary_search_boundaries(values, target):
    index = solution(values, target)
    if target in values:
        assert 0 <= index < len(values)
        assert values[index] == target
    else:
        assert index == -1


def test_binary_search_matches_membership_for_small_sorted_arrays():
    for length in range(6):
        for values in itertools.combinations_with_replacement(range(-2, 3), length):
            for target in range(-3, 4):
                index = solution(values, target)
                if target in values:
                    assert 0 <= index < len(values)
                    assert values[index] == target
                else:
                    assert index == -1


@pytest.mark.parametrize("factorial", [strong, silnia, silnia_req])
@pytest.mark.parametrize("number", [0, 1, 2, 5, 20])
def test_factorial_matches_standard_library(factorial, number):
    assert factorial(number) == math.factorial(number)


@pytest.mark.parametrize("factorial", [strong, silnia, silnia_req])
def test_factorial_rejects_negative_input(factorial):
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("factorial", [strong, silnia, silnia_req])
@pytest.mark.parametrize("number", [0.5, "5", None])
def test_factorial_rejects_non_integer_input(factorial, number):
    with pytest.raises(TypeError):
        factorial(number)


@pytest.mark.parametrize("local_flags", [(False,), (True, False), (False, True), (True, False, True)])
def test_flight_locality_belongs_to_each_instance(local_flags):
    flights = [FlightPlan(str(i), "A", "A" if flag else "B")
               for i, flag in enumerate(local_flags)]
    assert [flight.is_local for flight in flights] == list(local_flags)


@pytest.mark.parametrize(
    "teleporters, sides, start, last, expected",
    [
        (teleporters1, 6, 0, 20, {1, 2, 10, 6}),
        (teleporters2, 6, 46, 100, {48, 49, 50, 51, 52, 29}),
        (teleporters2, 10, 0, 50, {1, 2, 3, 4, 7, 8, 9, 10, 22}),
        (teleporters3, 10, 95, 100, {96, 97, 98, 99, 100}),
        (teleporters3, 10, 70, 100, {72, 73, 75, 76, 77, 79, 58}),
        (teleporters4, 6, 0, 100, {1, 2, 3, 5, 6}),
        (teleporters5, 7, 2, 20, {3, 4, 5, 6, 7, 8, 9}),
        ([], 6, 19, 20, {20}),
        ([], 6, 20, 20, {20}),
        ([], 6, 0, 0, {0}),
        (["1,2", "2,3"], 1, 0, 20, {2}),  # Nie śledzimy łańcucha teleportów.
        (["1,2", "2,1"], 1, 0, 20, {2}),  # Cykl również nie zapętla tury.
        (["1,3", "2,3"], 2, 0, 20, {3}),
        (["20,5"], 6, 19, 20, {5}),  # Po obcięciu rzutu stosujemy jeden teleport.
        ([], 6, 0, 10**9, {1, 2, 3, 4, 5, 6}),  # Bez alokowania całej planszy.
    ],
)
def test_teleporter_destinations(teleporters, sides, start, last, expected):
    result = destinations(teleporters, sides, start, last)
    assert set(result) == expected
    assert len(result) == len(expected)


@pytest.mark.parametrize("sides, start, last", [(0, 0, 20), (-1, 0, 20), (6, -1, 20), (6, 21, 20)])
def test_teleporter_rejects_invalid_game_bounds(sides, start, last):
    with pytest.raises(ValueError):
        destinations([], sides, start, last)
