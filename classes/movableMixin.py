from classes.robot import Robot


class MovableMixin(Robot):

    def __init__(self, name):
        super().__init__(name)
        self.move = [0, 0]


    def move_command(self, to_where):
        self.move = to_where
        return to_where