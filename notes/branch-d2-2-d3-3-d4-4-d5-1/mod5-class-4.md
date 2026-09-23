# The \(p\equiv4\pmod5\) Subbranch

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
p\equiv4\pmod5.
$$

## 1. The forced prime \(P=5\)

Since

$$
5\mid p-4,
$$

and

$$
p-4=P^\alpha
$$

is a prime power, necessarily

$$
\boxed{P=5}.
$$

Thus

$$
p-4=5^\alpha,
$$

so

$$
\boxed{p=5^\alpha+4.}
\tag{1}
$$

Because \(p\equiv5\pmod{24}\),

$$
5^\alpha=p-4\equiv1\pmod{24}.
$$

The residue \(5\) has order \(2\) modulo \(24\), so

$$
\boxed{\alpha\text{ is even}.}
$$

Write

$$
\alpha=2m.
$$

Then

$$
\boxed{p=25^m+4.}
\tag{2}
$$

## 2. The \(k=2\) condition forces \(Q^\beta\) to be prime

From

$$
p-3=2Q^\beta,
$$

equation (2) gives

$$
\boxed{
Q^\beta=\frac{25^m+1}{2}.
}
\tag{3}
$$

Set

$$
x=5^m.
$$

Then (3) becomes

$$
\boxed{x^2+1=2Q^\beta.}
\tag{4}
$$

We first exclude \(\beta>1\).

### Case \(\beta=2\)

Reducing (4) modulo \(5\),

$$
1\equiv2Q^2\pmod5.
$$

Hence

$$
Q^2\equiv3\pmod5,
$$

which is impossible because \(3\) is not a quadratic residue modulo \(5\).

Therefore

$$
\beta\ne2.
$$

### Case \(\beta>2\)

We use the classical theorem on

$$
x^2+1=2y^n.
$$

For positive integers \(x,y\) with \(y>1\) and \(n>1\), the only
nontrivial solution is

$$
(x,y,n)=(239,13,4).
$$

See the classical work of Ljunggren and subsequent simplified treatments.

Our value

$$
x=5^m
$$

cannot equal \(239\). Hence \(\beta>2\) is impossible.

Consequently,

$$
\boxed{\beta=1}.
$$

Therefore

$$
\boxed{
\frac{25^m+1}{2}=Q
}
$$

is prime.

## 3. The exponent \(m\) is a power of \(2\)

Suppose \(m\) has an odd divisor \(r>1\). Write

$$
m=ar,
\qquad r\text{ odd}.
$$

Put

$$
X=25^a.
$$

Then

$$
25^m+1=X^r+1.
$$

Since \(r\) is odd,

$$
X^r+1
=
(X+1)
\left(
X^{r-1}-X^{r-2}+\cdots-X+1
\right).
$$

Hence

$$
Q
=
\frac{X+1}{2}
\left(
X^{r-1}-X^{r-2}+\cdots-X+1
\right).
$$

Both factors are integers greater than \(1\). Indeed, \(X\ge25\) and
\(r\ge3\).

This contradicts the primality of \(Q\).

Therefore \(m\) has no odd divisor, and hence

$$
\boxed{m=2^s}
$$

for some \(s\ge0\).

Thus

$$
\boxed{
p=25^{2^s}+4.
}
\tag{5}
$$

## 4. Sophie Germain eliminates \(s\ge1\)

Suppose

$$
s\ge1.
$$

Set

$$
z=5^{2^{s-1}}.
$$

Then

$$
z^4
=
5^{2^{s+1}}
=
25^{2^s}.
$$

Consequently

$$
p=z^4+4.
$$

By the Sophie Germain identity,

$$
z^4+4
=
(z^2-2z+2)(z^2+2z+2).
$$

Both factors exceed \(1\), so \(p\) is composite.

This contradicts the assumption that \(p\) is prime.

Therefore

$$
\boxed{s=0}.
$$

Hence

$$
m=1,
\qquad
p=25+4=29.
$$

Thus

$$
n=p-5=24.
$$

## 5. The surviving value belongs to another branch

For \(n=24\),

$$
n+3=27=3^3.
$$

Therefore at \(k=3\), the large prime-power component is \(3^3>3\), meaning that the corresponding divisor decomposition has

$$
d_3=1,
$$

not

$$
d_3=3.
$$

Thus \(n=24\) does not belong to the branch currently under consideration. It was already classified in the branch

$$
d_2=2,\qquad d_3=1.
$$

## Conclusion

The entire residue class

$$
\boxed{p\equiv4\pmod5}
$$

produces no new solutions in the branch

$$
d_2=2,\quad d_3=3,\quad d_4=4,\quad d_5=1.
$$

The only formal survivor is

$$
p=29,\qquad n=24,
$$

but this value belongs to the already closed \(d_3=1\) branch.

Hence

$$
\boxed{
p\equiv4\pmod5
\Longrightarrow
\text{no new solution}.
}
$$

