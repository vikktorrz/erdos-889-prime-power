#include <bits/stdc++.h>
using namespace std;

// Exact search for the Erdős–Selfridge prime-power variant:
//
// V(n,k) = number of p such that p^{nu_p(n+k)} > k.
//
// We seek all n <= N with max_{k>=1} V(n,k) <= 1.
//
// Let Q2(m) be the second-largest prime-power component of m.
// Then V(n,k) >= 2 iff Q2(n+k) > k.
// Hence m=n+k covers n precisely when
//
//     m - Q2(m) + 1 <= n <= m-1.
//
// Also, V(n,k)>=2 implies k^2-k<n.

static int Kbound(long long N) {
    long long k = 1;
    while ((k + 1) * (k + 1) - (k + 1) < N) ++k;
    return (int)k;
}

int main(int argc, char** argv) {
    int N = (argc >= 2 ? atoi(argv[1]) : 1000000);
    if (N < 1) return 1;

    const int K = Kbound(N);
    const int M = N + K;

    cerr << "N=" << N << " K=" << K << " M=" << M << '\n';

    // Smallest prime factor table via a linear sieve.
    vector<uint32_t> spf(M + 1, 0);
    vector<int> primes;
    primes.reserve(M / max(1, (int)log((double)M)));

    for (int i = 2; i <= M; ++i) {
        if (spf[i] == 0) {
            spf[i] = (uint32_t)i;
            primes.push_back(i);
        }

        for (int p : primes) {
            if (p > (int)spf[i] || 1LL * i * p > M) break;
            spf[i * p] = (uint32_t)p;
        }
    }

    // q2[m] = second-largest prime-power component of m.
    vector<uint32_t> q2(M + 1, 0);

    for (int m = 2; m <= M; ++m) {
        int x = m;
        uint64_t best1 = 0, best2 = 0;

        while (x > 1) {
            int p = (int)spf[x];
            uint64_t q = p;

            x /= p;
            while (x > 1 && (int)spf[x] == p) {
                x /= p;
                q *= (uint64_t)p;
            }

            if (q > best1) {
                best2 = best1;
                best1 = q;
            } else if (q > best2) {
                best2 = q;
            }
        }

        q2[m] = (uint32_t)best2;
    }

    // Difference-array interval coverage.
    vector<int32_t> diff(N + 2, 0);

    for (int m = 2; m <= M; ++m) {
        uint32_t q = q2[m];
        if (q == 0) continue;

        int L = max(1, m - (int)q + 1);
        int R = min(N, m - 1);

        if (L <= R) {
            ++diff[L];
            --diff[R + 1];
        }
    }

    vector<int> exceptions;
    int coverage = 0;

    for (int n = 1; n <= N; ++n) {
        coverage += diff[n];
        if (coverage == 0) exceptions.push_back(n);
    }

    cout << "exceptions=" << exceptions.size() << '\n';
    cout << "last="
         << (exceptions.empty() ? -1 : exceptions.back()) << '\n';

    for (size_t i = 0; i < exceptions.size(); ++i) {
        if (i) cout << ' ';
        cout << exceptions[i];
    }
    cout << '\n';

    vector<long long> hist(32, 0);
    int max_k = 0, max_n = -1;

    unordered_set<int> is_exception;
    is_exception.reserve(exceptions.size() * 2 + 1);

    for (int n : exceptions) is_exception.insert(n);

    for (int n = 1; n <= N; ++n) {
        if (is_exception.count(n)) continue;

        int witness = -1;

        for (int k = 1; k <= K; ++k) {
            if (q2[n + k] > (uint32_t)k) {
                witness = k;
                break;
            }
        }

        if (witness < 0) {
            cerr << "ERROR: no witness for n=" << n << '\n';
            return 2;
        }

        if (witness >= (int)hist.size())
            hist.resize(witness + 1);

        ++hist[witness];

        if (witness > max_k) {
            max_k = witness;
            max_n = n;
        }
    }

    cout << "max_min_k=" << max_k
         << " at_n=" << max_n << '\n';

    for (int k = 1; k <= max_k; ++k) {
        if (hist[k])
            cout << k << ':' << hist[k] << ' ';
    }

    cout << '\n';
}