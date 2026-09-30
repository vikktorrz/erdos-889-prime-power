#include <bits/stdc++.h>
using namespace std;

pair<int, int> prime_power(int x, const vector<int>& spf) {
    if (x <= 1)
        return {-1, -1};

    int p = spf[x];

    if (p < 2)
        return {-1, -1};

    int e = 0;

    while (x > 1) {
        if (x % p != 0)
            return {-1, -1};

        x /= p;
        ++e;
    }

    return {p, e};
}

int main(int argc, char** argv) {
    int N = (argc >= 2 ? atoi(argv[1]) : 10000000);

    if (N < 53) {
        cerr << "N must be at least 53\n";
        return 1;
    }

    vector<int> spf(N + 1, 0);
    vector<int> primes;

    for (int i = 2; i <= N; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            primes.push_back(i);
        }

        for (int p : primes) {
            if (p > spf[i])
                break;

            long long v = 1LL * i * p;

            if (v > N)
                break;

            spf[v] = p;
        }
    }

    int solutions = 0;

    for (int p = 29; p <= N; p += 24) {
        if (spf[p] != p)
            continue;

        int a = p - 4;
        int b = (p - 3) / 2;
        int c = (p - 2) / 3;
        int d = (p - 1) / 4;

        if (c % 3 == 0)
            continue;

        auto A = prime_power(a, spf);
        auto B = prime_power(b, spf);
        auto C = prime_power(c, spf);
        auto D = prime_power(d, spf);

        if (A.first == -1 ||
            B.first == -1 ||
            C.first == -1 ||
            D.first == -1) {
            continue;
        }

        ++solutions;

        cout
            << "p=" << p
            << "  n=" << p - 5
            << "  "
            << p - 4 << "=" << A.first << "^" << A.second
            << ", "
            << p - 3 << "=2*" << B.first << "^" << B.second
            << ", "
            << p - 2 << "=3*" << C.first << "^" << C.second
            << ", "
            << p - 1 << "=4*" << D.first << "^" << D.second
            << '\n';
    }

    cerr << "solutions=" << solutions << '\n';

    return 0;
}