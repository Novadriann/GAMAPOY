#include <stdio.h>

void update(int *a, int *b) {
    int x = *a, y = *b;
    *a = x + y;
    *b = (x > y) ? (x - y) : (y - x);
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int *pa = &a, *pb = &b;
    update(pa, pb);
    printf("%d\n%d", a, b);
    return 0;
}
