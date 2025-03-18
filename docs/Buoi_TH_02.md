# Unit Test với Pytest

## 1. Giới thiệu về Pytest

Pytest là một framework kiểm thử mạnh mẽ và linh hoạt trong Python, được sử dụng rộng rãi để viết và thực thi các test case cho các ứng dụng phần mềm. Pytest hỗ trợ kiểm thử đơn vị (unit testing), kiểm thử tích hợp (integration testing) và kiểm thử hồi quy (regression testing).

### Các tính năng nổi bật của Pytest

- **Cú pháp đơn giản**: Không cần kế thừa từ `unittest.TestCase`, chỉ cần viết các hàm kiểm thử bắt đầu bằng `test_`.
- **Hỗ trợ kiểm tra ngoại lệ**: Dễ dàng kiểm tra các lỗi bằng `pytest.raises()`.
- **Cơ chế đánh dấu (markers)**: Cho phép gán nhãn các test case để kiểm soát việc chạy kiểm thử.
- **Hỗ trợ fixture**: Cung cấp khả năng thiết lập dữ liệu trước khi test và dọn dẹp sau khi test.
- **Báo cáo lỗi chi tiết**: Khi một test case thất bại, Pytest hiển thị thông tin chi tiết giúp dễ dàng xác định nguyên nhân lỗi.

## 2. Cài đặt Pytest

### Bước 1: Cài đặt thư viện pytest

Chạy lệnh sau trong terminal:

```sh
py -m pip install pytest
```

Hoặc cài đặt thông qua Package Manager trong PyCharm.

### Bước 2: Cấu trúc thư mục kiểm thử

Giả sử thư mục chứa 3 file:

- `main.py`: Chứa chương trình chính.
- `doi_tuong/chuc_nang.py`: Chứa các hàm xử lý.
- `test_doi_tuong/chuc_nang.py`: Chứa các test case kiểm thử.

**Lưu ý:**

- Các hàm kiểm thử phải bắt đầu bằng `test_`.
- Các file `doi_tuong/chuc_nang.py` và `test_doi_tuong/chuc_nang.py` phải nằm cùng một thư mục để có thể thực hiện kiểm thử.

### Bước 3: Tiến hành kiểm thử

Chạy lệnh sau để kiểm thử:

```sh
py -m pytest test_doi_tuong/chuc_nang.py
```

Mỗi dấu `.` màu xanh lá biểu thị test case passed, còn `F` màu đỏ biểu thị test case failed.

## 3. Ví dụ minh họa

### **File `doi_tuong/chuc_nang.py`**

```python
# Tìm ước chung lớn nhất
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

# Tối giản phân số
def simplify(numerator: int, denominator: int) -> tuple:
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Nhập phân số
def input_fraction(numerator: int, denominator: int) -> tuple:
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return simplify(numerator, denominator)
```

### **File `main.py`**

```python
from doi_tuong.chuc_nang import input_fraction

def main():
    print("Fraction Calculator")
    num1 = int(input("Enter numerator of first fraction: "))
    den1 = int(input("Enter denominator of first fraction: "))
    num2 = int(input("Enter numerator of second fraction: "))
    den2 = int(input("Enter denominator of second fraction: "))
    try:
        frac1 = input_fraction(num1, den1)
        frac2 = input_fraction(num2, den2)
        print(f"Addition: {add_fractions(frac1, frac2)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### **File `test_doi_tuong/chuc_nang.py`**

```python
import pytest
from doi_tuong.chuc_nang import input_fraction

def test_input_fraction():
    assert input_fraction(3, 4) == (3, 4)
    assert input_fraction(2, 4) == (1, 2)
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        input_fraction(1, 0)
    with pytest.raises(TypeError, match=".*must be integers.*"):
        input_fraction(1.5, 2)
```

## 4. Các tính năng phổ biến của Pytest

### 4.1 Kiểm tra ngoại lệ - `pytest.raises()`

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
```

### 4.2 Chuẩn bị dữ liệu test - `@pytest.fixture`

Dùng `@pytest.fixture` để tạo dữ liệu cần thiết cho các test case, giúp tránh lặp lại code setup.

```python
import pytest
@pytest.fixture
def sample_data():
    return (1, 2)

def test_fraction(sample_data):
    assert sample_data == (1, 2)
```

### 4.3 Gắn thẻ test case - `@pytest.mark`

Sử dụng `@pytest.mark.<tên_marker>` để đánh dấu test case, giúp tổ chức chạy test dễ dàng hơn.

```python
import pytest
@pytest.mark.slow
def test_heavy_computation():
    import time
    time.sleep(5)
    assert True
```

Chạy test với marker:

```sh
pytest -m slow
```

### 4.4 Chạy lại test bị lỗi hoặc dừng sau `n` lỗi

```sh
pytest --maxfail=2 test_example.py
```

## 5. Các lệnh Pytest phổ biến

```sh
pytest test_example.py  # Chạy tất cả test trong file test_example.py
pytest -v               # Hiển thị chi tiết kết quả kiểm thử
pytest -s               # Hiển thị output từ các câu lệnh print()
pytest --maxfail=2      # Dừng kiểm thử sau 2 lỗi đầu tiên
pytest -m marker_name   # Chạy các test có marker cụ thể
pytest --durations=3    # Hiển thị 3 test chạy chậm nhất
pytest --disable-warnings # Bỏ qua cảnh báo khi chạy test
```

## 6. Kết luận

Pytest là một framework mạnh mẽ và linh hoạt giúp đơn giản hóa quá trình kiểm thử trong Python. Với cú pháp dễ hiểu, hỗ trợ fixture, marker và báo cáo lỗi chi tiết, Pytest giúp việc viết và chạy unit test trở nên nhanh chóng và hiệu quả.
