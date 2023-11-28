from abc import ABC, abstractmethod

from updaters import constants


class AbstractItemUpdater(ABC):
    def __init__(self, item):
        self.item = item

    @abstractmethod
    def update(self):
        pass

    def _decrease_quality(self, amount: int):
        new_quality = self.item.quality - amount
        self.item.quality = max(new_quality, constants.MIN_QUALITY)

    def _increase_quality(self, amount: int):
        new_quality = self.item.quality + amount
        self.item.quality = min(new_quality, constants.MAX_QUALITY)

    def _decrease_sell_in(self):
        self.item.sell_in -= 1
