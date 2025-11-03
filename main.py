from classes.guardRobot import GuardRobot
from classes.deliveryRobot import DeliveryRobot


dora = DeliveryRobot("dora")
gideon = GuardRobot("gideon")
commands = ["SAY", "MOVE", "WHERE", "EXIT"]
user_command = input("please make a command: ")
while user_command != "EXIT":
    if user_command in commands:
        user_command_detail = input(f"please write what / where {user_command}: ")
        dora
        gideon

    user_command = input("please make a command: ")