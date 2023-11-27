from updaters import constants
from updaters.abstract_item_updater import AbstractItemUpdater


class AgedBrieUpdater(AbstractItemUpdater):
    def update(self):
        self._decrease_sell_in()
        increase_amount = 2 if self.item.sell_in < 0 else 1
        self._increase_quality(amount=increase_amount)

    def _increase_quality(self, amount: int):
        new_quality = self.item.quality + amount
        self.item.quality = min(new_quality, constants.MAX_QUALITY)

    def _decrease_sell_in(self):
        self.item.sell_in -= 1
