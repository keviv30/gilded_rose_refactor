import pytest
from updaters.normal_item_updater import NormalItemUpdater
from gilded_rose import Item

def test_normal_item_quality_degrades():
    item = Item("Normal Item", sell_in=10, quality=20)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.quality == 19
    assert item.sell_in == 9

def test_quality_degrades_twice_as_fast_after_sell_by_date():
    item = Item("Normal Item", sell_in=0, quality=20)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.quality == 18
    assert item.sell_in == -1


def test_quality_never_negative():
    item = Item("Normal Item", sell_in=10, quality=0)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.quality == 0
    assert item.sell_in == 9

def test_quality_degrades_twice_as_fast_and_never_negative():
    item = Item("Normal Item", sell_in=0, quality=1)
    updater = NormalItemUpdater(item)
    updater.update()
    assert item.quality == 0
    assert item.sell_in == -1
