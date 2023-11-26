import pytest
from updaters.backstage_pass_updater import BackstagePassUpdater
from gilded_rose import Item


@pytest.mark.parametrize("sell_in, quality, expected_quality", [
    (11, 20, 21),  # Quality increases by 1 when sell_in > 10
    (10, 20, 22),  # Quality increases by 2 when sell_in <= 10
    (5, 20, 23),   # Quality increases by 3 when sell_in <= 5
])
def test_backstage_pass_quality(sell_in: int, quality: int, expected_quality: int) -> None:
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
    updater = BackstagePassUpdater(item)
    updater.update()
    assert item.quality == expected_quality
