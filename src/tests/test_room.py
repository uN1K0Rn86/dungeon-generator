import unittest
from unittest.mock import patch
from room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(7, 7)

    def test_room_size_within_limits(self):
        self.assertGreaterEqual(self.room.width, 2)
        self.assertGreaterEqual(self.room.height, 2)
        self.assertLessEqual(self.room.width, 7)
        self.assertLessEqual(self.room.height, 7)

    @patch("room.randint", side_effect=[6, 7])
    def test_visual_output(self, mock_randint):
        room = Room(10, 10)

        self.assertEqual(str(room), """......
......
......
......
......
......
......
""")
