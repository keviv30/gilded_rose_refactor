import pytest

from gilded_rose import Item
from updaters.sulfuras_updater import SulfurasUpdater


def test_sulfuras_quality_remains_constant():
    quality = 80
    item = Item("Sulfuras, Hand of Ragnaros", sell_in=10, quality=quality)
    sulfuras_updater = SulfurasUpdater(item)
    sulfuras_updater.update()
    assert (
        item.quality == quality
    ), "Quality of 'Sulfuras' should remain constant"


def test_sulfuras_sell_in_remains_constant():
    sell_in = 10
    item = Item("Sulfuras, Hand of Ragnaros", sell_in=sell_in, quality=80)
    sulfuras_updater = SulfurasUpdater(item)
    sulfuras_updater.update()
    assert (
        item.sell_in == sell_in
    ), "SellIn of 'Sulfuras' should remain constant"
