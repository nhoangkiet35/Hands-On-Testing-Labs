#include <iostream>
using namespace std;

bool isPrime(int num)
{
    if (num < 2)
        return false;
    for (int i = 2; i * i <= num; i++)
    {
        if (num % i == 0)
            return false;
    }
    return true;
}

int main()
{
    int choice;
    do
    {
        cout << "\nMENU:\n1. Kiểm tra số nguyên tố\n2. Kiểm tra năm nhuận\n3. Thoát\n";
        cout << "Nhập lựa chọn: ";
        cin >> choice;

        if (choice == 1)
        {
            int num;
            cout << "Nhập một số nguyên dương: ";
            cin >> num;
            if (isPrime(num))
                cout << num << " là số nguyên tố.\n";
            else
                cout << num << " không phải là số nguyên tố.\n";
        }
    } while (choice != 3);
    return 0;
}