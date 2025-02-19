#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    system("cls");
    int a,b;

    cout<<"enter a number a : ";
    cin>>a;
    cout<<"enter a number b : ";
    cin>>b;
    a=a+b;
    b=a-b;
    a=a-b;
    cout<<a;
    cout<<b;
    return 0;
}