from gilded_rose import Item
from updaters.conjured_item_updater import ConjuredItemUpdater


def test_quality_decreases_by_2_before_sell_by():
    item = Item("Conjured Apple", sell_in=5, quality=10)
    updater = ConjuredItemUpdater(item)
    updater.update()
    assert item.quality == 8, "Quality should decrease by 2"


def test_quality_decreases_twice_as_fast_after_sell_by():
    item = Item("Conjured Apple", sell_in=0, quality=10)
    updater = ConjuredItemUpdater(item)
    updater.update()
    assert item.quality == 6, "Quality should decrease by 4"
