from abc import ABC, abstractmethod

class ITalk(ABC):
    @abstractmethod
    def talk(self):
        pass

class Human(ITalk):
    def talk(self):
        print("holaa")

class Robot(ITalk):
    def talk(self):
        print("bup bip bup")

talking_entity : ITalk = Robot()
talking_entity.talk()