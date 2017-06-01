class Day1PuzzleSolver(object):
    def __init__(self):
        # Read the input of the puzzle from a text file
        with open('day1puzzleinput.txt', 'r') as f:
            self.PUZZLE_INPUT = f.readline().replace(' ', '').split(',')

        self.current_direction = 'N'
        self.current_x = 0
        self.current_y = 0
        self.history_coords = []
        self.PART_1_ANS = None
        self.PART_2_ANS = None

    def turn_left(self):
        if self.current_direction == 'N':
            self.current_direction = 'W'
        elif self.current_direction == 'W':
            self.current_direction = 'S'
        elif self.current_direction == 'S':
            self.current_direction = 'E'
        elif self.current_direction == 'E':
            self.current_direction = 'N'

    def turn_right(self):
        if self.current_direction == 'N':
            self.current_direction = 'E'
        elif self.current_direction == 'E':
            self.current_direction = 'S'
        elif self.current_direction == 'S':
            self.current_direction = 'W'
        elif self.current_direction == 'W':
            self.current_direction = 'N'

    def move_forward(self, dir, x, y, steps):
        if dir == 'N':
            y += steps
        elif dir == 'E':
            x += steps
        elif dir == 'S':
            y -= steps
        elif dir == 'W':
            x -= steps

        return x, y

    def solve(self):
        historys = []
        for i in range(len(self.PUZZLE_INPUT)):
            if self.PUZZLE_INPUT[i][0] == 'L':
                self.turn_left()
            else:
                self.turn_right()

            for j in range(int(self.PUZZLE_INPUT[i][1:])):
                self.current_x, self.current_y = self.move_forward(self.current_direction, self.current_x,
                                                                   self.current_y, 1)

                if (self.current_x, self.current_y) in historys and self.PART_2_ANS is None:
                    self.PART_2_ANS = abs(self.current_x) + abs(self.current_y)
                else:
                    historys.append((self.current_x, self.current_y))

        self.PART_1_ANS = abs(self.current_x) + abs(self.current_y)


if __name__ == '__main__':
    puzzleSolver = Day1PuzzleSolver()
    puzzleSolver.solve()
    print puzzleSolver.PART_1_ANS
    print puzzleSolver.PART_2_ANS
