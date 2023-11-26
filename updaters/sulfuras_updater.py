from updaters.abstract_item_updater import AbstractItemUpdater


class SulfurasUpdater(AbstractItemUpdater):
    def update(self):
        # Sulfuras is a legendary item, so its SellIn and Quality values do not change.
        pass
