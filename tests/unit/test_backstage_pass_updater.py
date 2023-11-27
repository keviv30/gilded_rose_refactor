import pytest

from gilded_rose import Item
from updaters.backstage_pass_updater import BackstagePassUpdater


@pytest.mark.parametrize(
    "sell_in, quality, expected_quality",
    [
        (11, 20, 21),  # Quality increases by 1 when sell_in > 10
        (10, 20, 22),  # Quality increases by 2 when sell_in <= 10
        (5, 20, 23),  # Quality increases by 3 when sell_in <= 5
        (0, 20, 0),  # Quality drops to 0 on the day of the concert
        (5, 49, 50),  # Quality increases to 50 but not beyond
        (5, 50, 50),  # Quality stays at 50
    ],
)
def test_backstage_pass_quality(
    sell_in: int, quality: int, expected_quality: int
) -> None:
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
    updater = BackstagePassUpdater(item)
    updater.update()
    assert item.quality == expected_quality


@pytest.mark.parametrize(
    "sell_in, expected_sell_in",
    [
        (15, 14),  # Normal decrease
        (0, -1),  # Decrease when at 0
        (-10, -11),  # Decrease when negative
    ],
)
def test_backstage_pass_sell_in(sell_in: int, expected_sell_in: int) -> None:
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, 20)
    updater = BackstagePassUpdater(item)
    updater.update()
    assert item.sell_in == expected_sell_in
