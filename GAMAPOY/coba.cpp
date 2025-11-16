#include <bits/stdc++.h>
using namespace std;

void update(int *a, int *b) {
    int x = *a, y = *b;
    *a = x + y;
    *b = (x > y) ? (x - y) : (y - x);
}

int main() {
    int a, b;
    if (!(cin >> a >> b)) return 0;
    update(&a, &b);
    cout << a << "\n" << b << "\n";
    return 0;
}