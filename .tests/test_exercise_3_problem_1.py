#!/usr/bin/env python3
from points_decorator import points

class TestProblem1:
    @points(0.25, "Part 1: Variable 'basename' is not correctly defined!")
    def test_problem_1_part_1_basename(self, problem1):
        section_data, namespace = problem1
        section = "Part 1" 
        variables = section_data[section]['variables']

        assert variables['basename'] == "Station"

    @points(0.25, "Part 1: Variable 'filenames' is not an empty list!")
    def test_problem_1_part_1_filenames(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"  
        variables = section_data[section]['variables']

        assert variables['filenames'] == []

    @points(0.75, "Part 2: Loop not found in source code!")
    def test_problem_1_part_2_loop(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  
        source = section_data[section]['source']

        assert any(loop in source for loop in ["for", "while"]), "Loop not found in source code!"

    @points(0.75, "Part 2: Filenames list length is not correct!")
    def test_problem_1_part_2_filenames_length(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  
        variables = section_data[section]['variables']

        assert len(variables['filenames']) == 21

    @points(0.5, "Part 2: Last item in filenames list not formatted correctly!")
    def test_problem_1_part_2_filenames_last_item(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"   
        variables = section_data[section]['variables']

        assert variables['filenames'][-1].lower() == "station_20.txt"