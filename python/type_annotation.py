text: str = 'python'
num_int: int = 10
num_float: float = 10.5
data_list: list[int | str] = [1,'2',3,4,5]
ok: bool = True
empty: None = None
data_dict:  dict[str | int, int | str | None] = {'a': 1, 'b': 2, 3: 'c', 3: None}
data_byte: bytes = b'hello'
data_set: set[int | str] = {1,2,3,4,5,'python'}
list_inside_list: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_tuple: tuple[int | str, ...] = 1, 2, 3, 4, 'python'

print(data_list)
print(data_dict)
print(data_byte)
print(data_set)
print(list_inside_list)
print(data_tuple)

# ---------------------------------------------------------------------------------------------------------------------------------------

def plus(a: int, b: int) -> int:
    return a + b

print(plus(2, 2))

# ---------------------------------------------------------------------------------------------------------------------------------------

def show_text(text: str) -> None:
    print(text)
    
print(show_text('hello'))

# ---------------------------------------------------------------------------------------------------------------------------------------

def list_numbers(count: int, a: int) -> list[list[int]]:
    
    '''Functions that returns a list of numbers and their squares'''
    
    return [[i, i ** 2] for i in range(count)]

print(list_numbers.__doc__)
print(list_numbers.__annotations__)

# ---------------------------------------------------------------------------------------------------------------------------------------

def sum_numbers(*args: int) -> int:
    '''Function that returns the sum of numbers'''
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))

# ---------------------------------------------------------------------------------------------------------------------------------------

def get_dict(**kwargs: str) -> dict[str, str]:
    return kwargs

print(get_dict(name='John', age='30'))