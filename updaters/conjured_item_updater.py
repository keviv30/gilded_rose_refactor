from updaters.abstract_item_updater import AbstractItemUpdater


class ConjuredItemUpdater(AbstractItemUpdater):
    def update(self):
        self._decrease_sell_in()
        decrease_amount = 4 if self.item.sell_in < 0 else 2
        self._decrease_quality(amount=decrease_amount)
