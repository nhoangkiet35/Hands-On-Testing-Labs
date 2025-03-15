def value(s: str) -> int:
    s = s.lower()  # Chuyển về chữ thường để so sánh không phân biệt hoa/thường
    if s.startswith("hello"):
        return 0
    elif s.startswith("h"):
        return 20
    else:
        return 100


def main():
    user_input = input("Enter a string: ")
    print(f"Value: {value(user_input)}")


if __name__ == "__main__":
    main()
