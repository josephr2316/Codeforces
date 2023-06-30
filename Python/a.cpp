#include <iostream>

using namespace std;

int main()
{
    int n, f, total(0), answer(0);
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> f;
        total += f;
    }
    for (int i = 1; i <= 5; ++i)
    {
        printf("%d",total);
        printf("%d",n);
        if ((total + i) % (n + 1) != 1)
        {
            answer += 1;
            p
            printf("%d",answer);
        }
    }
    cout << answer << endl;
    return 0;
}