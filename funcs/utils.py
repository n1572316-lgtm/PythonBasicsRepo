from typing import Union, List, Any, Optional


def greet(name:str) -> str:
    return f"Hello, {name}"


def sum(num_1: Union [int, float], num_2: Optional [int] = 0) -> int |float:
    return num_1 + num_2


def multi(num_1: int | float, num_2: int | float) -> int |float:
    return num_1 * num_2


def print_list(arr: List[Any]) -> None:
    print(arr)


if __name__ == "_main_":
     print_list([1, 2, 3, 4])
