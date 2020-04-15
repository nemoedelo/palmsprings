class Worker:
    def __init__(self, name, surname, salary, bonus):
        self._name = name
        self._surname = surname
        self._position = {"salary": salary, "bonus": bonus}
