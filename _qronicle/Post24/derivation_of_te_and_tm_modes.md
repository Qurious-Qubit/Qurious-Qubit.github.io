---
layout: post
title: "Deriving Waveguide Modes: Boundary Conditions & Forbidden States"
description: "Why can't TM01 or TE00 exist? Let us derive TE and TM modes step-by-step from Maxwell's curl equations and uncover why boundary conditions strictly dictate allowed modes."
order: 24
slug: "24"
topic: [Theory, Derivation, EM-Theory, Microwave-Engg, L2-Intermediate]
images:
  - /images/qronicle/post24/image1.jpg
  - /images/qronicle/post24/image2.jpg
references:
  - name: "Microwave Engineering - David M. Pozar (Rectangular Waveguides)"
    link: "https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553"
  - name: "Waveguide Modes and Field Derivations - Microwaves101"
    link: "https://www.microwaves101.com/encyclopedias/waveguide-modes"
  - name: "MIT OpenCourseWare: Guided Electromagnetic Waves"
    link: "https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/"
resources:
  - name: "Rectangular Waveguide Dimensions and Cutoff Frequency Table"
    link: "https://www.rfcafe.com/references/electrical/waveguide-frequency-data.htm"
  - name: "Standard Waveguide Size Specifications (WR-90, WR-42, etc.)"
    link: "https://www.everythingrf.com/tech-resources/waveguides-specifications"
---

## The Stage is Set

In Post 23, we solved a fundamental paradox: we discovered that a hollow metal pipe cannot support a TEM wave because a single continuous conductor cannot maintain transverse electric fields without violating Faraday's and Ampere's loop laws. 

To survive inside the metallic pipe, waves must have a component pointing along the direction of travel ($z$):
* **Transverse Magnetic (TM) Modes:** $H_z = 0$, but $E_z \neq 0$.
* **Transverse Electric (TE) Modes:** $E_z = 0$, but $H_z \neq 0$.

Now comes the next big revelation: **Can we just pick any arbitrary integers $(m, n)$ for these modes?** 

Why do microwave textbooks say that $TE_{10}$ and $TM_{11}$ exist, but modes like $TM_{10}$, $TM_{01}$, and $TE_{00}$ are completely impossible? 

Let us derive the mathematics step-by-step from Maxwell's equations and uncover why the boundary conditions strictly forbid certain modes while crowning others!

---

## 1. Expanding Maxwell's Curl Equations

Consider a rectangular waveguide aligned along the $z$-axis with width $a$ along the $x$-axis and height $b$ along the $y$-axis ($a > b$). 

Assuming the wave travels in the $+z$ direction with harmonic time dependence, the fields propagate as:

$$\vec{E}(x, y, z, t) = \vec{E}(x, y) e^{j(\omega t - \beta z)} \qquad \text{and} \qquad \vec{H}(x, y, z, t) = \vec{H}(x, y) e^{j(\omega t - \beta z)}$$

Where $\omega$ is the angular frequency and $\beta$ is the forward phase constant. Because $\partial / \partial z = -j\beta$, Maxwell's curl equations ($\nabla \times \vec{E} = -j\omega\mu \vec{H}$ and $\nabla \times \vec{H} = j\omega\epsilon \vec{E}$) expand into Cartesian components:

$$\frac{\partial E_z}{\partial y} + j\beta E_y = -j\omega\mu H_x \qquad \text{(1)}$$

$$-j\beta E_x - \frac{\partial E_z}{\partial x} = -j\omega\mu H_y \qquad \text{(2)}$$

$$\frac{\partial H_z}{\partial y} + j\beta H_y = j\omega\epsilon E_x \qquad \text{(3)}$$

$$-j\beta H_x - \frac{\partial H_z}{\partial x} = j\omega\epsilon E_y \qquad \text{(4)}$$

Notice how beautifully coupled these equations are! By substituting (1) into (4) and (2) into (3), we can algebraically isolate and express **all four transverse components ($E_x, E_y, H_x, H_y$) solely in terms of the longitudinal components $E_z$ and $H_z$**:

$$E_x = -\frac{j}{k_c^2} \left(\beta \frac{\partial E_z}{\partial x} + \omega\mu \frac{\partial H_z}{\partial y}\right)$$

