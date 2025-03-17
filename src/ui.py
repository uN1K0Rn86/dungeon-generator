import sys
from room_generator import place_rooms
from visual_output import output

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

    def dungeon_generator(self):
        """
        Asks for user specifications for the dungeon and prints out the resulting dungeon.
        """

        while True:
            print("Return to main menu with the command '0'")
            print("All measurements are in tiles")
            print("Dungeon width and height should be at least 2 tiles more than the maximum width and height of a room")
            print("\n")

            width = int(input("Dungeon width: "))
            if width == 0:
                break

            height = int(input("Dungeon height: "))
            if height == 0:
                break

            room_maxwidth = int(input("Maximum width for rooms: "))
            if room_maxwidth == 0:
                break

            room_maxheight = int(input("Maximum height for rooms: "))
            if room_maxheight == 0:
                break

            amount = int(input("Amount of rooms:"))
            if amount == 0:
                break

            if width - room_maxwidth < 2:
                print("Please choose a wider dungeon or narrower room size")
                continue
            if height - room_maxheight < 2:
                print("Please choose a taller dungeon or lower room size")
                continue

            dungeon, tries = place_rooms(width, height, room_maxwidth, room_maxheight, amount)

            if tries == 0:
                print("Could not fit all the rooms into the dungeon. Please choose a bigger dungeon or less rooms")
                print("\n")

            print(output(dungeon))

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