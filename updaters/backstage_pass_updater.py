from updaters.abstract_item_updater import AbstractItemUpdater


class BackstagePassUpdater(AbstractItemUpdater):
    def update(self):
        self._update_quality()
        self._decrease_sell_in()
        self._reset_quality_if_concert_passed()

    def _update_quality(self):
        if self.item.sell_in > 10:
            self._increase_quality(amount=1)
        elif 5 < self.item.sell_in <= 10:
            self._increase_quality(amount=2)
        elif self.item.sell_in <= 5:
            self._increase_quality(amount=3)

    def _reset_quality_if_concert_passed(self):
        if self.item.sell_in < 0:
            self.item.quality = 0
