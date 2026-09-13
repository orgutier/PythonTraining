from exercises.week02.solution import fizzbuzz, is_prime


def test_fizzbuzz():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(18) is False
