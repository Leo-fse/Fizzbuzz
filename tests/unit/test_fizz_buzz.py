import pytest
from FizzBuzz import fizz_buzz


class Test文字列に変換:
    @pytest.mark.parametrize("num", [1, 2, 4])
    def test_そのまま(self, num):
        """そのまま文字列に変換する"""
        assert fizz_buzz(num) == str(num)

    @pytest.mark.parametrize("num", [3, 6, 9])
    def test_3の倍数はFizzに変換(self, num):
        result = fizz_buzz(num)
        assert result == "FIZZ"

    @pytest.mark.parametrize("num", [5, 10, 25])
    def test_5の倍数はBUZZに変換(self, num):
        assert fizz_buzz(num) == "BUZZ"

    @pytest.mark.parametrize("num", [15, 30, 45])
    def test_15の倍数はFIZZBUZZに変換(self, num):
        assert fizz_buzz(num) == "FIZZBUZZ"
