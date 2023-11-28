import pytest

from exceptions import QualityBoundException
from gilded_rose import Item
from validators import validate_item


def test_validate_sulfuras_with_correct_quality():
    sulfuras = Item("Sulfuras, Hand of Ragnaros", 0, 80)
    validate_item(sulfuras)


def test_validate_sulfuras_with_incorrect_quality():
    sulfuras = Item("Sulfuras, Hand of Ragnaros", 0, 79)
    with pytest.raises(QualityBoundException):
        validate_item(sulfuras)


def test_validate_normal_item_with_quality_within_range():
    normal_item = Item("Normal Item", 10, 20)
    validate_item(normal_item)


def test_validate_item_with_quality_out_of_range():
    normal_item = Item("Normal Item", 10, 55)
    with pytest.raises(QualityBoundException):
        validate_item(normal_item)
