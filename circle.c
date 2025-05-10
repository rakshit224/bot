#include <stdio.h>
#include <math.h>

int main() {
    int radius = 5;  // Radius of the circle
    int center_x = radius;
    int center_y = radius;

    for (int y = 0; y < 2*radius; y++) {
        for (int x = 0; x < 2*radius; x++) {
            // Circle equation (x-center_x)^2 + (y-center_y)^2 = r^2
            if ( (int)(pow(x - center_x, 2) + pow(y - center_y, 2)) <= pow(radius, 2)) {
                printf("P");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}
