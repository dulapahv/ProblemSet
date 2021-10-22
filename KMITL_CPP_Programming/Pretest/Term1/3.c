#include <stdio.h>

float rect_area(float width, float height) {
    float area = width * height;
    return area;
}

float rect_perimeter(float width, float height) {
    float perimeter = 2 * (width + height);
    return perimeter;
}

int main() {
    float width, height, area, perimeter;
    printf("Width = ");
    scanf("%f", &width);
    printf("Height = ");
    scanf("%f", &height);
    area = rect_area(width, height);
    perimeter = rect_perimeter(width, height);
    printf("Area = %f\n", area);
    printf("Perimeter = %f\n", perimeter);
    return 0;
}