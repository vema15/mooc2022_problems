def hash_square(length):
    count = 1
    while count <= length:
        print("#" * length)
        count += 1


if __name__ == "__main__":
    hash_square(5)