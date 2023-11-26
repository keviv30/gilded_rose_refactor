from abc import ABC, abstractmethod

class AbstractItemUpdater(ABC):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update(self):
        pass