$$E_y = \frac{j}{k_c^2} \left(-\beta \frac{\partial E_z}{\partial y} + \omega\mu \frac{\partial H_z}{\partial x}\right)$$

$$H_x = \frac{j}{k_c^2} \left(\omega\epsilon \frac{\partial E_z}{\partial y} - \beta \frac{\partial H_z}{\partial x}\right)$$

$$H_y = -\frac{j}{k_c^2} \left(\omega\epsilon \frac{\partial E_z}{\partial x} + \beta \frac{\partial H_z}{\partial y}\right)$$

Where $k_c^2 = k^2 - \beta^2 = \omega^2\mu\epsilon - \beta^2$ is our cutoff wavenumber (the transverse momentum budget from Post 23).

This is a tremendous simplification! It means we do not need to solve for all six components of the electromagnetic field. **We only need to solve for the scalar longitudinal field ($E_z$ or $H_z$), and every other field is automatically generated through simple derivatives!**

---

## 2. The 2D Helmholtz Equation & Separation of Variables

Inside the waveguide, the longitudinal field $\psi$ (representing $E_z$ or $H_z$) must satisfy the 2D Helmholtz wave equation:

$$\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2} + k_c^2 \psi = 0$$

To solve this, we use the method of **Separation of Variables**, assuming the solution splits into independent $x$ and $y$ functions:

$$\psi(x, y) = X(x) Y(y)$$

Substituting this into the Helmholtz equation and dividing by $X Y$:

$$\frac{1}{X} \frac{d^2 X}{dx^2} + \frac{1}{Y} \frac{d^2 Y}{dy^2} + k_c^2 = 0$$

Because $x$ and $y$ can vary completely independently, each term must equal an unvarying constant:

$$\frac{d^2 X}{dx^2} + k_x^2 X = 0 \implies X(x) = A\cos(k_x x) + B\sin(k_x x)$$

$$\frac{d^2 Y}{dy^2} + k_y^2 Y = 0 \implies Y(y) = C\cos(k_y y) + D\sin(k_y y)$$

Where the separation constants satisfy:

$$k_x^2 + k_y^2 = k_c^2$$

Now, the constants $A, B, C, D, k_x,$ and $k_y$ must be locked down by physical boundary conditions at the conducting walls.

---

## 3. Deriving TM Modes ($H_z = 0$) & The Forbidden TM States

In Transverse Magnetic (TM) modes, $H_z = 0$ everywhere, and we solve for $E_z(x, y) = X(x)Y(y)$.

A fundamental law of electromagnetics states that an electric field parallel (tangential) to a perfect conductor must drop to zero right at the metallic surface:
* At the left and right walls ($x = 0$ and $x = a$): $E_z(0, y) = 0$ and $E_z(a, y) = 0$.
* At the bottom and top walls ($y = 0$ and $y = b$): $E_z(x, 0) = 0$ and $E_z(x, b) = 0$.

Let us apply these conditions:

1. **At $x = 0$:**
   $$X(0) = A\cos(0) + B\sin(0) = A = 0$$
   Therefore, $A = 0$, leaving $X(x) = B\sin(k_x x)$.

2. **At $y = 0$:**
   $$Y(0) = C\cos(0) + D\sin(0) = C = 0$$
   Therefore, $C = 0$, leaving $Y(y) = D\sin(k_y y)$.

3. **At $x = a$:**
   $$X(a) = B\sin(k_x a) = 0$$
   For a non-zero wave ($B \neq 0$), $\sin(k_x a)$ must be zero:
   $$k_x a = m\pi \implies k_x = \frac{m\pi}{a} \quad (m = 1, 2, 3\dots)$$

4. **At $y = b$:**
   $$Y(b) = D\sin(k_y b) = 0 \implies k_y = \frac{n\pi}{b} \quad (n = 1, 2, 3\dots)$$

Combining these, the longitudinal electric field for any $TM_{mn}$ mode is:

$$E_z(x, y) = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)$$

### The Big Mystery: Why Can't $TM_{00}, TM_{10},$ or $TM_{01}$ Exist?

Look at the sine functions in our solution:
* **What if $m = 0$?** 
  $$\sin\left(\frac{0 \cdot \pi x}{a}\right) = \sin(0) = 0 \implies E_z(x, y) = 0$$
