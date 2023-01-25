from typing import Tuple, Union, List
from string import digits, ascii_letters

DEFAULT_SYMBOLS = digits + ascii_letters


def base_converter(input_str: str, input_base: int = 10, output_base: int = 10,
        symbols: Union[str, List[str]]= DEFAULT_SYMBOLS, min_length: int= 1) -> str:
    """Converts between any two bases"""
    int_equivalent = alt_base_str_to_int(input_str, input_base, symbols)
    return int_to_alt_base(int_equivalent, output_base, symbols, min_length)

def _generate_compliant_symbols_list(symbols: Union[str, List[str]],
        base: int) -> Tuple[List[str], int]:
    "Build a symbols list compatible with the base"
    power: int = 1
    new_symbols: List[str] = []

    symbol_count = len(symbols)

    if symbol_count >= base:
        return list(symbols), 1

    while base > symbol_count**power:
        power += 1

    for i in range(base):
        new_symbols.append(''.join(_int_to_alt_base_str_list(i, symbol_count, symbols, power)))

    return new_symbols, power

def int_to_alt_base(value: int, base: int, symbols: Union[str, List[str]]= DEFAULT_SYMBOLS,
        min_length: int = 1) -> str:
    """Convert an int directly to an alternate base"""
    symbols, _ = _generate_compliant_symbols_list(symbols, base)
    return ''.join(_int_to_alt_base_str_list(value, base, symbols, min_length))

def _int_to_alt_base_str_list(value: int, base: int,
        symbols: Union[str, List[str]]= DEFAULT_SYMBOLS, min_length: int = 1) -> List[str]:
    """
    Converts an integer to an alternate base using symbols as the key for which symbol
    represents which numbers.
    """
    symbols, _ = _generate_compliant_symbols_list(symbols, base)
    return [symbols[i] for i in _int_to_alt_base_int_list(value, base, min_length)]

def _int_to_alt_base_int_list(value: int, base: int, min_length: int= 1) -> List[int]:
    """
    Converts an integer into a alternate base. Each character in the new number is
    stored as an integer value in an array.
    """
    nums: List[int] = []
    while len(nums) < min_length or value != 0:
        value, remainder = divmod(value, base)
        nums.insert(0, remainder)
    return nums

def alt_base_str_to_int(alt_base_str: str, base: int,
        symbols: Union[str, List[str]]= DEFAULT_SYMBOLS) -> int:
    """Convert a string of alternate base into an integer"""
    symbols, symbol_len = _generate_compliant_symbols_list(symbols, base)
    separated_str = [alt_base_str[i:i+symbol_len] for i in range(0, len(alt_base_str), symbol_len)]
    return _alt_base_str_list_to_int(separated_str, base, symbols)

def _alt_base_str_list_to_int(alt_base_str_list: List[str], base: int,
        symbols: Union[str, List[str]]= DEFAULT_SYMBOLS) -> int:
    """Convert list of symbols and a base value into its integer equivalent"""
    symbols, _ = _generate_compliant_symbols_list(symbols, base)
    try:
        return _alt_base_int_list_to_int(
            [symbols.index(symbol) for symbol in alt_base_str_list], base)
    except ValueError as err:
        print("It's likely a symbol in alt_base_str_list wasn't in symbols")
        raise err

def _alt_base_int_list_to_int(alt_base_int_list: List[int], base: int) -> int:
    """
    Takes a list of values representing a written number and a base the number is written in
    and calculate the original number in base 10.
    """
    int_value: int = 0
    for index, list_val in enumerate(reversed(alt_base_int_list)):
        int_value += (base**index) * list_val
    return int_value
