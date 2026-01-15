# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
# значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Rhomb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більше 0")

        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут A повинен бути в межах 0–180 градусів")

            object.__setattr__(self, "angle_b", 180 - value)

        object.__setattr__(self, name, value)

rhomb = Rhomb(20, 80)

print("Сторона a:", rhomb.side_a)
print("Кут A:", rhomb.angle_a)
print("Кут B:", rhomb.angle_b)