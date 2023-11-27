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


def test_quality_never_negative():
    item = Item("Conjured Mana Cake", sell_in=3, quality=1)
    updater = ConjuredItemUpdater(item)
    updater.update()
    assert item.quality == 0, "Quality should not go below 0"


def test_sell_in_decreases_each_day():
    item = Item("Conjured Mana Cake", sell_in=5, quality=10)
    updater = ConjuredItemUpdater(item)
    updater.update()
    assert item.sell_in == 4, "SellIn should decrease by 1"
