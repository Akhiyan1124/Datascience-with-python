def test_for_loop():
    numbers = [5, 10, 15]
    total = 0
    for num in numbers:
        total += num
    print("For Loop Test:", "PASS" if total == 30 else "FAIL")


def test_while_loop():
    count = 3
    result = []
    while count > 0:
        result.append(count)
        count -= 1
    print("While Loop Test:", "PASS" if result == [3,2,1] else "FAIL")


def test_break_continue():
    found = False
    for i in range(5):
        if i == 3:
            found = True
            break
    print("Break Test:", "PASS" if found else "FAIL")

    evens = []
    for i in range(1,6):
        if i % 2 != 0:
            continue
        evens.append(i)
    print("Continue Test:", "PASS" if evens == [2,4] else "FAIL")


if __name__ == "__main__":
    test_for_loop()
    test_while_loop()
    test_break_continue()
    print("All tests completed!")