* **What if $n = 0$?** 
  $$\sin\left(\frac{0 \cdot \pi y}{b}\right) = \sin(0) = 0 \implies E_z(x, y) = 0$$

If either $m = 0$ or $n = 0$, the longitudinal field $E_z$ collapses to zero everywhere!

Remember our transverse equations: for TM modes ($H_z = 0$), all transverse fields ($E_x, E_y, H_x, H_y$) are calculated by taking derivatives of $E_z$. If $E_z = 0$, **then every single electric and magnetic field inside the waveguide vanishes to zero!**

> **Rule for TM Modes:** **Neither $m$ nor $n$ can be zero ($m \ge 1$ and $n \ge 1$)**! 
> Modes like $TM_{00}$, $TM_{10}$, and $TM_{01}$ are mathematically and physically impossible. 
> The lowest possible TM mode that can exist in a rectangular waveguide is **$TM_{11}$**!

---

## 4. Deriving TE Modes ($E_z = 0$) & Why $TE_{10}$ Exists While $TE_{00}$ Does Not

In Transverse Electric (TE) modes, $E_z = 0$ everywhere, and we solve for $H_z(x, y) = X(x)Y(y)$.

The boundary condition requires that the tangential electric fields along the metal walls must be zero:
* At $x = 0$ and $x = a$, the tangential electric field is $E_y$. Looking at our expansion equations with $E_z = 0$:
  $$E_y = \frac{j\omega\mu}{k_c^2} \frac{\partial H_z}{\partial x} = 0 \implies \left.\frac{\partial H_z}{\partial x}\right|_{x=0, a} = 0$$
* At $y = 0$ and $y = b$, the tangential electric field is $E_x$:
  $$E_x = -\frac{j\omega\mu}{k_c^2} \frac{\partial H_z}{\partial y} = 0 \implies \left.\frac{\partial H_z}{\partial y}\right|_{y=0, b} = 0$$

Notice the key difference: **For TE modes, the normal derivative of the magnetic field must vanish at the conducting walls!**

Applying this to our general solution:

1. **At $x = 0$:**
   $$\left.\frac{dX}{dx}\right|_{x=0} = -A k_x \sin(0) + B k_x \cos(0) = B k_x = 0 \implies B = 0$$
   Therefore, $B = 0$, leaving $X(x) = A\cos(k_x x)$.

2. **At $y = 0$:**
   $$\left.\frac{dY}{dy}\right|_{y=0} = D k_y = 0 \implies D = 0$$
   Therefore, $D = 0$, leaving $Y(y) = C\cos(k_y y)$.

3. **At $x = a$:**
   $$\left.\frac{dX}{dx}\right|_{x=a} = -A k_x \sin(k_x a) = 0 \implies k_x = \frac{m\pi}{a} \quad (m = 0, 1, 2, 3\dots)$$

4. **At $y = b$:**
   $$\left.\frac{dY}{dy}\right|_{y=b} = -C k_y \sin(k_y b) = 0 \implies k_y = \frac{n\pi}{b} \quad (n = 0, 1, 2, 3\dots)$$

Combining these, the longitudinal magnetic field for any $TE_{mn}$ mode is:

$$H_z(x, y) = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right)$$

### The Big Mystery: Why Can $TE_{10}$ and $TE_{01}$ Exist, but $TE_{00}$ Cannot?

Notice that because our solution uses **cosines**, setting an index to zero does NOT kill the field, because $\cos(0) = 1$!

* **Can the $TE_{10}$ mode ($m=1, n=0$) exist?**
  Let us plug in $m=1, n=0$:
  $$H_z(x, y) = H_0 \cos\left(\frac{\pi x}{a}\right) \cos(0) = H_0 \cos\left(\frac{\pi x}{a}\right) \neq 0$$
  Now check its transverse fields! Because $H_z$ varies with $x$, its derivative is non-zero:
  $$\frac{\partial H_z}{\partial x} = -H_0 \frac{\pi}{a} \sin\left(\frac{\pi x}{a}\right) \neq 0$$
  This non-zero derivative creates a healthy transverse electric field:
  $$E_y = \frac{j\omega\mu}{k_c^2} \frac{\partial H_z}{\partial x} = -\frac{j\omega\mu a}{\pi} H_0 \sin\left(\frac{\pi x}{a}\right)$$
  And a corresponding transverse magnetic field $H_x$! 
  **Yes, $TE_{10}$ is a completely valid, propagating physical mode!** (Similarly, $TE_{01}$ with $m=0, n=1$ is also valid).

