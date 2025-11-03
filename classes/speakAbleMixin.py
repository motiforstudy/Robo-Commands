from classes.robot import Robot

class SpeakableMixin(Robot):

    def __init__(self, name):
        super().__init__(name)
        self.talk = ""


    def talk_command(self, talk):
        self.talk = talk
        print(self.talk)