class LootBag:

    def add_toy_for_child(self, toy, child):
        return

    def list_toys_for_child(self, child):
        if child == 'Vincent':
            return ['Ball']
        elif child == 'Walter':
            return []
        else:
            return ['Slime']

    def remove_toy_for_child(self, toy, child):
        return

    def list_children_getting_presents(self):
        return ['Vincent', 'Walter']

    def deliver_to_child(self, child):
        return

    def get_delivery_status_child(self, child):
        if child == 'Fernando':
            return True
        else:
            return False
