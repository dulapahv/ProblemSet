#include <stdio.h>
#include <float.h>

int main() {
    float f = -64011388.0f;
    while (f > -FLT_MIN) {
        f /= 2.0f;
        printf("%f", f);
    }
}