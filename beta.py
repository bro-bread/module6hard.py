import math

class Figure:
    sides_count = 0
    def __init__(self,sides, color,filled = True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if r <= 255 and type(r) == int:
            if g <= 255 and type(g) == int:
                if b <= 255 and type(b):
                    pass
                else:
                    pass
            else:
                pass
        else:
            pass

    def set_color(self,r ,g ,b):
            if r <= 255 and type(r) == int:
                if g <= 255 and type(g) == int:
                    if b <= 255 and type(b) == int:
                        self.__color = [r,g,b]
                    else:
                        pass
                else:
                    pass
            else:
                pass

    def __is_valid_sides(self, *storona):
        storona_list_T = []
        storona_list = []
        for i in storona:
            if len(storona) == len(self.__sides):
                if type(i) == int and i > 0:
                    storona_list_T.append(True)
                else:
                    storona_list.append(False)

            else:
                storona_list.append(False)

        if any(storona_list_T):
            return True

        if any(storona_list):
            pass
        else:
            return False


    def  get_sides(self):
        print(*self.__sides)

    def  __len__(self):
        sum_list = sum(self.__sides)
        return sum_list

    def set_sides(self, *new_sides):
        ryr = list(self.__sides)
        sssp = []
        if len(new_sides) != Figure.sides_count:
            ryr.clear()
            for u in new_sides:
                sssp.append(u)
            rdr2 = tuple(sssp)
            self.__sides = ryr + sssp
            print(self.__sides,"🍺")
        else:
            pass


class  Circle(Figure):
    sides_count = 1
    def __radius(self):
        r = self.sides_count / (2 * 3.14)
        print(r)

    def  get_square(self):
        r = self.sides_count / (2 * 3.14)
        S = ((r**2)/(4*3.14))
        print(S)

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        if len(self._Figure__sides) == 3:
            r = sum(self._Figure__sides)
            p = r/2
            s = p*(p-self._Figure__sides[0])*(p-self._Figure__sides[1])*(p-self._Figure__sides[2])
            S = int(math.sqrt(s))

class Cube(Figure):
    sides_count = 12
    def __init__(self, *sides):
        super().__init__(*sides)
        if type(sides[0]) == list:
            rtp = sides[0]
            self.__sides = [rtp[0], rtp[0], rtp[0], rtp[0], rtp[0], rtp[0], rtp[0], rtp[0], rtp[0], rtp[0], rtp[0]]
            print(self.__sides,"🥵")
        if type(sides[0]) == int:
            rtt = sides[0]
            self.__sides = [rtt, rtt, rtt, rtt, rtt, rtt, rtt, rtt, rtt, rtt, rtt, rtt]
            print(self.__sides,"🥶")

    def  get_volume(self):
        v = self.__sides[0]**3
        print(v, "")

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube([222, 35, 130], [6, 2])

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



