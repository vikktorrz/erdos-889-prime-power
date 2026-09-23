# Residual Family \(p=3\cdot5^{6r}+2\)

After eliminating the residue classes

$$
p\equiv1,3,4\pmod5
$$

inside the branch

$$
d_2=2,\qquad d_3=3,\qquad d_4=4,\qquad d_5=1,
$$

the remaining case is

$$
\boxed{
p=3\cdot5^{6r}+2,
\qquad r\ge1.
}
$$

The corresponding prime-power conditions are

$$
\boxed{
3\cdot5^{6r}-2=P^\alpha
}
\tag{1}
$$

and

$$
\boxed{
\frac{3\cdot5^{6r}+1}{4}=S^\delta.
}
\tag{2}
$$

The \(k=3\) component is

$$
p-2=3\cdot5^{6r},
$$

so in the original notation

$$
\gamma=6r.
$$

## 1. The exponent \(\alpha\) is odd

Reducing (1) modulo \(5\),

$$
P^\alpha\equiv-2\equiv3\pmod5.
$$

A square modulo \(5\) is \(1\) or \(4\). Hence \(\alpha\) cannot be even:

$$
\boxed{\alpha\text{ is odd}.}
\tag{3}
$$

Moreover,

$$
3\cdot5^{6r}-2\equiv1\pmod{24},
$$

because

$$
5^{6r}\equiv1\pmod{24}.
$$

Since \(\alpha\) is odd,

$$
P^\alpha\equiv1\pmod{24}
$$

implies

$$
\boxed{P\equiv1\pmod{24}.}
$$

Together with

$$
P^\alpha\equiv3\pmod5
$$

and the oddness of \(\alpha\),

$$
P\equiv3\pmod5.
$$

Therefore

$$
\boxed{P\equiv73\pmod{120}.}
\tag{4}
$$

## 2. The residue class \(r\equiv1\pmod3\) is impossible

Modulo \(19\),

$$
5^6\equiv7\pmod{19},
$$

and

$$
7^3\equiv1\pmod{19}.
$$

If

$$
r\equiv1\pmod3,
$$

then

$$
5^{6r}\equiv7\pmod{19},
$$

so

$$
3\cdot5^{6r}-2
\equiv
3\cdot7-2
\equiv0
\pmod{19}.
$$

Thus \(19\mid P^\alpha\), forcing

$$
P=19.
$$

But \(19\equiv4\pmod5\), and \(\alpha\) is odd, so

$$
19^\alpha\equiv4\pmod5,
$$

whereas (1) is congruent to \(3\pmod5\). Contradiction.

Hence

$$
\boxed{r\not\equiv1\pmod3.}
\tag{5}
$$

## 3. The residue class \(r\equiv2\pmod5\) is impossible

Consider (2). Modulo \(61\),

$$
5^6\equiv9\pmod{61},
$$

and \(9\) has order \(5\) modulo \(61\).

If

$$
r\equiv2\pmod5,
$$

then

$$
5^{6r}\equiv9^2\equiv20\pmod{61}.
$$

Consequently,

$$
3\cdot5^{6r}+1
\equiv
3\cdot20+1
\equiv0
\pmod{61}.
$$

Since \(61\nmid4\),

$$
61\mid S^\delta,
$$

so

$$
S=61.
$$

But

$$
S^\delta
=
\frac{3\cdot5^{6r}+1}{4}
\equiv4\pmod5.
$$

On the other hand,

$$
61^\delta\equiv1\pmod5,
$$

a contradiction.

Therefore

$$
\boxed{r\not\equiv2\pmod5.}
\tag{6}
$$

## 4. Further modular exclusions

The same principle gives additional restrictions.

### Modulo \(29\)

One has

$$
5^6\equiv23\pmod{29},
$$

with \(23\) of order \(7\). For

$$
r\equiv4\pmod7,
$$

we obtain

$$
3\cdot5^{6r}-2\equiv0\pmod{29}.
$$

Thus \(P=29\). But

$$
29\equiv4\pmod5,
$$

and therefore every power of \(29\) is congruent to \(1\) or \(4\pmod5\), never \(3\). Hence

$$
\boxed{r\not\equiv4\pmod7.}
\tag{7}
$$

### Modulo \(101\)

The order of \(5^6\) modulo \(101\) is \(25\), and

$$
r\equiv3\pmod{25}
$$

gives

$$
101\mid3\cdot5^{6r}-2.
$$

Since

$$
101\equiv1\pmod5,
$$

a power of \(101\) cannot be congruent to \(3\pmod5\). Thus

$$
\boxed{r\not\equiv3\pmod{25}.}
\tag{8}
$$

### Modulo \(151\)

The order of \(5^6\) modulo \(151\) is \(25\), and

$$
r\equiv2\pmod{25}
$$

gives

$$
151\mid3\cdot5^{6r}+1.
$$

Thus \(S=151\). Since

$$
151\equiv1\pmod5,
$$

this contradicts

$$
S^\delta\equiv4\pmod5.
$$

Hence

$$
\boxed{r\not\equiv2\pmod{25}.}
\tag{9}
$$

## Current residual restrictions

Every remaining solution in this branch must satisfy

$$
\boxed{
r\not\equiv1\pmod3,
}
$$

$$
\boxed{
r\not\equiv2\pmod5,
}
$$

$$
\boxed{
r\not\equiv4\pmod7,
}
$$

$$
\boxed{
r\not\equiv3,2\pmod{25},
}
$$

together with

$$
\boxed{
P\equiv73\pmod{120}.
}
$$

These congruences do not yet eliminate the entire family. They constitute a
modular sieve for the remaining exponent \(r\).

The next objective is to determine whether the remaining residue classes can
be covered by finitely many similar prime-divisor obstructions,
