/*
 * Author: Xusniddin Qalandarov
 * Date: 25/10/2023
 * Name: Xusniddin Qalandarov
 */

#include <iostream>

using namespace std;

bool isLeapYear(int year) {
  return (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0));
}

int main() {
  int year;
  cout << "Enter a year: ";
  cin >> year;

  if (isLeapYear(year)) {
    cout << year << " is a leap year." << endl;
  } else {
    cout << year << " is not a leap year." << endl;
  }

  return 0;
}
