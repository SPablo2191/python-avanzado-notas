from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass

    def sleep(self):
        print("Sleeping...")


class Human(Animal):
    def talk(self):
        pass


pablo = Human()
pablo.talk()
pablo.sleep()