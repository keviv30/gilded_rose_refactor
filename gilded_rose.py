# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List, TypeVar, Generic, Type

from updaters.abstract_item_updater import AbstractItemUpdater
from updaters.aged_brie_updater import AgedBrieUpdater
from updaters.backstage_pass_updater import BackstagePassUpdater
from updaters.conjured_item_updater import ConjuredItemUpdater
from updaters.normal_item_updater import NormalItemUpdater
from updaters.sulfuras_updater import SulfurasUpdater


T = TypeVar('T', bound=AbstractItemUpdater)


class GildedRose(Generic[T]):
    def __init__(self, items: List[Item]):
        self.items = items
        self.updater_map = {
            "Aged Brie": AgedBrieUpdater,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater,
            "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
            "conjured": ConjuredItemUpdater
        }

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item.name)(item)
            updater.update()

    def get_updater(self, item_name: str) -> Type[T]:

        if "conjured" in item_name.lower():
            return self.updater_map["conjured"]

        return self.updater_map.get(item_name, NormalItemUpdater)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
