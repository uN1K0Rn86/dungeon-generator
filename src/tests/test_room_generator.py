import pytest
from room_generator import generate_room, place_rooms

class TestGenerateRoom:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.room = generate_room(7, 7)

    def test_room_size_within_limits(self):
        assert 2 <= self.room[0] <= 7
        assert 2 <= self.room[1] <= 7

class TestPlaceRooms:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dungeon, tries = place_rooms(40, 30, 8, 7, 9)

    def test_dungeon_size(self):
        assert len(self.dungeon) == 30
        assert len(self.dungeon[0]) == 40