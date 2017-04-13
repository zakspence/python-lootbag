import unittest
from lootbag import *

class TestBagOLoot(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bag = LootBag()

    def test_add_toy_bag(self):
        self.bag.add_toy_for_child('Ball', 'Vincent')
        vincents_toys = self.bag.list_toys_for_child('Vincent')

        self.assertIsInstance(vincents_toys, list)
        self.assertIn('Ball', vincents_toys)

    def test_remove_toy_for_child(self):
        toy = 'Slinky'
        self.bag.add_toy_for_child(toy, 'Walter')

        self.assertIn('Walter', self.bag.list_children_getting_presents())

        self.bag.remove_toy_for_child(toy, 'Walter')
        vincents_toys = self.bag.list_toys_for_child('Walter')

        self.assertNotIn(toy, vincents_toys)

    def test_list_of_good_kids(self):
        good_kids = self.bag.list_children_getting_presents()

        self.assertIn('Vincent', good_kids)

    def test_toys_in_bag_for_specific_child(self):
        vincents_toys = self.bag.list_toys_for_child('Alejandro')

        self.assertIn('Slime', vincents_toys)

    def test_child_toys_are_delivered(self):
        toy = 'Nintendo 64'
        self.bag.add_toy_for_child(toy, 'Fernando')
        self.bag.deliver_to_child('Fernando')
        is_fernando_delivered = self.bag.get_delivery_status_child('Fernando')
        is_jessica_delivered = self.bag.get_delivery_status_child('Jessica')

        self.assertTrue(is_fernando_delivered)
        self.assertFalse(is_jessica_delivered)
