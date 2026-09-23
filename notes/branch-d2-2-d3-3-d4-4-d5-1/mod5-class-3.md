# The \(p\equiv3\pmod5\) Subbranch

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
p\equiv3\pmod5.
$$

Then \(5\mid p-3\), and since the explicit factor \(2\) is coprime to \(5\),

$$
Q=5.
$$

Hence

$$
p-3=2\cdot5^\beta,
$$

so

$$
\boxed{p=2\cdot5^\beta+3.}
\tag{1}
$$

## 1. The exponent \(\beta\) is even

Since \(p\equiv5\pmod{24}\), in particular

$$
p\equiv2\pmod3.
$$

Reducing (1) modulo \(3\),

$$
2\cdot5^\beta+3
\equiv
2(-1)^\beta
\pmod3.
$$

Therefore

$$
(-1)^\beta=1,
$$

and hence

$$
\boxed{\beta\text{ is even}.}
$$

Write

$$
\beta=2m.
$$

Then

$$
p=2\cdot5^{2m}+3.
$$

## 2. The exponent \(\delta\) is equal to \(1\)

From

$$
p-1=4S^\delta
$$

and (1),

$$
4S^\delta=2\cdot5^\beta+2
=2(5^\beta+1).
$$

Hence

$$
\boxed{
S^\delta=\frac{5^\beta+1}{2}.
}
$$

Put

$$
x=5^m.
$$

Since \(\beta=2m\),

$$
x^2+1=2S^\delta.
\tag{2}
$$

### Case \(\delta=2\)

Reducing (2) modulo \(5\),

$$
1\equiv2S^2\pmod5.
$$

Thus

$$
S^2\equiv3\pmod5,
$$

which is impossible because \(3\) is a quadratic non-residue modulo \(5\).

Hence

$$
\delta\ne2.
$$

### Case \(\delta>2\)

The classical classification of

$$
x^2+1=2y^r,\qquad xy>1,\ r>2,
$$

has the unique nontrivial solution

$$
(x,y,r)=(239,13,4).
$$

Our \(x=5^m\) cannot equal \(239\). Therefore \(\delta>2\) is impossible.

Consequently,

$$
\boxed{\delta=1.}
$$

Thus

$$
\boxed{
\frac{5^\beta+1}{2}=S
}
$$

is itself prime.

## 3. The exponent \(\beta\) is a power of \(2\)

Recall that

$$
\beta=2m.
$$

Suppose \(m\) has an odd divisor \(r>1\). Write

$$
m=ar
$$

and put

$$
X=5^{2a}.
$$

Then

$$
5^\beta+1=X^r+1
$$

and, because \(r\) is odd,

$$
X^r+1
=
(X+1)
\left(
X^{r-1}-X^{r-2}+\cdots-X+1
\right).
$$

Since \(X\) is odd,

$$
S=\frac{X+1}{2}
\left(
X^{r-1}-X^{r-2}+\cdots-X+1
\right).
$$

Both factors exceed \(1\), contradicting the primality of \(S\).

Therefore \(m\) has no odd divisor, so \(m\) is a power of \(2\).

Hence

$$
\boxed{
\beta=2^s
}
\qquad(s\ge1).
\tag{3}
$$

## 4. Elimination of \(s\ge2\)

From (1),

$$
p=2\cdot5^{2^s}+3.
$$

### Case 1: \(s\) even

For \(s\ge2\),

$$
2^s\equiv4\pmod6.
$$

Since \(5\) has order \(6\) modulo \(7\),

$$
5^{2^s}\equiv5^4\equiv2\pmod7.
$$

Therefore

$$
p
\equiv
2\cdot2+3
\equiv0
\pmod7.
$$

Since \(p>7\), this contradicts the primality of \(p\).

Thus no even \(s\ge2\) is possible.

### Case 2: \(s\) odd and \(s\ge3\)

Modulo \(5\),

$$
2^s\equiv3\pmod5.
$$

Since \(5\) has order \(5\) modulo \(11\),

$$
5^{2^s}\equiv5^3\equiv4\pmod{11}.
$$

Hence

$$
p
\equiv
2\cdot4+3
\equiv0
\pmod{11}.
$$

Since \(p>11\), this again contradicts primality.

Therefore the only possible value is

$$
\boxed{s=1}.
$$

Hence

$$
\boxed{\beta=2}.
$$

Substituting into (1),

$$
p=2\cdot5^2+3=53.
$$

Consequently,

$$
\boxed{n=p-5=48.}
$$

## Conclusion

The entire residue class

$$
\boxed{p\equiv3\pmod5}
$$

of the branch

$$
d_2=2,\quad d_3=3,\quad d_4=4,\quad d_5=1
$$

contains exactly one solution:

$$
\boxed{p=53,\qquad n=48.}
$$

Indeed,

$$
49=7^2,\qquad
50=2\cdot5^2,\qquad
51=3\cdot17,\qquad
52=4\cdot13.
$$

Thus the known exceptional value \(n=48\) is completely explained within
this residue class.
