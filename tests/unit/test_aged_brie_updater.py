from updaters.aged_brie_updater import AgedBrieUpdater
from gilded_rose import Item


def test_aged_brie_quality_increases():
    item = Item("Aged Brie", 10, 20)
    updater = AgedBrieUpdater(item)
    updater.update()
    assert item.quality == 21


def test_aged_brie_quality_never_exceeds_50():
    item = Item("Aged Brie", 10, 49)
    updater = AgedBrieUpdater(item)
    updater.update()
    updater.update()  # Increasing twice to test the boundary
    assert item.quality == 50


def test_aged_brie_sell_in_decreases():
    item = Item("Aged Brie", 10, 20)
    updater = AgedBrieUpdater(item)
    updater.update()
    assert item.sell_in == 9


def test_aged_brie_quality_increases_twice_as_fast_after_sell_by():
    item = Item("Aged Brie", 0, 20)
    updater = AgedBrieUpdater(item)
    updater.update()
    assert item.quality == 22


def test_aged_brie_quality_stops_at_50_after_sell_by():
    item = Item("Aged Brie", 0, 49)
    updater = AgedBrieUpdater(item)
    updater.update()
    assert item.quality == 50