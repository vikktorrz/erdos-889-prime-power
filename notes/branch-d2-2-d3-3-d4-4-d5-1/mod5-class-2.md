# The \(p\equiv2\pmod5\) Subbranch

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
p\equiv2\pmod5.
$$

## 1. The forced prime \(R=5\)

Since \(5\mid p-2\), while the explicit factor \(3\) is coprime to \(5\),

$$
\boxed{R=5}.
$$

Therefore

$$
p-2=3\cdot5^\gamma,
$$

so

$$
\boxed{p=3\cdot5^\gamma+2.}
\tag{1}
$$

## 2. The exponent \(\gamma\) is even

We have

$$
p\equiv5\pmod{24},
$$

hence in particular

$$
p\equiv5\pmod8.
$$

Since

$$
5^\gamma\equiv
\begin{cases}
5\pmod8,&\gamma\text{ odd},\\
1\pmod8,&\gamma\text{ even},
\end{cases}
$$

equation (1) gives

$$
p\equiv
\begin{cases}
3\cdot5+2\equiv1\pmod8,&\gamma\text{ odd},\\
3\cdot1+2\equiv5\pmod8,&\gamma\text{ even}.
\end{cases}
$$

Hence

$$
\boxed{\gamma=2m}
$$

for some \(m\ge1\). Thus

$$
\boxed{p=3\cdot25^m+2.}
\tag{2}
$$

## 3. A first restriction on \(m\)

Since

$$
p-4=3\cdot25^m-2=P^\alpha,
$$

reducing modulo \(5\) gives

$$
P^\alpha\equiv3\pmod5.
$$

In particular,

$$
\boxed{\alpha\text{ is odd}.}
\tag{3}
$$

Now consider \(p\) modulo \(7\). Since

$$
25\equiv4\pmod7,
\qquad
4^3\equiv1\pmod7,
$$

if

$$
m\equiv1\pmod3,
$$

then

$$
p\equiv3\cdot4+2\equiv0\pmod7.
$$

But \(p>7\), contradicting the primality of \(p\). Therefore

$$
\boxed{m\not\equiv1\pmod3.}
\tag{4}
$$

There remain the residue classes \(m\equiv0,2\pmod3\).

## 4. Elimination of \(m\equiv2\pmod3\)

Suppose

$$
m\equiv2\pmod3.
$$

The \(k=4\) equation is

$$
p-1=4S^\delta,
$$

so

$$
S^\delta
=
\frac{3\cdot25^m+1}{4}.
\tag{5}
$$

Modulo \(7\),

$$
25^m\equiv4^m\equiv4^2\equiv2\pmod7,
$$

and consequently

$$
3\cdot25^m+1\equiv3\cdot2+1\equiv0\pmod7.
$$

Therefore

$$
7\mid S^\delta.
$$

Since \(S\) is prime,

$$
\boxed{S=7}.
$$

Equation (5) becomes

$$
\boxed{
4\cdot7^\delta=3\cdot25^m+1.
}
\tag{6}
$$

We now reduce (6) modulo \(19\).

Since

$$
25\equiv6\pmod{19}
$$

and \(6\) has order \(9\) modulo \(19\), while \(m\equiv2\pmod3\),
we have

$$
m\equiv2,5,8\pmod9.
$$

The corresponding values of \(6^m\) are

$$
6^2\equiv17,\qquad
6^5\equiv5,\qquad
6^8\equiv16
\pmod{19}.
$$

Hence the right-hand side of (6) can only be

$$
3\cdot17+1\equiv14,
$$

$$
3\cdot5+1\equiv16,
$$

or

$$
3\cdot16+1\equiv11
\pmod{19}.
$$

On the other hand,

$$
7^3\equiv1\pmod{19},
$$

so

$$
4\cdot7^\delta
$$

can only take the values

$$
4,\quad9,\quad6
\pmod{19}.
$$

The two sets are disjoint:

$$
\{14,16,11\}\cap\{4,9,6\}=\varnothing.
$$

This contradicts (6). Therefore

$$
\boxed{m\not\equiv2\pmod3.}
\tag{7}
$$

Combining (4) and (7),

$$
\boxed{m\equiv0\pmod3.}
$$

Thus

$$
m=3r
$$

for some \(r\ge1\), and

$$
\boxed{
\gamma=6r,
\qquad
p=3\cdot5^{6r}+2.
}
\tag{8}
$$

## Conclusion

The entire residue class

$$
p\equiv2\pmod5
$$

reduces to the single exponential family

$$
\boxed{
p=3\cdot5^{6r}+2,
\qquad r\ge1.
}
$$

The remaining prime-power conditions become

$$
3\cdot5^{6r}-2=P^\alpha,
$$

$$
\frac{3\cdot5^{6r}-1}{2}=Q^\beta,
$$

$$
\frac{3\cdot5^{6r}+1}{4}=S^\delta,
$$

with

$$
\alpha\text{ odd}.
$$

The next target is therefore to eliminate this one-parameter family using the
remaining prime-power conditions.
