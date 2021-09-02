def fibonacci(x):
    global nth

    # Error checking
    if (x <= 0) or (x - int(x) != 0):
        return "Enter positive integer"

    n1, n2 = 0, 1  # initializing first two terms of the sequence
    count = 0

    if x == 1:
        return 0  # if there is only one term, return n1
    if x == 2:
        return 1  # if there is only one term, return n1
    # generate fibonacci sequence
    else:
        while count < x - 2:
            nth = n1 + n2  # update value of nth term
            n1 = n2  # update past values
            n2 = nth
            count += 1  # update count
        return nth


def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(8) == 13
    assert fibonacci(11) == 55
    assert fibonacci(0) == "Enter positive integer"
    assert fibonacci(-1) == "Enter positive integer"
    assert fibonacci(3.7) == "Enter positive integer"
