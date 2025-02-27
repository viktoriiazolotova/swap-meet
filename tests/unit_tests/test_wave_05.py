import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category == "Clothing"
    assert str(cloth) == "The finest clothing you could wear."

# @pytest.mark.skip
def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category == "Decor"
    assert str(decor) == "Something to decorate your space."

# @pytest.mark.skip
def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category == "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."

# @pytest.mark.skip
def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

# @pytest.mark.skip
def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    five_condition_description = items[0].condition_description()
    assert isinstance(five_condition_description, str)
    for item in items:
        assert item.condition_description() == five_condition_description

    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert isinstance(one_condition_description, str)

    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description

################# Added tests to increase code coverage  ####################
def test_items_have_condition_descriptions_fair_condition():
    items = [
        Clothing(condition=2),
        Decor(condition=2),
        Electronics(condition=2)
    ]
  
    assert items[0].condition_description() == "Fair condition"
    assert items[1].condition_description() == "Fair condition"
    assert items[2].condition_description() == "Fair condition"

def test_items_have_condition_descriptions_good_condition():
    items = [
        Clothing(condition=3),
        Decor(condition=3),
        Electronics(condition=3)
    ]

    assert items[0].condition_description() == "Good condition"
    assert items[1].condition_description() == "Good condition"
    assert items[2].condition_description() == "Good condition"

def test_items_have_condition_descriptions_normal_condition():
    items = [
        Clothing(condition=4),
        Decor(condition=4),
        Electronics(condition=4)
    ]
    
    assert items[0].condition_description() == "Normal condition"
    assert items[1].condition_description() == "Normal condition"
    assert items[2].condition_description() == "Normal condition"

def new_func():
    return False

def test_returns_false_if_items_have_condition_empty_string():
    items = [
        Clothing(condition=""),
        Decor(condition=""),
        Electronics(condition="")
    ]
    
    assert items[0].condition_description() == False
    assert items[1].condition_description() == False
    assert items[2].condition_description() == False