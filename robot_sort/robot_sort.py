class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # initial pickup
        print(f"START: Item is {self._item}, Pos = {self._position}, List = {self._list}")
        self.swap_item()
        print(f"INIT: Item is {self._item}, Pos = {self._position}, List = {self._list}")
        # Have the robot turn on light to indicate it needed to swap an item
        self.set_light_on()

        while self.light_is_on():
            # reset boolean (light)
            self.set_light_off()

            while self.can_move_right():
                self.move_right()
                if self.compare_item() == -1:
                    # Found larger number while moving right. Swap items
                    print(f"(R) Pre-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
                    self.swap_item()
                    print(f"(R) Post-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
                    # Since an item was swapped, turn light on
                    self.set_light_on()

            # After debugging, I see that the robot should now have the highest possible number at this point and is at the end of the list, force a swap here
            if self.compare_item() == 1:
                print(f"(R) Pre-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
                self.swap_item()
                print(f"(R) Post-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
                self.set_light_on()

            while self.can_move_left():
                self.move_left()
                if self.compare_item() == 1:
                    # Found smaller number while moving left. Swap items
                    print(f"(L) Pre-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
                    self.swap_item()
                    print(f"(L) Post-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
                    # Since an item was swapped, turn light on
                    self.set_light_on()

            # Should be back to where the robot first dropped off the None, force a swap here
            print(f"Pre-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
            self.swap_item()
            print(f"Post-Swap: {self._item}, Pos = {self._position}, List = {self._list}")
            self.set_light_off()
            # I'm finding the above 3 lines of code runs twice back-to-back
            # After assessing code, I can only conclude that main while-loop arrives here, performs swap, the light was on, runs through loop again never swapping right or left again
            # and gets back here and performs final swap again. Need a way to limit this to run only once.
            # That's easy, turn the light off. Can't believe it took me a few minutes to figure that one out.


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    short_l = [3, 13, 7, 25, 32, 21, 38, 18, 12, 5]
    # to the right: [None, 3, 7, 13, 25, 21, 32, 18, 12, 5], 38 in hand
    # to the left: [None, 5, 7, 13, 25, 21, 32, 18, 12, 38], 3 in hand
    # to the right: [], I think I realized I may be missing something in my logic here. Gonna use prints to check sort method
    # sorted: [3, 5, 7, 12, 13, 18, 21, 25, 32, 38]
    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(short_l)

    robot.sort()
    print(robot._list)