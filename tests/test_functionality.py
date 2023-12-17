import importlib
import inspect

import pytest
import components as comp

def test_initialise_board_return_size():
    """
    Test if the initialise_board function returns a list of the correct size.
    """
    size = 10
    # Run the function
    board = comp.initialise_board(size)
    # Check that the return is a list
    assert isinstance(board, list), "initialise_board function does not return a list"
    # check that the length of the list is the same as board
    assert len(board) == size, "initialise_board function does not return a list of the correct size"
    for row in board:
        # Check that each sub element is a list
        assert isinstance(row, list), "initialise_board function does not return a list of lists"
        # Check that each sub list is the same size as board
        assert len(row) == size, "initialise_board function does not return lists of the correct size"
def test_initialise_board_boundary_data():
    """
    Test if the initialise_board function can handle certain boundary data points.
    """
    size_1 = 10000000000000
    size_2 = 1
    sizes = [size_1, size_2]
    for size in sizes:
        # Run the function
        board = comp.initialise_board(size)
        # Check that the return is a list
        assert isinstance(board, list), "initialise_board function does not return a list"
        # check that the length of the list is the same as board
        assert len(board) == size, "initialise_board function does not return a list of the correct size"
        for row in board:
            # Check that each sub element is a list
            assert isinstance(row, list), "initialise_board function does not return a list of lists"
            # Check that each sub list is the same size as board
            assert len(row) == size, "initialise_board function does not return lists of the correct size"
def test_initialise_board_erroneous_data():
    """
    Test if the initialise_board function can handle certain erroneous data points.
    """
    size_1 = 'ten'
    size_2 = 0.2
    size_3 = 'r'
    size_4 = -10
    sizes = [size_1, size_2, size_3, size_4]
    for size in sizes:
        # Run the function
        board = comp.initialise_board(size)
        # Check that the return is a list
        assert isinstance(board, list), "initialise_board function does not return a list"
        # check that the length of the list is the same as the default
        assert len(board) == 10, "initialise_board function does not return a list of the correct size"
        for row in board:
            # Check that each sub element is a list
            assert isinstance(row, list), "initialise_board function does not return a list of lists"
            # Check that each sub list is the same size as the default
            assert len(row) == 10, "initialise_board function does not return lists of the correct size"
def test_create_battleships_return_values():
    """
    Test if the create_battleships function returns the right information given standard data.
    """
    filename = "battleships.txt"
    # run the function
    ships = create_battleships(filename)
    # check that the return is a dictionary
    assert isinstance(filename, dict), "create_battleships function does not return a dictionary"
    # check that the length of the dictionary is of size 5
    assert len(ships) == 5, "create_battleships function does not return a dictionary of the correct size"
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
def test_create_battleships_boundary_data():
    """
    Test if the create_battleships function can handle certain boundary data points.
    """
    filename = "empty.txt"
    with open(filename, 'w') as _:
        # create an empty file
        pass
    ships = create_battleships(filename)
    assert isinstance(ships, dict), "create_battleships function does not return a dictionary"
    assert len(ships) == 0, "create_battleships function does not return a dictionary as empty"
def test_create_battleships_erroneous_data():
    """
    Test if the create_battleships function can handle certain erroneous data points.
    """
    filename = "erroneous_ships.txt"
    with open(filename, 'w') as ship_file:
        ship_file.write("Destroyer:a\nCruiser:not a size")
    ships = create_battleships(filename)
    assert isinstance(ships, dict), "create_battleships function does not return a dictionary"
    assert len(ships) == 0, "create_battleships function does not return a dictionary as empty"
def test_place_return_values():
    """
    Test if the place function can handle normal data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    place(board, 'Ship', 3, (2, 3), 'h')
    assert isinstance(board, list), "place function does not return a list"
    assert len(board) == size, "place function does not return a list of the correct size"
    for row in board:
        assert isinstance(row, list), "place function does not return a list of lists"
        assert len(row) == size, "place function does not return lists of the correct size"
    assert board == [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, 'Ship', 'Ship', 'Ship', None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None]
    ], "place does not return the ships in the correct places"
def test_place_boundary_data():
    """
    Test if the place function can handle certain boundary data points.
    """
    size = 1
    board = [[None] * size for row in range(size)]
    place(board, 'Ship', 1, (0, 0), 'h')
    assert isinstance(board, list), "place function does not return a list"
    assert len(board) == size, "place function does not return a list of the correct size"
    for row in board:
        assert isinstance(row, list), "place function does not return a list of lists"
        assert len(row) == size, "place function does not return lists of the correct size"
    assert board == [['Ship']], "place does not return the ships in the correct places"
def test_place_erroneous_data():
    """
    Test if the place function can handle certain erroneous data points.
    """
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
def test_can_place_return_values():
    """
    Test if the can_place function can handle certain normal data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    result = can_place(board, 3, 5, 4, 'v')
    assert result is True, "can_place function cannot place a ship"
def test_can_place_boundary_data():
    """
    Test if the can_place function can handle certain boundary data points.
    """
    size = 10
    board = [[None] * size for row in range(size)]
    result = can_place(board, 1, 9, 9, 'h')
    assert result is True, "can_place function cannot place the ship on an edge"
    size = 1
    board = [[None] * size for row in range(size)]
    result = can_place(board, 1, 0, 0, 'h')
    assert result is True, "can_place function cannot place the ship on a small board"
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
    assert result is False, "can_place function places a ship over another"