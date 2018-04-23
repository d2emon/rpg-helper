"""
Testing GUI
"""

import mock
import pytest
import gui
import gui.menu


def test_ask_chars_count_int():
    with mock.patch('builtins.input', return_value='0'):
        assert isinstance(gui.askCharsCount(), int)


def test_ask_chars_count_text():
    with mock.patch('builtins.input', return_value='text input'):
        with pytest.raises(ValueError) as excinfo:
            gui.askCharsCount()


def test_ask_hours():
    with mock.patch('builtins.input', return_value='text input'):
        assert isinstance(gui.askHours(), int)


def test_ask_yn():
    with mock.patch('builtins.input', return_value="y\n"):
        assert isinstance(gui.askYN(), int)
        # gui.bye()
        # assert isinstance(gui.askRollMethod(), int)


def test_ask_roll_method():
    with mock.patch('builtins.input', return_value='text input'):
        gui.bye()
        assert isinstance(gui.askRollMethod(), int)


def test_bye():
    with pytest.raises(SystemExit) as excinfo:
        gui.bye()
    assert excinfo.value.code == 0


def test_ask_help_message():
    with pytest.raises(SystemExit) as excinfo:
        assert isinstance(gui.helpMessage(), int)


def test_menu():
    with mock.patch('builtins.input', return_value='1'):
        with pytest.raises(SystemExit) as excinfo:
            assert isinstance(gui.menu.showMenu("title", [{"title": 1, }, {"a": "b", }, 2, 3, ], gui.bye), int)
