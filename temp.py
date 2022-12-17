
class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
    # Переопределите метод describe().
    def describe(self, full):
 #       if full == False:
            return print(super().describe())
 #       return print(f'Попугай {self.name} - заметная птица, '
 #                   f'окрас её перьев - {self.color}, а размер - {self.size} '
 #                   f'Интересный факт: попугаи чувствуют ритм, '
 #                   f'а вовсе не бездумно двигаются под музыку. '
 #                   f'Если сменить композицию, '
 #                   f'то и темп движений птицы изменится')
        

class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    # Переопределите метод describe().
    def describe(self, full):
        if full == False:
            return print(super().describe())
        return print(f'Размер пингвина {self.name} '
                    f'из рода {self.genus} - {self.size}. '
                    f'Интересный факт: однажды группа '
                    f'геологов-разведчиков похитила пингвинье яйцо, '
                    f'и их принялась преследовать вся стая, '
                    f'не пытаясь, впрочем, при этом нападать. '
                    f'Посовещавшись, похитители вернули птицам яйцо, '
                    f'и те отстали.')



kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe(False)
kowalski.describe(True)
