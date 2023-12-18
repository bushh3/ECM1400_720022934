import pytest
from tests import test_helper_functions as thf
from battleships_game.components import *

testReport = thf.TestReport("test_functionality_report.txt")
########################################################################################################################
# Test Components.py functions
########################################################################################################################
def test_initialise_board_return_size():
    """
    Test if the initialise_board function returns a list of the correct size.
    """
    size = 10
    # Run the function
    board = initialise_board(size)
    # Check that the return is a list
    try:
        assert isinstance(board, list), "initialise_board function does not return a list"
        # check that the length of the list is the same as board
        assert len(board) == size, "initialise_board function does not return a list of the correct size"
        for row in board:
            # Check that each sub element is a list
            assert isinstance(row, list), "initialise_board function does not return a list of lists"
            # Check that each sub list is the same size as board
            assert len(row) == size, "initialise_board function does not return lists of the correct size"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_initialise_board_boundary_data():
    """
    Test if the initialise_board function can handle certain boundary data points.
    """
    size_1 = 1000
    size_2 = 1
    sizes = [size_1, size_2]
    for size in sizes:
        # Run the function
        board = initialise_board(size)
        try:
            # Check that the return is a list
            assert isinstance(board, list), "initialise_board function does not return a list"
            # check that the length of the list is the same as board
            assert len(board) == size, "initialise_board function does not return a list of the correct size"
            for row in board:
                # Check that each sub element is a list
                assert isinstance(row, list), "initialise_board function does not return a list of lists"
                # Check that each sub list is the same size as board
                assert len(row) == size, "initialise_board function does not return lists of the correct size"
        except AssertionError as message:
            testReport.add_message(str(message))
            pytest.fail(str(message))
def test_initialise_board_erroneous_data():
    """
    Test if the initialise_board function can handle certain erroneous data points.
    """
    size_1 = 'ten'
    size_2 = 0.2
    size_3 = 'r'
    sizes = [size_1, size_2, size_3]
    for size in sizes:
        # Run the function
        try:
            board = initialise_board(size)
            # Check that the return is a list
            assert isinstance(board, list), "initialise_board function does not return a list"
            # check that the length of the list is 1
            assert board == [[]], "initialise_board function does not return an empty list of lists"
        except AssertionError as message:
            testReport.add_message(str(message))
            pytest.fail(str(message))
def test_create_battleships_return_values():
    """
    Test if the create_battleships function returns the right information given standard data.
    """
    filename = "battleships.txt"
    # run the function
    battleships = create_battleships(filename)
    try:
        # check that the return is a dictionary
        assert isinstance(battleships, dict), "create_battleships function does not return a dictionary"
        # check that the length of the dictionary is of size 5
        assert len(battleships) == 5, "create_battleships function does not return a dictionary of the correct size"
        # check the names and sizes of the ships are all correct and present
        assert "Aircraft_Carrier" in battleships, "create_battleships function does not return the correct names of ships"
        assert battleships["Aircraft_Carrier"] == 5, "create_battleships function does not return the correct sizes of ships"
        assert "Battleship" in battleships, "create_battleships function does not return the correct names of ships"
        assert battleships["Battleship"] == 4, "create_battleships function does not return the correct sizes of ships"
        assert "Cruiser" in battleships, "create_battleships function does not return the correct names of ships"
        assert battleships["Cruiser"] == 3, "create_battleships function does not return the correct sizes of ships"
        assert "Submarine" in battleships, "create_battleships function does not return the correct names of ships"
        assert battleships["Submarine"] == 3, "create_battleships function does not return the correct sizes of ships"
        assert "Destroyer" in battleships, "create_battleships function does not return the correct names of ships"
        assert battleships["Destroyer"] == 2, "create_battleships function does not return the correct sizes of ships"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_create_battleships_boundary_data():
    """
    Test if the create_battleships function can handle certain boundary data points.
    """
    filename = "empty.txt"
    with open(filename, 'w') as _:
        # create an empty file
        pass
    ships = create_battleships(filename)
    try:
        assert isinstance(ships, dict), "create_battleships function does not return a dictionary"
        assert len(ships) == 0, "create_battleships function does not return a dictionary as empty"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_create_battleships_erroneous_data():
    """
    Test if the create_battleships function can handle certain erroneous data points.
    """
    filename = "erroneous_ships.txt"
    with open(filename, 'w') as ship_file:
        ship_file.write("Destroyer:a\nCruiser:not a size")
    ships = create_battleships(filename)
    try:
        assert isinstance(ships, dict), "create_battleships function does not return a dictionary"
        assert len(ships) == 0, "create_battleships function does not return a dictionary as empty"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_place_return_values():
    """
    Test if the place function can handle normal data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    place(board, 'Ship', 3, (2, 3), 'h')
    try:
        assert isinstance(board, list), "place function does not return a list"
        assert len(board) == size, "place function does not return a list of the correct size"
        for row in board:
            assert isinstance(row, list), "place function does not return a list of lists"
            assert len(row) == size, "place function does not return lists of the correct size"
        print(board)
        assert board == [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None,'Ship', 'Ship', 'Ship', None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]
        ], "place does not return the ships in the correct places"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_place_boundary_data():
    """
    Test if the place function can handle certain boundary data points.
    """
    size = 1
    board = [[None] * size for row in range(size)]
    place(board, 'Ship', 1, (0, 0), 'h')
    try:
        assert isinstance(board, list), "place function does not return a list"
        assert len(board) == size, "place function does not return a list of the correct size"
        for row in board:
            assert isinstance(row, list), "place function does not return a list of lists"
            assert len(row) == size, "place function does not return lists of the correct size"
        assert board == [['Ship']], "place does not return the ships in the correct places"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))

'''
def test_place_battleships_return_values():
    """
    Test if the place_battleships function can handle certain normal data points.
    """
    
def test_place_battleships_boundary_data():
    """
    Test if the place_battleships function can handle certain boundary data points.
    """
def test_place_battleships_erroneous_data():
    """
    Test if the place_battleships function can handle certain erroneous data points.
    """
'''
def test_can_place_return_values():
    """
    Test if the can_place function can handle certain normal data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    result = can_place(board, 3, 5, 4, 'v')
    try:
        assert result is True, "can_place function cannot place a ship"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_can_place_boundary_data():
    """
    Test if the can_place function can handle certain boundary data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    result = can_place(board, 1, 9, 9, 'h')
    try:
        assert result is True, "can_place function cannot place the ship on an edge"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
    size = 1
    board = [[None] * size for row in range(size)]
    result = can_place(board, 1, 0, 0, 'h')
    try:
        assert result is True, "can_place function cannot place the ship on a small board"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))
def test_can_place_erroneous_data():
    """
    Test if the can_place function can handle certain erroneous data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    # add a ship
    for i in range(2, 5):
        board[3][i] = 'Ship'
    result = can_place(board, 3, 2, 3, 'h')
    try:
        assert result is False, "can_place function places a ship over another"
    except AssertionError as message:
        testReport.add_message(str(message))
        pytest.fail(str(message))