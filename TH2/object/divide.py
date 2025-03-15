def divide(a: int, b: int) -> float:
    """Thực hiện phép chia a / b. Nếu b = 0, ném ra lỗi ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0.")
    return a / b
