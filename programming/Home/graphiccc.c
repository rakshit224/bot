#include<conio.h>
#include<stdio.h>
#include<graphics.h>
#include<math.h>
int main(){
    int gd=DETECT,gm;
    int x1,y1,x2,y2,i,steps,xinc, yinc,dx,dy;
    initgraph(&gd,&gm, (char*)"");
    printf("Enter the value of x1 and y1 :");
    scanf("%d%d",&x1,&y1);
    printf("Enter the value of x2 and y2 :");
    scanf("%d%d",&x2,&y2);
    // calculate dx and dy
    dx=x2-x1;  
    dy=y2-y1;
    // calculate steps
    if(abs(dx)>abs(dy))
    {
        steps=abs(dx);
    }
    else
    {
        steps=abs(dy);
    }
    // calculate xinc and yinc
    xinc=dx/steps;
    yinc=dy/steps;
    // draw the line
    for(i=1;i<=steps;i++)
    {
        putpixel(x1,y1,WHITE);
        delay(100);
        x1=x1+xinc;
        y1=y1+yinc;
    }
    getch();
    return 0;
}