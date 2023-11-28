from updaters.abstract_item_updater import AbstractItemUpdater


class AgedBrieUpdater(AbstractItemUpdater):
    def update(self):
        self._decrease_sell_in()
        increase_amount = 2 if self.item.sell_in < 0 else 1
        self._increase_quality(amount=increase_amount)
