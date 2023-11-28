# Refactoring GildedRose Kata

The Gilded Rose Refactoring Project is a Python-based application designed to 
manage an inventory system for shop named "The Gilded Rose". 
The aim of this project refactors GildedRose legacy/original code.
Please see the link below for more info:
https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.txt

The original code was refactored taking account of object-oriented design and 
test-driven development (TDD) practices. 
The application updates the quality and sell-in value of items in the shop's 
inventory as time progresses.

Features

- Inventory Management: Automatically updates the quality and sell-in values of items in the inventory.
- Special Item Rules: Implements unique rules for special items like "Aged Brie," "Backstage passes," and "Sulfuras."
- Conjured Item feature implementation: Includes functionality for "Conjured" items, 
which decreases in quality faster than normal items.

Requirements

- Python 3.6 or higher
- pip (Python package manager)
- pytest
- black
- isort
- mypy

### Installation

Installation

1) Clone the repository

```commandline
git clone git@github.com:keviv30/gilded_rose_refactor.git
cd gilded-rose-refactoring
```

2) Set up a virtual environment

```commandline
python -m venv venv
source venv/bin/activate
```

3) Install dependencies

```commandline
pip install -r requirements.txt
```

#### Running the Application

To run the Gilded Rose application, use:

Display current inventory:

```commandline
python main.py --display
```

Example output:

```
Inventory current status:

Aged Brie, 2, 0
Backstage passes to a TAFKAL80ETC concert, 10, 20
Conjured Apple, 3, 6
```

You can add more Items to the inventory if needed

Update items:

```commandline
python main.py --display --update 5
```

#### Running the pytests

```commandline
pytest -sv
```

#### Running the provided texttest

```commandline
./start_texttest.sh
```

Note: the texttest might fail for conjured item as it was initially treating them
as a normal item before refactor

Scopes of improvement:

- Adding logging to Gilded Rose project is a great idea, especially for tracking the status of items over time.
- Possibly add alert if a price of an item drops below certain threshold as a feature
- Adding more tests to cover varius scenarios
- Could use a factory-like method to get the correct updater for each item
