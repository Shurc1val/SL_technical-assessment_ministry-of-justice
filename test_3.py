
# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.

import pytest
from datetime import datetime

def sum_current_time(time_str: str = datetime.now().strftime("%H:%M:%S"),
                     verify_time_input = False) -> int:
    """
    Returns sum of the numbers in time_str, given in the format %H:%M:%S; defaults to current time
    if no time is given.

    Optional argument verify_time_input to check if the time_str input is a valid time in the
    correct form; default value is False. If verify_time_input is True, and time_str is invalid,
    -1 is returned and an error message printed to the console.
    """

    if verify_time_input:
        try:
            datetime.strptime(time_str, "%H:%M:%S")
        except (ValueError, TypeError) as error:
            print("Invalid time_str entered: ", error)
            return -1 

    return sum([int(num) for num in time_str.split(":")])


@pytest.mark.parametrize('time_str, exp_result', [
        ("01:02:03", 6),
        ("09:12:54", 75),
        ("15:10:59", 84),
        ("01:10:00", 11),
        ("8:10:59", 77), # datetime.strptime() will parse this as valid time object of desired form
        ("00:00:00", 0),
        ("23:59:59", 141)
    ],
    ids = [
        'basic_test_1',
        'basic_test_2',
        'basic_test_3',
        'basic_test_4',
        'no_leading_zero',
        'all_zeros',
        'highest_value_of_each'
    ]
)
def test_sum_current_time_valid_inputs(time_str: str, exp_result):
    """Tests the function sum_current_time for various valid inputs."""
    assert sum_current_time(time_str) == exp_result
    assert sum_current_time(time_str, False) == sum_current_time(time_str, True)
        # Checks that the verify_time_input parameter does not change the result


def test_sum_current_time_no_input():
    """
    Tests that running the function with no input returns an integer output that is greater than or
    equal to zero (any other testing either makes assumptions on how long the function will take to
    run, or may fail if run at certain times).
    """
    time_sum = sum_current_time()
    assert isinstance(time_sum, int)
    assert time_sum >= 0


@pytest.mark.parametrize('time_str', [
        (6),
        (True),
        ("hello"),
        ("01:02"),
        ("09"),
        ("28:10:59"),
        ("24:12:08")
    ],
    ids = [
        'invalid_type_1',
        'invalid_type_2',
        'invalid_format_1',
        'invalid_format_2',
        'invalid_format_3',
        'invalid_time_1',
        'invalid_time_2'
    ]
)
def test_sum_current_time_invalid_inputs(time_str: str):
    """Tests the function sum_current_time correctly handles various invalid inputs."""
    assert sum_current_time(time_str, True) == -1