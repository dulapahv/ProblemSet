#include <stdio.h>

#define PI 3.141592

double calcRectangle(double length, double width);
double calcSquare(double side);
double calcTriangle(double length, double heigth);
double calcCircle(double radius);

int main() {
    int choice;
    double x, y = 0;
    printf("What do you want to calculate?\n1. Rectangle\n2. Square\n3. Triangle\n4. Circle\n");
    scanf("%d", &choice);

    switch (choice) {
    case 1: // Rectangle
        printf("Length: ");
        scanf("%lf", &x);
        printf("Width: ");
        scanf("%lf", &y);
        printf("%lf", calcRectangle(x, y));
        break;
    
    case 2: // Sqauare
        printf("Side: ");
        scanf("%lf", &x);
        printf("%lf", calcSquare(x));
        break;

    case 3: // Triangle
        printf("Length: ");
        scanf("%lf", &x);
        printf("Height: ");
        scanf("%lf", &y);
        printf("%lf", calcTriangle(x, y));
        break;
    
    case 4: // Circle
        printf("Radius: ");
        scanf("%lf", &x);
        printf("%lf", calcCircle(x));
        break;

    default:
        break;
    }
    return 0;
}

double calcRectangle(double length, double width) {
    return length * width;
}

double calcSquare(double side) {
    return side * side;
}

double calcTriangle(double length, double heigth) {
    return 0.5 * length * heigth;
}

double calcCircle(double radius) {
    return PI * (radius * radius);
}