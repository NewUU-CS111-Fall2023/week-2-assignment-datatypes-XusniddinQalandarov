/*
 * Author:
 * Date:
 * Name:
 */

#include <iostream>
#include <random>

using namespace std;

int main() {
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<> dist(1, 100);

  int randomNumber = dist(gen);

  while (true) {
    int guess;
    cout << "Guess a number between 1 and 100: ";
    cin >> guess;

    if (guess == randomNumber) {
      cout << "Correct! You guessed the number!" << endl;
      break;
    } else if (guess < randomNumber) {
      cout << "Too low." << endl;
    } else {
      cout << "Too high." << endl;
    }
  }

  return 0;
}
