#include <bits/stdc++.h>
using namespace std;

bool is_prime_power(long long x, int spf_x) {
    while (x % spf_x == 0)
        x /= spf_x;

    return x == 1;
}

pair<long long, int> prime_power(long long x, const vector<int>& spf) {
    int p = spf[x];
    int e = 0;

    while (x % p == 0) {
        x /= p;
        ++e;
    }

    if (x != 1)
        return {-1, -1};

    return {p, e};
}

int main(int argc, char** argv) {
    int N = (argc >= 2 ? atoi(argv[1]) : 10000000);

    vector<int> spf(N + 1);
    vector<int> primes;

    for (int i = 2; i <= N; ++i) {
        if (spf[i] == 0) {
            spf[i] = i;
            primes.push_back(i);
        }

        for (int p : primes) {
            if (p > spf[i] || 1LL * i * p > N)
                break;

            spf[i * p] = p;
        }
    }

    int solutions = 0;

    for (int p = 5; p <= N; p += 24) {
        if (spf[p] != p)
            continue;

        long long a = p - 4;
        long long b = (p - 3) / 2;
        long long c = (p - 2) / 3;
        long long d = (p - 1) / 4;

        // d_3 = 3 requires gcd(3,c) = 1.
        if (c % 3 == 0)
            continue;

        auto A = prime_power(a, spf);
        auto B = prime_power(b, spf);
        auto C = prime_power(c, spf);
        auto D = prime_power(d, spf);

        if (A.first == -1 ||
            B.first == -1 ||
            C.first == -1 ||
            D.first == -1)
            continue;

        ++solutions;

        cout << "p=" << p
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
}
