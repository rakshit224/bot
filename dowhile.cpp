#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    int a,b,c;
    cout<<"enter a mumber : ";
    cin>>a;
    cout<<"enter a number 2 : ";
    cin>>b;
    do{
        c=a*b;
        cout<<"the sum of a and b is :"<<c;
       
}
while (c<20);
return 0;
}
