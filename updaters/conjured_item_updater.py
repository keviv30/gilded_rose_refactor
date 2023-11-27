from updaters import constants
from updaters.abstract_item_updater import AbstractItemUpdater


class ConjuredItemUpdater(AbstractItemUpdater):
    def update(self):
        self._decrease_sell_in()
        decrease_amount = 4 if self.item.sell_in < 0 else 2
        self._decrease_quality(amount=decrease_amount)

    def _decrease_quality(self, amount: int):
        new_quality = self.item.quality - amount
        self.item.quality = max(new_quality, constants.MIN_QUALITY)

    def _decrease_sell_in(self):
        # Decrease sell_in by 1
        self.item.sell_in -= 1
