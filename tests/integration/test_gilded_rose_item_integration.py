"""
Requirements:
- All items have a SellIn value which denotes the number of days we have to sell the item
- All items have a Quality value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

Other requirements:
- Once the sell by date has passed, Quality degrades twice as fast
- The Quality of an item is never negative
- "Aged Brie" actually increases in Quality the older it gets
- The Quality of an item is never more than 50
- "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert
"""

from gilded_rose import GildedRose, Item


def test_quality_degrades_twice_as_fast_after_sell_by_date():

    # Given
    normal_item = Item("Normal Item", sell_in=1, quality=10)
    gilded_rose = GildedRose(items=[normal_item])

    # When
    gilded_rose.update_quality()

    # Then
    assert normal_item.sell_in == 0
    assert normal_item.quality == 9  # Quality should decrease by 1

    # When
    gilded_rose.update_quality()

    # Then
    assert normal_item.sell_in == -1
    assert normal_item.quality == 7  # Quality should decrease by 2


def test_quality_never_negative():
    # Given
    items = [Item("Normal Item", 0, 0)]
    gilded_rose = GildedRose(items)

    # When
    gilded_rose.update_quality()

    # Then
    assert items[0].quality == 0
