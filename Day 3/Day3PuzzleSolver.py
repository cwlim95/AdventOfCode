class Day3PuzzleSolver(object):
    def __init__(self):
        with open('day3puzzleinput.txt', 'r') as f:
            self.PUZZLE_INPUT = [line.strip().split('  ') for line in f.readlines()]
            for i in range(len(self.PUZZLE_INPUT)):
                self.PUZZLE_INPUT[i] = filter(None, self.PUZZLE_INPUT[i])

    def validate_triangle(self, triangle_sides):
        triangle_sides = map(int, triangle_sides)
        min1 = triangle_sides.pop(triangle_sides.index(min(triangle_sides)))
        min2 = triangle_sides.pop(triangle_sides.index(min(triangle_sides)))
        if min1 + min2 <= triangle_sides[0]:
            return False

        return True


if __name__ == '__main__':
    puzzleSolver = Day3PuzzleSolver()
    correct_triangle = 0

    for triangle in puzzleSolver.PUZZLE_INPUT:
        if puzzleSolver.validate_triangle(triangle) is True:
            print triangle
            correct_triangle += 1
    print correct_triangle
