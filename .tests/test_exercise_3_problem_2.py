#!/usr/bin/env python3
from points_decorator import points

class TestProblem2:

    @points(0.125, "Problem 2, Part 1: List `cold` is not correctly defined!")
    def test_problem2_part_1_cold(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']

        assert 'cold' in variables
        assert isinstance(variables['cold'], list)
        assert len(variables['cold']) == 0

    @points(0.125, "Problem 2, Part 1: List `warm` is not correctly defined!")
    def test_problem2_part_1_warm(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']

        assert 'warm' in variables, "warm is not defined"
        assert isinstance(variables['warm'], list), "warm is not a list"
        assert len(variables['warm']) == 0, "warm is not an empty list"

    @points(0.125, "Problem 2, Part 1: List `slippery` is not correctly defined!")
    def test_problem2_part_1_slippery(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']

        assert 'slippery' in variables
        assert isinstance(variables['slippery'], list)
        assert len(variables['slippery']) == 0

    @points(0.125, "Problem 2, Part 1: List `comfortable` is not correctly defined!")
    def test_problem2_part_1_comfortable(self, problem2):
        section_data, namespace = problem2
        section = "Part 1"  
        variables = section_data[section]['variables']

        assert 'comfortable' in variables
        assert isinstance(variables['comfortable'], list)
        assert len(variables['comfortable']) == 0

    @points(2, "Part 2: Loop not found in source code!")
    def test_problem2_part_2_loop(self, Problem2):
        section_data, namespace = problem2
        section = "Part 2" 
        source = section_data[section]['source']

        assert any(loop in source for loop in ["for", "while"])

    @points(0.5, "Problem 2, Part 3: Variable `slippery_times` is not correctly defined!")
    def test_problem2_part_3_slippery_times(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"  
        variables = section_data[section]['variables']

        assert variables['slippery_times'] == 16

    @points(0.5, "Problem 2, Part 3: Variable `warm_times` is not correctly defined!")
    def test_problem2_part_3_warm_times(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"  
        variables = section_data[section]['variables']

        assert variables['warm_times'] == 0

    @points(0.5, "Problem 2, Part 3: Variable `cold_times` is not correctly defined!")
    def test_problem2_part_3_cold_times(self, problem2):
        section_data, namespace = problem2
        section = "Part 3"  
        variables = section_data[section]['variables']

        assert variables['cold_times'] == 15


