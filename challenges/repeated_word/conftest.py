import pytest

@pytest.fixture
def example_string():
    """One example input string."""
    return 'it was the best of times, it was the worst of times'


@pytest.fixture
def example_two():
    """Another example input string."""
    return 'once upon a time, there was a brave princess who'


@pytest.fixture
def empty_string():
    """Empty input string."""
    return ''


@pytest.fixture
def singleton():
    """Single-word input string."""
    return 'the'

@pytest.fixture
def example_three():
    """Yet another example input string."""
    return 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York.'


@pytest.fixture
def bad_data():
    """Input that is not a string."""
    return 3


@pytest.fixture
def no_repeats():
    """Input with no repeats."""
    return 'the quick brown fox jumped over a lazy dog'
