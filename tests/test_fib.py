import pytest

from mypkg.fibonacci import fibonacci

def test_fib_10():
    assert(fibonacci(10) == 55)