* **What about the $TE_{00}$ mode ($m=0, n=0$)?**
  If both $m = 0$ and $n = 0$:
  $$H_z(x, y) = H_0 \cos(0) \cos(0) = H_0 = \text{constant}$$
  A spatially constant $H_z$ has zero derivatives everywhere:
  $$\frac{\partial H_z}{\partial x} = 0 \qquad \text{and} \qquad \frac{\partial H_z}{\partial y} = 0$$
  Plugging these zero derivatives into our transverse equations:
  $$E_x = 0, \quad E_y = 0, \quad H_x = 0, \quad H_y = 0$$
  All transverse electric and magnetic fields vanish completely! You are left with only a static, constant longitudinal magnetic field $H_z = H_0$ with zero electric field. A field with zero electric field cannot carry electromagnetic power ($P = \vec{E} \times \vec{H}^* = 0$) and cannot propagate as a wave!

> **Rule for TE Modes:** **$m$ or $n$ can be zero, but they CANNOT both be zero simultaneously ($m=n=0$ is forbidden)**!
> Modes like $TE_{10}$ and $TE_{01}$ are fully allowed, but $TE_{00}$ is physically impossible.

---

## 5. Mode Summary & The Cutoff Frequency ($f_c$)

Let us summarize our findings in a clear master table:

| Mode Family | Field Formula | Allowed Indices | Strictly Forbidden Modes | Lowest Allowed Mode |
| :--- | :--- | :--- | :--- | :--- |
| **TM Modes** | $E_z = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)$ | $m \ge 1, \ n \ge 1$ | $TM_{00}, \ TM_{10}, \ TM_{01}$ | **$TM_{11}$** |
| **TE Modes** | $H_z = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right)$ | $m \ge 0, \ n \ge 0$ (not both 0) | $TE_{00}$ | **$TE_{10}$** (for $a > b$) |

Using our separation constants $k_x = m\pi/a$ and $k_y = n\pi/b$, the cutoff wavenumber is:

$$k_c^2 = k_x^2 + k_y^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$

Since $k_c = \omega_c / u = 2\pi f_c / u$, we divide by $2\pi$ and multiply by $u$ to obtain the master **Cutoff Frequency Formula**:

$$f_c = \frac{u}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

### Crown Jewel: Why $TE_{10}$ is the Dominant Mode
In standard rectangular waveguides, we intentionally design the broader width $a$ to be larger than the height $b$ ($a > b$, typically $a = 2b$).

Let us compare the lowest cutoff frequencies:
* For $TE_{10}$: $f_{c(10)} = \frac{u}{2a}$
* For $TE_{01}$: $f_{c(01)} = \frac{u}{2b}$
* For $TM_{11}$: $f_{c(11)} = \frac{u}{2}\sqrt{\left(\frac{1}{a}\right)^2 + \left(\frac{1}{b}\right)^2}$

Because $a > b$, the fraction $1/a$ is strictly smaller than $1/b$, making **$f_{c(10)}$ the lowest cutoff frequency of any mode in the entire waveguide!**

This mode with the lowest cutoff frequency is crowned the **Dominant Mode**. It is the very first wave allowed through the "toll booth" as frequency increases from zero.

---

## Summary & What Lies Ahead

By applying physical boundary conditions to Maxwell's equations, we have unlocked the secrets of guided waves:
1. **$TM_{00}, TM_{10},$ and $TM_{01}$ cannot exist** because boundary conditions force sines, which collapse to zero if either index is zero. The lowest TM mode is $TM_{11}$.
2. **$TE_{00}$ cannot exist** because constant $H_z$ yields zero transverse fields, but **$TE_{10}$ and $TE_{01}$ are fully valid** because cosines remain non-zero ($\cos(0) = 1$).
3. For $a > b$, **$TE_{10}$ has the lowest cutoff frequency ($f_c = u / 2a$)** and is our fundamental operating mode.

Now that we know the exact field shapes and why specific modes exist, how does the wave actually move down the tube? 

In **Post 25**, we will follow the wave's internal reflections, uncovering the **Zig-Zag Path** and the **Phase Constant ($\beta$)**!
