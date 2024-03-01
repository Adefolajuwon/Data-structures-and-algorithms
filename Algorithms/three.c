#include <stdio.h>

void solve_simultaneous_eq(float coefficients[3][3], float constants[3]) {
    float x, y, z;
    float det = coefficients[0][0] * (coefficients[1][1] * coefficients[2][2] - coefficients[1][2] * coefficients[2][1]) -
                coefficients[0][1] * (coefficients[1][0] * coefficients[2][2] - coefficients[1][2] * coefficients[2][0]) +
                coefficients[0][2] * (coefficients[1][0] * coefficients[2][1] - coefficients[1][1] * coefficients[2][0]);

    if (det == 0) {
        printf("The system of equations has no unique solution.\n");
        return;
    }

    x = (constants[0] * (coefficients[1][1] * coefficients[2][2] - coefficients[1][2] * coefficients[2][1]) -
         constants[1] * (coefficients[0][1] * coefficients[2][2] - coefficients[0][2] * coefficients[2][1]) +
         constants[2] * (coefficients[0][1] * coefficients[1][2] - coefficients[0][2] * coefficients[1][1])) / det;

    y = (constants[0] * (coefficients[1][2] * coefficients[2][0] - coefficients[1][0] * coefficients[2][2]) -
         constants[1] * (coefficients[0][2] * coefficients[2][0] - coefficients[0][0] * coefficients[2][2]) +
         constants[2] * (coefficients[0][2] * coefficients[1][0] - coefficients[0][0] * coefficients[1][2])) / det;

    z = (constants[0] * (coefficients[1][0] * coefficients[2][1] - coefficients[1][1] * coefficients[2][0]) -
         constants[1] * (coefficients[0][0] * coefficients[2][1] - coefficients[0][1] * coefficients[2][0]) +
         constants[2] * (coefficients[0][0] * coefficients[1][1] - coefficients[0][1] * coefficients[1][0])) / det;

    printf("Solution: x = %.2f, y = %.2f, z = %.2f\n", x, y, z);
}

int main() {
    float coefficients[3][3];
    float constants[3];

    // Get input from the user
    printf("Enter the coefficients of the equations (3x3 matrix):\n");
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            scanf("%f", &coefficients[i][j]);
        }
    }

    printf("Enter the constants of the equations (3x1 matrix):\n");
    for (int i = 0; i < 3; ++i) {
        scanf("%f", &constants[i]);
    }

    // Call the function to solve the equations
    solve_simultaneous_eq(coefficients, constants);

    return 0;
}
