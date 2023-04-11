class Soda:
    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):
        if self.additive is not None:
            print(f'Газировка и {self.additive}')
        else:
            print('Обычная газировка')


def main():
    soda = Soda('Малина')
    soda.show_my_drink()


if __name__ == '__main__':
    main()
