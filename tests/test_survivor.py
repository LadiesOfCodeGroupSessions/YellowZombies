# write tests here, don't forget to import what you need and
# info: https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class
from main.survivor import Survivor
from pytest import raises


class TestZombies:

    def test_check_survivor_has_name(self):
        survivor = Survivor("Judy")

        assert survivor.name == "Judy"

    def test_check_survivor_has_zero_wounds(self):
        survivor = Survivor("Judy")

        assert survivor.wounds == 0

    def test_survivor_dies_immediately_after_two_wounds(self):
        survivor = Survivor("Judy")

        survivor.wounds = 1
        assert survivor.is_dead is False

        survivor.wounds = 2
        assert survivor.is_dead is True

        survivor.wounds = 3
        assert survivor.is_dead is True

    def test_name_can_be_anything(self):
        survivor = Survivor("Becky")
        assert survivor.name == "Becky"

    def test_survivor_starts_with_3_actions(self):
        survivor = Survivor("Becky")
        assert survivor.actions == 3  # changename?

    def test_survivor_can_carry_up_to_five_pieces_of_equipment(self):
        survivor = Survivor("Becky")

        survivor.pick_equipment("Baseball bat")
        survivor.pick_equipment("Frying pan")
        survivor.pick_equipment("Katana")
        survivor.pick_equipment("Pistol")
        survivor.pick_equipment("Bottled Water")

        assert len(survivor.equipments) == 5

        with raises(Exception) as limit_reached_exception:
            # print("Hakuna Matata")
            survivor.pick_equipment("Molotov")

        assert "Limit reached" in str(limit_reached_exception.value)
        # print(limit_reached_exception.value)

    def test_survivor_can_carry_up_to_two_in_hand_equipment(self):
        survivor = Survivor("Becky")

        survivor.pick_equipment("Baseball bat")
        survivor.pick_equipment("Frying pan")
        survivor.pick_equipment("Katana")

        assert len(survivor.in_hand_equipment) <= 2
        assert survivor.in_hand_equipment[0] == "Baseball bat"
        assert survivor.in_hand_equipment[1] == "Frying pan"

    def test_survivor_can_carry_up_to_three_in_reserve(self):
        survivor = Survivor("Becky")

        survivor.pick_equipment("Baseball bat")
        survivor.pick_equipment("Frying pan")
        survivor.pick_equipment("Katana")
        survivor.pick_equipment("Pistol")
        survivor.pick_equipment("Bottled Water")

        assert len(survivor.in_hand_equipment) <= 2
        assert survivor.in_hand_equipment[0] == "Baseball bat"
        assert survivor.in_hand_equipment[1] == "Frying pan"

        assert len(survivor.in_reserve) <= 3
        assert survivor.in_reserve[0] == "Katana"
        assert survivor.in_reserve[1] == "Pistol"
        assert survivor.in_reserve[2] == "Bottled Water"

    def test_survivor_gets_wound_and_reduces_equipment(self):
        survivor = Survivor("Becky")

        survivor.pick_equipment("Baseball bat")
        survivor.pick_equipment("Frying pan")
        survivor.pick_equipment("Katana")
        survivor.pick_equipment("Pistol")
        survivor.pick_equipment("Bottled Water")

        survivor.wounds = 1
        assert len(survivor.equipments) == 4
        assert survivor.in_hand_equipment[0] == "Baseball bat"
        assert survivor.in_hand_equipment[1] == "Frying pan"

        assert survivor.in_reserve[0] == "Katana"
        assert survivor.in_reserve[1] == "Pistol"
        assert survivor.in_reserve[2] is None

