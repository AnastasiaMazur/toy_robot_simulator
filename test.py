from unittest import TestCase

from run import parse_command
from commands import PlaceCommand, COMMANDS_MAP


class TestToyRobot(TestCase):
    TEST_CASES = [
        {
            "commands": ["MOVE", "REPORT"],
            "expected_result": "0,1,NORTH"
        },
        {
            "commands": ["PLACE 1,2,EAST", "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"],
            "expected_result": "3,3,NORTH"
        },
        {
            "commands": ["PLACE 0,0,NORTH", "LEFT", "MOVE", "MOVE", "MOVE", "RIGHT", "MOVE", "REPORT"],
            "expected_result": "0,1,NORTH"
        }
    ]

    def test_cases(self) -> None:
        for case in self.TEST_CASES:
            robot_toy = PlaceCommand().__call__()
            for command in case["commands"]:
                if "PLACE" in command:
                    command_name, args = parse_command(command)
                    robot_toy = PlaceCommand(*args).__call__()
                elif command == "REPORT":
                    self.assertEqual(robot_toy.make_report(), case["expected_result"])
                else:
                    run_command = COMMANDS_MAP[command]()
                    run_command(robot_toy)
