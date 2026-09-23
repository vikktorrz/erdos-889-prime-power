# The \(p\equiv1\pmod5\) Subbranch

We study the branch

$$
d_2=2,\qquad d_3=3,\qquad d_4=4,\qquad d_5=1,
$$

with

$$
p=n+5
$$

prime and

$$
p-4=P^\alpha,\qquad
p-3=2Q^\beta,\qquad
p-2=3R^\gamma,\qquad
p-1=4S^\delta.
$$

Assume

$$
p\equiv1\pmod5.
$$

Then \(5\mid p-1\), so the prime-power base in

$$
p-1=4S^\delta
$$

must be

$$
\boxed{S=5}.
$$

Therefore

$$
p=4\cdot5^\delta+1.
\tag{1}
$$

## 1. The exponent \(\delta\) is even

Since \(p\equiv5\pmod{24}\), in particular

$$
p\equiv2\pmod3.
$$

Reducing (1) modulo \(3\),

$$
p\equiv (-1)^\delta+1\pmod3.
$$

For \(p\equiv2\pmod3\), we must have

$$
(-1)^\delta=1.
$$

Hence

$$
\boxed{\delta\text{ is even}.}
$$

Write

$$
\delta=2m,
\qquad m\ge1.
$$

Then

$$
\boxed{
p=4\cdot25^m+1.
}
\tag{2}
$$

## 2. The \(k=3\) condition gives a contradiction

We have

$$
p-2=4\cdot25^m-1.
$$

Since the branch requires

$$
p-2=3R^\gamma,
$$

we must have

$$
R^\gamma
=
\frac{4\cdot25^m-1}{3}.
\tag{3}
$$

Factor the numerator:

$$
4\cdot25^m-1
=
(2\cdot5^m-1)(2\cdot5^m+1).
$$

Therefore

$$
R^\gamma
=
\frac{(2\cdot5^m-1)(2\cdot5^m+1)}{3}.
\tag{4}
$$

The two factors

$$
A=2\cdot5^m-1,
\qquad
B=2\cdot5^m+1
$$

satisfy

$$
\gcd(A,B)=1.
$$

Moreover, exactly one of \(A,B\) is divisible by \(3\). Indeed,

$$
5^m\equiv(-1)^m\pmod3,
$$

so exactly one of

$$
2\cdot5^m-1,\qquad
2\cdot5^m+1
$$

is \(0\pmod3\).

After dividing that factor by \(3\), we therefore obtain two
coprime positive integers whose product is \(R^\gamma\).

Both factors are greater than \(1\):

$$
2\cdot5^m-1\ge9,
$$

and

$$
2\cdot5^m+1\ge11.
$$

The factor divisible by \(3\) cannot become \(1\) after division, since it
is at least \(9\).

Thus (4) expresses \(R^\gamma\) as a product of two coprime integers
greater than \(1\). This is impossible because \(R^\gamma\) is a power of
a single prime.

Hence the assumption

$$
p\equiv1\pmod5
$$

leads to a contradiction.

## Conclusion

The entire residue class

$$
\boxed{p\equiv1\pmod5}
$$

is impossible in the branch

$$
d_2=2,\quad d_3=3,\quad d_4=4,\quad d_5=1.
$$

No solutions occur in this residue class.
