import sys
from dungeon import Dungeon

class Ui:
    """
    Class for implementing the user interface.
    """

    def __init__(self):
        """
        Constructor that initializes a list of created dungeons.
        """
        self.dungeons = []

    def run(self):
        """
        The method used to start the dungeon generator.
        """

        print("*** Welcome to the Dungeon Generator ***\n")
        self.menu()

    def menu(self):
        """
        Prints the main menu and calls other methods based on user input.
        """

        print("*** Choose from the following: ***")
        print("1: Generate Dungeon")
        print("2: Legend")
        print("3: View Dungeons")
        print("4: Exit\n")
        command = input("Command: ")
        print("\n")

        if command == "1":
            self.dungeon_generator()
        elif command == "2":
            self.legend()
        elif command == "3":
            self.view_dungeon()
        elif command == "4":
            self.quit()

    def validate_input(self, prompt: str) -> int:
        """
        Validates user input

        Args:
            prompt (text): User in put to be validated.
        Returns:
            value (integer): The input converted to an integer, assuming that is possible. 
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Please enter a valid integer.")

    def dungeon_generator(self):
        """
        Asks for user specifications for the dungeon and prints out the resulting dungeon.
        """

        while True:
            print("Return to main menu with the command '0'")
            print("All measurements are in tiles")
            print("Dungeon width and height should be at least 2 tiles more than the maximum width and height of a room")
            print("\n")

            width = self.validate_input("Dungeon width: ")
            if width == 0:
                break

            height = self.validate_input("Dungeon height: ")
            if height == 0:
                break


            room_maxwidth = self.validate_input("Maximum width for rooms: ")
            if room_maxwidth == 0:
                break

            room_maxheight = self.validate_input("Maximum height for rooms: ")
            if room_maxheight == 0:
                break

            rooms_amount = self.validate_input("Amount of rooms: ")
            if rooms_amount == 0:
                break

            chance = self.validate_input("Chance to include additional hallways (percentage, 5 suggested) : ")

            name = input("Name: ")

            print("\n")

            if width - room_maxwidth < 2:
                print("Please choose a wider dungeon or narrower room size")
                continue
            if height - room_maxheight < 2:
                print("Please choose a taller dungeon or lower room size")
                continue

            demo = bool(input("Would you like a step-by-step demonstration of how the dungeon is built? (y/n): ") == "y")

            print("\n")

            dungeon = Dungeon(width, height, room_maxwidth, room_maxheight, rooms_amount, name, demo)
            dungeon.place_rooms()
            self.dungeons.append(dungeon)

            if len(dungeon.rooms) < rooms_amount:
                print("Could not fit all rooms into the dungeon.")

            plot = input("Would you like a graphical plot of the dungeon with a Delaunay triangulation? (y/n): ")
            if plot == "y":
                dungeon.display("delaunay")

            print("\n")

            dungeon.prim(chance)
            dungeon.a_star()

            ascii_print = input("Would you like an ascii printout of the dungeon? (y/n): ")
            if ascii_print == "y":
                print(dungeon)

            print("\n")

            prim = input("Would you like to see the paths found by Prim's algorithm? (y/n): ")
            if prim == "y":
                dungeon.display("prim")

            print("\n")

            print("Here is the dungeon in its final form: \n")
            dungeon.display()

        self.menu()

    def view_dungeon(self):
        """
        View a previously generated dungeon based on its name.
        """

        if len(self.dungeons) == 0:
            print("No dungeons to view. Please create a dungeon first.\n")
            self.menu()
        else:
            print("Created dungeons:")
            for dungeon in self.dungeons:
                print(dungeon.name)

        while True:
            print("Return to main menu with the command '0'")
            print("\n")

            name = input("Dungeon name: ")
            names = {dungeon.name: i for i, dungeon in enumerate(self.dungeons)}

            if name == "0":
                break

            if name in names:
                dungeon = self.dungeons[names[name]]
                view = input("What type of view would you like? (ascii (a) / Delaunay Triangulation (d) / MST (MST) / Final (f): ")
                if view == "a":
                    print(dungeon)
                elif view == "d":
                    dungeon.display("delaunay")
                elif view == "MST":
                    dungeon.display("prim")
                elif view == "f":
                    dungeon.display()
                else:
                    print("Invalid command. Please try again")
            else:
                print("Could not find a dungeon by that name")
        self.menu()

    def legend(self):
        """
        Prints explanations for dungeon tiles.
        """

        print("Each tile in the dungeon represents either a wall or a floor.")
        print("# - Wall")
        print(". - Floor")
        print("\n")

        self.menu()

    def quit(self):
        """
        Exits the program.
        """

        print("*** Thank You! ***")
        sys.exit()
