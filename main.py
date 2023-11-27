import argparse

from gilded_rose import GildedRose, Item


def main():
    parser = argparse.ArgumentParser(
        description="Gilded Rose Inventory Management System"
    )

    parser.add_argument(
        "-u",
        "--update",
        type=int,
        metavar="DAYS",
        default=0,
        help="Update quality of all items for a specified number of days (default 10 days)",
    )
    parser.add_argument(
        "-d",
        "--display",
        action="store_true",
        help="Display current inventory before and after update",
    )

    args = parser.parse_args()

    items = [
        Item("Aged Brie", 2, 0),
        Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
        Item("Conjured Apple", 3, 6),
        # Add other items here
    ]
    gilded_rose = GildedRose(items)

    if args.display:
        print("\nInventory current status:\n")
        display_inventory(items)

    if args.update > 0:
        for day in range(1, args.update + 1):
            gilded_rose.update_quality()
            if args.display:
                print(f"\nInventory Status - Day {day}:")
                display_inventory(items)

    if args.display and args.update > 0:
        print(f"\nCompleted updating for {args.update} day(s).")


def display_inventory(items):
    for item in items:
        print(item)


if __name__ == "__main__":
    main()
