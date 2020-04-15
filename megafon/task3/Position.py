from megafon.task3.Worker import Worker


# I don't actually got the idea of inheritance from Worker to Position, but if you ask so..
class Position(Worker):

    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def get_total_income(self):
        return self._position["salary"] + self._position["bonus"]
