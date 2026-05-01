def test_temp_avg():
    high = 65
    low = 42

    avg = (high + low) / 2

    assert avg == 53.5

if __name__ == "__main__":
    try:
        test_temp_avg()
        print("Test passed")
    except AssertionError:
        print("Test failed")