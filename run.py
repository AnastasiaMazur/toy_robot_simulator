import sys
from typing import List, Tuple

from robot import Robot
from commands import COMMANDS_MAP


def parse_command(command_line) -> Tuple[str, List[str]]:
    command_line = command_line.split()

    if not len(command_line):
        raise ValueError

    command_name = command_line[0].upper()
    args = list(command_line[1:][0].replace(".", ",").upper().split(",")) if len(command_line) > 1 else []
    return command_name, args


def run_commands() -> None:
    toy_robot = None

    for line in sys.stdin:
        command_name, args = parse_command(line)
        if command_name in COMMANDS_MAP:
            run_command = COMMANDS_MAP[command_name](*args)
            if command_name == "PLACE":
                toy_robot = run_command()
            else:
                if not toy_robot:
                    toy_robot = Robot()
                run_command(toy_robot)
        else:
            raise ValueError()

if __name__ == '__main__':
    print("Running toy robot simulator...")
    run_commands()
