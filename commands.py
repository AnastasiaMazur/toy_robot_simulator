import sys
from robot import Robot


class BaseCommand:
    def __init__(self, *args):
        self.params = list(args)


class PlaceCommand(BaseCommand):
    def __call__(self, *args) -> Robot:
        return Robot(*self.params)

class MoveCommand(BaseCommand):
    def __call__(self, robot_instance:Robot, *args) -> None:
        robot_instance.move_robot()

class LeftCommand(BaseCommand):
    def __call__(self, robot_instance:Robot, *args) -> None:
        robot_instance.turn_left()

class RightCommand(BaseCommand):
    def __call__(self, robot_instance:Robot, *args) -> None:
        robot_instance.turn_right()

class ReportCommand(BaseCommand):
    def __call__(self, robot_instance:Robot, *args) -> None:
        sys.exit(robot_instance.make_report())


COMMANDS_MAP = {
    "PLACE": PlaceCommand,
    "MOVE": MoveCommand,
    "LEFT":LeftCommand,
    "RIGHT": RightCommand,
    "REPORT": ReportCommand
}
