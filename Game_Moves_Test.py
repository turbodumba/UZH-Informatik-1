#!/usr/bin/env python3
from unittest import TestCase
from Game_Moves import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_up(self):
        # NOTE: this test case is buggy and needs fixing!
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        self.assertEqual(expected, actual)

    def test_wrong_char(self):
        state = (
            "###  ##",
            "#  ##  ",
            "## _   ",
            "  o    "
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_wrong_length(self):
        state = (
            "####",
            "o  #",
            " ###",
            "### #"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_wrong_player(self):
        state = (
            "# o #",
            "     ",
            "o####",
            " ####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_wrong_size_one(self):
        state = (
            "###",
            "",
            "  o"
            "   "
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_wrong_size_two(self):
        state = (

        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_no_move(self):
        state = (
            "# #",
            " # ",
            "#o#",
            " # ",
            "# #"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_move_up_not_possible(self):
        state = (
            "###",
            "#o#",
            "   "
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_down_edge(self):
        state = (
            "###    ",
            "###   #",
            "##   ##",
            "#   o##"
        )
        actual = move(state, "left")
        expected = (
            (
                "###    ",
                "###   #",
                "##   ##",
                "#  o ##"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(actual, expected)

    def test_left_edge(self):
        state = (
            "###",
            "o #",
            "  #"
        )
        actual = move(state, "down")
        expected = (
            (
                "###",
                "  #",
                "o #"
            ),
            ("right", "up")
        )
        self.assertEqual(actual, expected)

    def test_right_edge(self):
        state = (
            "   ",
            "# o",
            "###"
        )
        actual = move(state, "up")
        expected = (
            (
                "  o",
                "#  ",
                "###"
            ),
            ("down", "left")
        )
        self.assertEqual(actual, expected)

    def test_up_edge(self):
        state = (
            "#o ",
            "   ",
            "###"
        )
        actual = move(state, "right")
        expected = (
            (
                "# o",
                "   ",
                "###"
            ),
            ("down", "left")
        )
        self.assertEqual(actual, expected)

    def test_emptyness(self):
        state = (
            ""
            ""
            ""
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_emptystring(self):
        state = (
            ""
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_random(self):
        state = (
            "  #",
            " o ",
            "# #"
        )
        actual = move(state, "up")
        expected = (
            (
                " o#",
                "   ",
                "# #"
            ),
            ("down", "left")
        )
        self.assertEqual(actual, expected)

    def test_empty_world(self):
        state = (
            "   ",
            "   ",
            "   "
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_no_player(self):
        state = (
            "#####",
            "     ",
            "     ",
            "##  #",
            "#   #",
            "#    ",
            "     "
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_empty_world_two(self):
        state = (
            " ",
            " ",
            " "
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_empty_world_three(self):
        state = (
            "",
            " ",
            ""
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_empty_world_four(self):
        state = (
            "",

        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_empty_world_five(self):
        state = (
            "\n ",
            "  #",
            "#o ",
            "###"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_empty_world_six(self):
        state = (
            "",
            "",
            "",
            ""
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_empty_world_poss(self):
        state = (
            "     ",
            "     ",
            "  o  ",
            "     ",
            "     "
        )
        expected = ((
                        "     ",
                        "     ",
                        " o   ",
                        "     ",
                        "     "
                    ),
                    (
                        'down', 'left', 'right', 'up'
                    ))
        actual = move(state, "left")
        self.assertEqual(expected, actual)

    def test_wrong_dir(self):
        state = (
            "####",
            "o ##",
            " ###"
        )
        with self.assertRaises(Warning):
            move(state, 2)

    def test_three_players(self):
        state = (
            "# o   #",
            "##   o ",
            "##     ",
            "###   #",
            "o  ####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_move_down_not_possible(self):
        state = (
            "# #",
            " o ",
            "###"
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_move_left_not_possible(self):
        state = (
            "# #",
            "#o ",
            "# #"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_move_right_not_possible(self):
        state = (
            "# #",
            " o#",
            "   "
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_one_row(self):
        state = (
            "#####  o######",
        )
        expected = (
            (
                "##### o ######",
            ),
            ("left", "right")
        )
        actual = move(state, "left")
        self.assertEqual(expected, actual)

    def test_one_column(self):
        state = (
            "#",
            "#",
            " ",
            "o",
            " ",
            " ",
            "#"
        )
        expected = (
            (
            "#",
            "#",
            " ",
            " ",
            "o",
            " ",
            "#"
            ),
            ("down", "up")
        )
        actual = move(state, "down")
        self.assertEqual(expected, actual)

    def test_dir_caps(self):
        state = (
            "##",
            "o ",
            "  "
        )
        with self.assertRaises(Warning):
            move(state, "Down")

    def test_one_row_wrong(self):
        state = (
            "#####  o######"
        )
        with self.assertRaises(Warning):
            move(state, "right")

    def test_one_column_wrong(self):
        state = (
            "#",
            "#",
            "#",
            "o",
            " ",
            " ",
            "#"
        )
        with self.assertRaises(Warning):
            move(state, "up")