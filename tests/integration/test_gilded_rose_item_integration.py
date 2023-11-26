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


def test_quality_of_aged_brie_increase_after_sell_date():
    # Given
    items = [Item("Aged Brie", 0, 10)]
    gilded_rose = GildedRose(items)

    # When
    gilded_rose.update_quality()

    # Then
    assert items[0].quality == 12


def test_item_quality_never_exceeds_50():
    # Given
    items = [
        Item("Aged Brie", sell_in=2, quality=48),
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    ]
    gilded_rose = GildedRose(items=items)

    for _ in range(10):
        # When
        gilded_rose.update_quality()

        # Then
        # Check that quality of each item never exceeds 50
        for item in items:
            assert item.quality <= 50


def test_sulfuras_never_changes():
    # Given
    items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
    gilded_rose = GildedRose(items)

    # When
    gilded_rose.update_quality()

    # Then
    assert items[0].sell_in == 0
    assert items[0].quality == 80


def test_normal_item_degradation():
    # Given
    items = [Item("Normal Item", 5, 10)]
    gilded_rose = GildedRose(items)

    # When
    gilded_rose.update_quality()

    # Then
    assert items[0].quality == 9

    # When
    # After sell-by date
    items[0].sell_in = -1
    gilded_rose.update_quality()
    assert items[0].quality == 7


def test_gilded_rose_with_various_items():
    # Given
    items = [
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Normal Item", sell_in=10, quality=20),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    ]
    gilded_rose = GildedRose(items)

    # When
    gilded_rose.update_quality()

    # Then
    assert items[0].quality == 1  # Aged Brie increases in quality
    assert items[1].quality == 50  # Backstage passes increase by 3 but cap at 50
    assert items[2].quality == 19  # Normal item degrades by 1
    assert items[3].quality == 80 # Sulfuras quality does not change


def test_backstage_passes_before_after_concert():

    # Given
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=45),
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=47)
    ]

    gilded_rose = GildedRose(items)

    # When
    gilded_rose.update_quality()

    # Then
    assert items[0].quality == 21  # Increases by 1 when more than 10 days left
    assert items[1].quality == 47  # Increases by 2 when 10 days or less
    assert items[2].quality == 50  # Increases by 3 but caps at 50

    # Update again to simulate day passing
    gilded_rose.update_quality()
    assert items[2].quality == 0
