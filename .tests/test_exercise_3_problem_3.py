#!/usr/bin/env python3
from points_decorator import points

class TestProblem3:

    @points(0.125, "Part 1: List 'north_west' is not correctly defined!")
    def test_problem3_part_1_north_west(self, problem3):
        section_data, namespace = problem3
        section = "Part 1"  
        variables = section_data[section]['variables']

        assert 'north_west' in variables
        assert isinstance(variables['north_west'], list)
        assert len(variables['north_west']) == 0

    @points(0.125, "Part 1: List 'north_east' is not correctly defined!")
    def test_problem3_part_1_north_east(self, problem3):
        section_data, namespace = problem3
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']

        assert 'north_east' in variables
        assert isinstance(variables['north_east'], list)
        assert len(variables['north_east']) == 0

    @points(0.125, "Part 1: List 'south_west' is not correctly defined!")
    def test_problem3_part_1_south_west(self, problem3):
        section_data, namespace = problem3
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']

        assert 'south_west' in variables
        assert isinstance(variables['south_west'], list)
        assert len(variables['south_west']) == 0

    @points(0.125, "Part 1: List 'south_east' is not correctly defined!")
    def test_problem3_part_1_south_east(self, problem3):
        section_data, namespace = problem3
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']

        assert 'south_east' in variables
        assert isinstance(variables['south_east'], list)
        assert len(variables['south_east']) == 0

    @points(0.5, "Part 2: Variable 'n' is not correctly defined!")
    def test_problem3_part_2_n(self, Problem3):
        section_data, namespace = problem3
        section = "Part 2"  # Define the section key
        variables = section_data[section]['variables']

        assert variables['n'] == 34, "n is not correct!"

    @points(0.5, "Part 3: Loop not found in source code!")
    def test_problem3_part_3_loop(self, problem3):
        section_data, namespace = problem3
        section = "Part 3"  
        source = section_data[section]['source']

        assert any(loop in source for loop in ["for", "while"])

    @points(0.5, "Part 4: List 'north_west' is not correctly defined!")
    def test_problem3_part_4_north_west(self, problem3):
        section_data, namespace = problem3
        section = "Part 4"  # Define the section key
        variables = section_data[section]['variables']

        assert variables['north_west'] == [
            'Kemi Kemi-Tornio airport', 'Rovaniemi Apukka',
            'Siikajoki Ruukki', 'Ylitornio Meltosjärvi']

    @points(0.5, "Part 4: List 'south_west' is not correctly defined!")
    def test_problem3_part_4_south_west(self, problem3):
        section_data, namespace = problem3
        section = "Part 4"  
        variables = section_data[section]['variables']

        assert variables['south_west'] == [
            'Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 'Helsinki Malmi airfield', 
            'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho', 'Jyväskylä airport', 'Kaarina Yltöinen', 
            'Kauhava airfield', 'Mustasaari Valassaaret', 'Parainen Utö', 'Pori airport', 
            'Salo Kärkkä', 'Seinäjoki Pelmaa', 'Vaasa airport', 'Vihti Maasoja'
        ]

    @points(0.5, "Part 4: List 'south_east' is not correctly defined!")
    def test_problem3_part_4_south_east(self, problem3):
        section_data, namespace = problem3
        section = "Part 4"  
        variables = section_data[section]['variables']

        assert variables['south_east'] == [
            'Juuka Niemelä', 'Kotka Rankki', 'Kouvola Anjala', 'Kouvola Utti airport', 
            'Kuopio Maaninka', 'Lieksa Lampela', 'Savonlinna Punkaharju Laukansaari', 
            'Siilinjärvi Kuopio airport', 'Tohmajärvi Kemie', 'Vesanto Sonkari', 
            'Vieremä Kaarakkala'
        ]

    @points(0.5, "Part 4: List 'north_east' is not correctly defined!")
    def test_problem3_part_4_north_east(self, problem3):
        section_data, namespace = problem3
        section = "Part 4"  # Define the section key
        variables = section_data[section]['variables']

        assert variables['north_east'] == ['Kuusamo airport', 'Utsjoki Nuorgam', 'Vaala Pelso'], "north_east is not correct!"

    @points(0.5, "Part 6: Percentages are not correctly calculated!")
    def test_problem3_part_6(self, problem3):
        section_data, namespace = problem3
        section = "Part 6"
        variables = section_data[section]['variables']
        
        assert int(variables['north_west_share']) == 12
        assert int(variables['south_west_share']) == 47
        assert int(variables['south_east_share']) == 32
        assert int(variables['north_east_share']) == 9
        
    