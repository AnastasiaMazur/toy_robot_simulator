from position import Coordinates
from tabletop import TableTop


class Robot:
    FACING_NAMES_MAP = {
        (0, -1): "SOUTH",
        (-1, 0): "WEST",
        (0, 1): "NORTH",
        (1, 0): "EAST"
    }
    FACING_POSSIBILITIES = list(FACING_NAMES_MAP.keys())

    def __init__(self, position_x=0, position_y=0, facing='NORTH', tabletop=TableTop(Coordinates(0,0),Coordinates(4,4))):
        self.position = Coordinates(int(position_x), int(position_y))
        # setting default direction of 'NORTH'
        self.facing = self.find_direction(facing)
        self.tabletop = tabletop

    def find_direction(self, facing) -> tuple:
        try:
            facing = [key for key,value in self.FACING_NAMES_MAP.items() if value == facing]
        except KeyError:
            return self.FACING_POSSIBILITIES[2]
        else:
            return facing[0]

    def turn_left(self) -> None:
        facing = self.FACING_POSSIBILITIES[
            (self.FACING_POSSIBILITIES.index(self.facing) + len(self.FACING_POSSIBILITIES)-1) % len(self.FACING_POSSIBILITIES)]
        return self._put_robot(self.position, facing, self.tabletop)

    def turn_right(self) -> None:
        facing = self.FACING_POSSIBILITIES[
            (self.FACING_POSSIBILITIES.index(self.facing)+1) % len(self.FACING_POSSIBILITIES)]
        return self._put_robot(self.position, facing, self.tabletop)

    def move_robot(self) -> None:
        return self._put_robot(self.position + Coordinates(*self.facing), self.facing, self.tabletop)

    def _put_robot(self, position:Coordinates, facing, tabletop:TableTop) -> None:
        if tabletop.contains(position):
            self.position = position
        self.facing = facing
        self.tabletop = tabletop

    def make_report(self) -> str:
        return f'{self.position.x},{self.position.y},{self.FACING_NAMES_MAP.get(self.facing)}'
