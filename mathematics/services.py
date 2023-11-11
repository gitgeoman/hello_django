def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a + b


def div(a: int, b: int) -> float:
    if b == 0:
        raise ValueError('Arg b cannot be 0.')
    return a / b


def mul(a: int, b: int) -> float:
    return a * b


operations = {
    'add': add,
    'sub': sub,
    'div': div,
    'mul': mul,
}


class AlgebraService:

    def calculate(operation: str, a: int, b: int) -> int | float:
        return operations[operation](a, b)
