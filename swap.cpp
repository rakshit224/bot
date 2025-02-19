#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    system("cls");
    int a,b,temp;

    cout<<"enter a number a : ";
    cin>>a;
    cout<<"enter a number b : ";        
    cin>>b;
    temp=a;
    a=b;
    b=temp;
    cout <<a;
    cout<<b;
    return 0;
}