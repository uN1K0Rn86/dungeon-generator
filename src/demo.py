from dungeon import Dungeon

p = [(2.0, 5.0), (3.5, 9.5), (5.5, 16.0), (21.5, 18.5), (20.0, 4.0), (21.5, 14.0), (10.0, 5.0)]
dungeon = Dungeon(25, 25, 5, 5, 7)
dungeon.place_rooms(demo=True)
print(dungeon)
print([(room.center_x, dungeon.height - room.center_y) for room in dungeon.rooms])
dungeon.d.display()
dungeon.display("delaunay")
