# task Human
class Human:
    default_name = 'Victor'
    default_age = 25

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'age: {self.age}')
        print(f'name: {self.name}')
        print(f'money: {self.__money}')
        print(f'house: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def make_deal(self, house, price):
        self.__house = house
        self.__money -= price

    def earn_money(self, value):
        self.__money += value
        print(f'Earned money, current value: {self.__money}')

    def buy_house(self, house, sale):
        price = house.final_price(sale)
        if self.__money >= price:
            self.make_deal(house, price)
        else:
            print('Not money!')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        return self._price - (self._price / 100 * sale)


class SmallHouse(House):
    def_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.def_area, price)


def main():
    human = Human()
    human.info()
    Human.default_info()
    human.earn_money(1000)
    sh = SmallHouse(500)
    human.buy_house(sh, 1)
    human.earn_money(1222)
    human.buy_house(sh, 50)
    human.info()



if __name__ == '__main__':
    main()
