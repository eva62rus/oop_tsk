class TriangleCheacker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted(self.sides)
                if self.sides[0] + self.sides[1] > self.sides[2]:
                    return 'Is triangle'
                return 'Its not triangle'
            return 'Negative values'
        return 'Input are not values'


def main():
    t = TriangleCheacker([2, 3, 4])
    print(t.is_triangle())


if __name__ == '__main__':
    main()