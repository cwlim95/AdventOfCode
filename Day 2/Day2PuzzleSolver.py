class Day2PuzzleSolver(object):
    def __init__(self):
        with open('day2puzzleinput.txt', 'r') as f:
            self.PUZZLE_INPUT = [line.strip() for line in f.readlines()]

        self.numpad_p1 = [[i + 1 + 3 * j for i in range(3)] for j in range(3)]
        self.current_location = [1, 1]
        self.part_1_sol = []
        self.part_2_sol = []

        self.numpad_p2 = [[0 for i in range(5)] for j in range(5)]
        self.numpad_p2[0][2] = 1
        self.numpad_p2[1][1] = 2
        self.numpad_p2[1][2] = 3
        self.numpad_p2[1][3] = 4
        self.numpad_p2[2][0] = 5
        self.numpad_p2[2][1] = 6
        self.numpad_p2[2][2] = 7
        self.numpad_p2[2][3] = 8
        self.numpad_p2[2][4] = 9
        self.numpad_p2[3][1] = 'A'
        self.numpad_p2[3][2] = 'B'
        self.numpad_p2[3][3] = 'C'
        self.numpad_p2[4][2] = 'D'

    def solve_p1(self):
        for line in self.PUZZLE_INPUT:
            for char in line:
                if char == 'U':
                    self.current_location[1] -= 1
                elif char == 'D':
                    self.current_location[1] += 1
                elif char == 'L':
                    self.current_location[0] -= 1
                elif char == 'R':
                    self.current_location[0] += 1

                if self.current_location[0] <= -1:
                    self.current_location[0] += 1

                if self.current_location[0] >= 3:
                    self.current_location[0] -= 1

                if self.current_location[1] <= -1:
                    self.current_location[1] += 1

                if self.current_location[1] >= 3:
                    self.current_location[1] -= 1
            self.part_1_sol.append(self.numpad_p1[self.current_location[1]][self.current_location[0]])

    def solve_p2(self):
        self.current_location = [0, 2]
        for line in self.PUZZLE_INPUT:
            for char in line:
                if char == 'U':
                    self.current_location[1] -= 1
                elif char == 'D':
                    self.current_location[1] += 1
                elif char == 'L':
                    self.current_location[0] -= 1
                elif char == 'R':
                    self.current_location[0] += 1

                if self.current_location[0] <= -1 or (char == 'L' and self.current_location in [[1, 0], [0, 1], [0, 3], [1, 4]]):
                    self.current_location[0] += 1

                elif self.current_location[0] >= 5 or (char == 'R' and self.current_location in [[3, 0], [4, 1], [4, 3], [3, 4]]):
                    self.current_location[0] -= 1

                elif self.current_location[1] <= -1 or (char == 'U' and self.current_location in [[0, 1], [1, 0], [3, 0], [4, 1]]):
                    self.current_location[1] += 1

                elif self.current_location[1] >= 5 or (char == 'D' and self.current_location in [[0, 3], [1, 4], [3, 4], [4, 3]]):
                    self.current_location[1] -= 1
            self.part_2_sol.append(self.numpad_p2[self.current_location[1]][self.current_location[0]])
if __name__ == '__main__':
    puzzleSolver = Day2PuzzleSolver()
    puzzleSolver.solve_p2()
    print puzzleSolver.part_2_sol
