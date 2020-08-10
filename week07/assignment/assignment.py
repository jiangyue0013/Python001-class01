from abc import ABCMeta


class Animal(metaclass=ABCMeta):
    def __init__(self, a_type, size, character) -> None:
        self.a_type = a_type
        self.size = size
        self.character = character
    
    @property
    def is_fierce_animal(self):
        if ((self.size == '中' or self.size == '大') 
            and self.a_type == '食肉' 
            and self.character == '凶猛'):
            return True
        else:
            return False


class Cat(Animal):
    cry = '喵'
    def __init__(self, name, a_type, size, character) -> None:
        super(Cat, self).__init__(a_type, size, character)
        self.name = name
    
    @property
    def is_pet(self):
        return not self.is_fierce_animal


class Zoo(object):
    def __init__(self, name) -> None:
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal):
        animal_id = id(animal)
        animal_class_name = animal.__class__.__name__

        if animal_id in self.animals:
            print(f'{animal_class_name} exists.')
            return
        else:
            self.animals[animal_id] = animal_class_name
        
        if not hasattr(self, animal_class_name):
            setattr(self, animal_class_name, [animal])
        else:
            self[animal_class_name].append(animal)
        print(f'Add {animal_class_name}({animal_id})')
        

if __name__ == "__main__":
    z = Zoo('时间动物园')
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    z.add_animal(cat1)
    have_cat = getattr(z, 'Cat')
    print(have_cat)