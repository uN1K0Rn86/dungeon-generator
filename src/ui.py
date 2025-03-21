import sys
from dungeon import Dungeon

class Ui:
    """
    Class for implementing the user interface.
    """

    def run(self):
        """
        The method used to start the dungeon generator.
        """

        print("Welcome to the Dungeon Generator")
        self.menu()

    def menu(self):
        """
        Prints the main menu and calls other methods based on user input.
        """

        print("Choose from the following:")
        print("1: Generate Dungeon")
        print("2: Legend")
        print("3: Exit")
        command = input("Command: ")
        print("\n")

        if command == "1":
            self.dungeon_generator()
        elif command == "2":
            self.legend()
        elif command == "3":
            self.quit()

    def validate_input(self, prompt):
        """
        Validates user input
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

            rooms_amount = self.validate_input("Amount of rooms:")
            if rooms_amount == 0:
                break

            if width - room_maxwidth < 2:
                print("Please choose a wider dungeon or narrower room size")
                continue
            if height - room_maxheight < 2:
                print("Please choose a taller dungeon or lower room size")
                continue

            dungeon = Dungeon(width, height, room_maxwidth, room_maxheight, rooms_amount)
            dungeon.place_rooms()

            if len(dungeon.rooms) < rooms_amount:
                print("Could not fit all rooms into the dungeon.")

            print(dungeon)

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

        print("Thank You!")
        sys.exit()
