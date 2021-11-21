def fizz_buzz(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return "FIZZBUZZ"
    if num % 3 == 0:
        return "FIZZ"
    if num % 5 == 0:
        return "BUZZ"
    return str(num)


if __name__ == "__main__":
    for num in range(1, 101):
        print(f"{num} : {fizz_buzz(num)}")
