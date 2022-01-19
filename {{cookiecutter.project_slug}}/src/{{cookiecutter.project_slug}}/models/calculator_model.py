import enum


class Operation(enum.Enum):
    ADD = "+"
    SUB = "-"

    @classmethod
    def member_values(cls) -> list:
        return [i.value for i in cls._member_map_.values()]  # type: ignore


class CalculatorModel:
    def __init__(self):
        self._result = 0

    def calc(self, value1: float, operation: Operation, value2: float):
        if not isinstance(operation, Operation):
            raise ValueError("operation must be Operation")

        if operation.value == "+":
            self._result = value1 + value2
        elif operation.value == "-":
            self._result = value1 - value2
        else:
            raise ValueError(f"not support operation: {operation.value}")
        return self._result
