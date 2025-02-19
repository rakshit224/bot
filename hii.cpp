#include<iostream>
#include<string>
using namespace std;

int main() {
    string name,secondname;
    int age, standard;
    system("cls");  // Clear the console screen
    cout << "Enter your name: ";
    cin >> name>>secondname;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Enter your class: ";
    cin >> standard;

    cout << "Hello " << name<<secondname<< ", your name is.\nYour age is " << age << ".\nYou study in class " << standard << "." << endl;

    return 0;
}