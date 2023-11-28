from exceptions import QualityBoundException


def validate_item(item) -> None:
    if item.name == "Sulfuras, Hand of Ragnaros":
        if item.quality != 80:
            raise QualityBoundException(
                f"Quality of item {item.name} should be 80, it has a value of {item.quality}"
            )
    elif item.quality > 50 or item.quality < 0:
        raise QualityBoundException(
            f"Quality of item {item.name} is not in the correct range, it has a value of {item.quality}"
        )
