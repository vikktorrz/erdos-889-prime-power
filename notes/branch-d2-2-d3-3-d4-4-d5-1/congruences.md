# Congruence Analysis of the Four Consecutive Prime-Power Branch

We study the branch

$$
d_2=2,\qquad d_3=3,\qquad d_4=4,\qquad d_5=1.
$$

Write

$$
n=p-5,
$$

where \(p=n+5\) is prime. Since \(24\mid n\), we have

$$
\boxed{p\equiv5\pmod{24}}.
$$

The conditions for \(k=1,\ldots,4\) become

$$
\boxed{
\begin{aligned}
p-4&=P^\alpha,\\
p-3&=2Q^\beta,\\
p-2&=3R^\gamma,\\
p-1&=4S^\delta.
\end{aligned}}
$$

Equivalently,

$$
\boxed{
\begin{aligned}
P^\alpha&=p-4,\\
Q^\beta&=\frac{p-3}{2},\\
R^\gamma&=\frac{p-2}{3},\\
S^\delta&=\frac{p-1}{4}.
\end{aligned}}
$$

Because \(p\equiv5\pmod{24}\),

$$
P^\alpha\equiv1\pmod{24},
$$

$$
Q^\beta\equiv1\pmod{12},
$$

$$
R^\gamma\equiv1\pmod8,
$$

and

$$
S^\delta\equiv1\pmod6.
$$

Hence, whenever the corresponding exponent is odd,

$$
\begin{aligned}
\alpha\text{ odd}&\Longrightarrow P\equiv1\pmod{24},\\
\beta\text{ odd}&\Longrightarrow Q\equiv1\pmod{12},\\
\gamma\text{ odd}&\Longrightarrow R\equiv1\pmod8,\\
\delta\text{ odd}&\Longrightarrow S\equiv1\pmod6.
\end{aligned}
$$

## Forced occurrence of the prime \(5\)

For \(p>5\), exactly one of

$$
p-1,\quad p-2,\quad p-3,\quad p-4
$$

is divisible by \(5\).

Since the explicit factors \(1,2,3,4\) are all coprime to \(5\), the
corresponding prime-power base must be \(5\). Thus one of

$$
P,Q,R,S
$$

is necessarily equal to \(5\).

More precisely,

$$
\boxed{
\begin{array}{c|c}
p\pmod5 & \text{forced prime}\\
\hline
1&S=5\\
2&R=5\\
3&Q=5\\
4&P=5
\end{array}}
$$

This gives four natural residue branches modulo \(5\).

## Known solution

The known solution in this branch is

$$
p=53,\qquad n=48.
$$

Indeed,

$$
49=7^2,
\qquad
50=2\cdot5^2,
\qquad
51=3\cdot17,
\qquad
52=4\cdot13.
$$

Thus

$$
(P,\alpha)=(7,2),\qquad
(Q,\beta)=(5,2),\qquad
(R,\gamma)=(17,1),\qquad
(S,\delta)=(13,1).
$$

The value \(p=29\) gives

$$
25=5^2,\quad26=2\cdot13,\quad27=3^3,\quad28=4\cdot7,
$$

but it belongs to the \(d_3=1\) branch because \(n+3=27\) has the large
prime-power component \(3^3\).

## Immediate research targets

The next goal is to derive restrictions on the four exponents

$$
\alpha,\beta,\gamma,\delta.
$$

In particular:

1. Determine whether any exponent \(>1\) forces strong congruence
   restrictions on \(p\).

2. Analyze separately the four cases

$$
p\equiv1,2,3,4\pmod5,
$$

using the fact that the corresponding base is \(5\).

3. Combine the congruences modulo \(5\) with the conditions modulo
   \(8,12,24\) and small primes such as \(7,11,13\).

4. Investigate whether the system

$$
p-4=P^\alpha,\quad
p-3=2Q^\beta,\quad
p-2=3R^\gamma,\quad
p-1=4S^\delta
$$

can be reduced to finitely many exponent patterns.

The current evidence does **not** establish that \(p=53\) is unique.
The value \(p=53\) is therefore treated only as a known solution.
# Initial Congruence Analysis

We study the branch

$$
d_2=2,\qquad d_3=3,\qquad d_4=4,\qquad d_5=1.
$$

Writing

$$
n=p-5,
$$

the conditions for \(k=1,\ldots,4\) become

$$
\boxed{
\begin{aligned}
p-4&=P^\alpha,\\
p-3&=2Q^\beta,\\
p-2&=3R^\gamma,\\
p-1&=4S^\delta,
\end{aligned}}
$$

where \(p\) is prime.

Since \(24\mid n\),

$$
\boxed{p\equiv5\pmod{24}}.
$$

## Immediate congruence restrictions

From \(p\equiv5\pmod{24}\),

$$
P^\alpha=p-4\equiv1\pmod{24},
$$

$$
Q^\beta=\frac{p-3}{2}\equiv1\pmod{12},
$$

$$
R^\gamma=\frac{p-2}{3}\equiv1\pmod8,
$$

and

$$
S^\delta=\frac{p-1}{4}\equiv1\pmod6.
$$

Consequently:

* if \(\alpha\) is odd, then \(P\equiv1\pmod{24}\);
* if \(\beta\) is odd, then \(Q\equiv1\pmod{12}\);
* if \(\gamma\) is odd, then \(R\equiv1\pmod8\);
* if \(\delta\) is odd, then \(S\equiv1\pmod6\).

The primes \(P,Q,R,S\) are distinct from \(2\) and \(3\).

## A forced prime equal to 5

Since \(p>5\) is prime,

$$
p\not\equiv0\pmod5,
$$

so

$$
p\equiv1,2,3,4\pmod5.
$$

Exactly one of \(p-1,p-2,p-3,p-4\) is therefore divisible by \(5\).
Since the small factors \(2,3,4\) are not divisible by \(5\), the
corresponding prime-power base must equal \(5\).

More precisely,

$$
\boxed{
\begin{array}{c|c}
p\pmod5 & \text{forced base}\\
\hline
1&S=5\\
2&R=5\\
3&Q=5\\
4&P=5
\end{array}}
$$

Thus at least one of the four prime-power bases \(P,Q,R,S\) is always
equal to \(5\).

## Known configuration

The known example in this branch is

$$
p=53,
\qquad n=48,
$$

for which

$$
53-4=49=7^2,
$$

$$
53-3=50=2\cdot5^2,
$$

$$
53-2=51=3\cdot17,
$$

$$
53-1=52=4\cdot13.
$$

Thus

$$
(P,\alpha)=(7,2),\quad
(Q,\beta)=(5,2),\quad
(R,\gamma)=(17,1),\quad
(S,\delta)=(13,1).
$$

The case \(p=29\) gives

$$
29-4=25,\quad
29-3=26,\quad
29-2=27,\quad
29-1=28,
$$

but \(29-2=27=3^3\) has its remaining prime-power component divisible by \(3\).
Hence it belongs to the \(d_3=1\) branch rather than the present
\(d_3=3\) branch.

## Research questions

The immediate targets are:

1. Can the forced occurrence of the prime \(5\) be combined with congruences
   modulo \(7,11,13,\ldots\) to eliminate some residue classes of \(p\)?

2. Can one prove restrictions on the exponents
   \(\alpha,\beta,\gamma,\delta\)?

3. Can the four equations be combined into a genuine Diophantine theore
