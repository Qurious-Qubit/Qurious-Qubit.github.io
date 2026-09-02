---
layout: post
title: "Derivation of Waveguide Modes from Maxwell's Equations: Cutoff & Mode Selection"
description: "Why can't TEM waves exist in a hollow pipe? Let us derive TE and TM modes step-by-step from Maxwell's curl equations and discover why only specific modes can physically exist."
order: 23
slug: "23"
topic: [Theory, Derivation, EM-Theory, Microwave-Engg, L2-Intermediate]
images:
  - /images/qronicle/post23/image1.jpg
  - /images/qronicle/post23/image2.jpg
references:
  - name: "Microwave Engineering - David M. Pozar (Rectangular Waveguides)"
    link: "https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553"
  - name: "Waveguide Basics and Mode Derivations - Microwaves101"
    link: "https://www.microwaves101.com/encyclopedias/waveguide-basics"
  - name: "MIT OpenCourseWare: Guided Electromagnetic Waves"
    link: "https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/"
resources:
  - name: "Rectangular Waveguide Dimensions and Cutoff Frequency Table"
    link: "https://www.rfcafe.com/references/electrical/waveguide-frequency-data.htm"
  - name: "Standard Waveguide Size Specifications (WR-90, WR-42, etc.)"
    link: "https://www.everythingrf.com/tech-resources/waveguides-specifications"
---

## The Problem with Ordinary Wires

Up until now, whenever we wanted to route an electrical signal from point A to point B, we happily picked a standard copper wire or a coaxial cable. For our everyday household electronics or low-frequency audio gadgets, these cables perform their duty flawlessly. 

However, as we step into the fast-paced realm of microwave engineering and quantum control, our operating frequencies shoot straight up into the Gigahertz ($\text{GHz}$) range. At these speeds, ordinary wires begin to fail miserably:

1. **The Skin Effect**: At gigahertz frequencies, alternating current doesn't flow through the whole thickness of the conductor anymore. Electrons get crowded tightly onto the ultra-thin outer skin of the wire. This drastically shrinks the effective cross-sectional area, causing the resistance—and heat losses—to shoot through the roof.
2. **Dielectric Losses**: In a standard coaxial cable, a plastic or teflon insulator sits snugly between the center conductor and the outer shield. At microwave speeds, the rapidly flipping electric field shakes the molecules of this plastic insulator back and forth billions of times a second. The dielectric acts like a hungry sponge, soaking up our precious microwave power and turning it into waste heat. If we tried pumping kilowatt-level radar signals or delicate quantum microwave pulses through a typical small coax cable, the inner conductor would literally melt!

So, what is the neat engineering solution? We simply remove the center conductor and throw out the lossy plastic altogether!

---

## Enter the Waveguide

A rectangular waveguide is quite literally what its name suggests: a hollow, metallic rectangular pipe with width $a$ along the $x$-axis and height $b$ along the $y$-axis ($a > b$). Inside, there is zero plastic insulation and no central inner wire. It is just pure empty space (or dry air) enclosed by highly conductive metallic walls.

Instead of shoving electrons down a wire, we directly launch an electromagnetic wave into this hollow tube. The metallic walls act like shiny mirrors, repeatedly reflecting the wave and guiding it safely down the $+z$ direction. Because the interior is mostly empty space, the dielectric loss is virtually zero, and the outer metal surface area is large enough to handle immense microwave power with minimal loss.

In quantum computing labs, 3D hollow metallic cavities and waveguides are prized components. Inside dilution refrigerators, superconducting microwave cavities made of high-purity aluminium or niobium achieve quality factors ($Q$) in the millions, protecting fragile quantum states like $\vert 0 \rangle$ and $\vert 1 \rangle$ from decaying into the environment.

However, there is a deep mathematical mystery: **How do electromagnetic waves actually arrange themselves inside this metal box, and why can only certain specific "modes" survive while others are strictly forbidden?**

To answer this, we must start directly from the bedrock of electromagnetism: **Maxwell's Equations**.

---

## Why TEM Waves Cannot Exist in a Hollow Pipe

In a coaxial cable or a two-wire line, signals travel as a **Transverse Electromagnetic (TEM)** wave. In a TEM wave, both the electric field ($\vec{E}$) and magnetic field ($\vec{H}$) are purely perpendicular (transverse) to the direction of travel ($z$). There is zero longitudinal field along the direction of propagation:

$$E_z = 0 \quad \text{and} \quad H_z = 0 \quad (\text{TEM Wave})$$

Can a TEM wave travel down our hollow metallic waveguide? **Mathematically and physically, NO!**

Let us understand why using electrostatics:
If $E_z = 0$, Maxwell's divergence equation in a source-free region ($\nabla \cdot \vec{E} = 0$) simplifies strictly in the transverse plane $(x, y)$:

$$\nabla_t \cdot \vec{E}_t = \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} = 0$$

Since the electric field can be expressed as the gradient of an electric scalar potential ($\vec{E}_t = -\nabla_t \Phi$), this means the potential must satisfy the 2D **Laplace Equation**:

$$\nabla_t^2 \Phi = \frac{\partial^2 \Phi}{\partial x^2} + \frac{\partial^2 \Phi}{\partial y^2} = 0$$

Now look at the walls of our waveguide. The waveguide is a single, continuous, closed conductor. In electrostatics, a continuous conductor forms an **equipotential surface**—the entire perimeter of the metallic wall is at the exact same potential $V_0$.

According to Laplace's Uniqueness Theorem, if a closed boundary is held at a constant potential $V_0$, the only possible solution inside is that the potential is completely flat and constant everywhere:

$$\Phi(x, y) = V_0 = \text{constant}$$

Because the potential is constant everywhere, the electric field inside is:

$$\vec{E}_t = -\nabla_t \Phi = 0$$

The electric field collapses to zero everywhere! 

> **Key Takeaway:** A TEM wave requires at least **two isolated conductors** (like the inner pin and outer shield of a coax cable) so that a voltage difference can be sustained between them. In a hollow pipe with only one continuous metallic boundary, a TEM wave cannot physically exist!

Therefore, any wave traveling down a hollow waveguide **must** have a longitudinal field component along the $z$-axis:
* **Transverse Magnetic (TM) Modes:** $H_z = 0$, but $E_z \neq 0$.
* **Transverse Electric (TE) Modes:** $E_z = 0$, but $H_z \neq 0$.

---

## Expanding Maxwell's Equations

Let us place our rectangular waveguide along the $z$-axis. Assuming the wave propagates in the $+z$ direction with harmonic time dependence, the fields take the form:

$$\vec{E}(x, y, z, t) = \vec{E}(x, y) e^{j(\omega t - \beta z)} \qquad \text{and} \qquad \vec{H}(x, y, z, t) = \vec{H}(x, y) e^{j(\omega t - \beta z)}$$

Where $\omega$ is the angular frequency and $\beta$ is the forward phase constant. Because $\partial / \partial z = -j\beta$, Maxwell's two curl equations in a source-free, lossless medium ($\mu, \epsilon$) expand into:

$$\nabla \times \vec{E} = -j\omega\mu \vec{H} \qquad \text{and} \qquad \nabla \times \vec{H} = j\omega\epsilon \vec{E}$$

Writing out the Cartesian components:

$$\frac{\partial E_z}{\partial y} + j\beta E_y = -j\omega\mu H_x \qquad \text{(1)}$$

$$-j\beta E_x - \frac{\partial E_z}{\partial x} = -j\omega\mu H_y \qquad \text{(2)}$$

$$\frac{\partial H_z}{\partial y} + j\beta H_y = j\omega\epsilon E_x \qquad \text{(3)}$$

$$-j\beta H_x - \frac{\partial H_z}{\partial x} = j\omega\epsilon E_y \qquad \text{(4)}$$

By substituting (1) into (4) and (2) into (3), we can algebraically isolate and solve for every single transverse field component ($E_x, E_y, H_x, H_y$) **purely in terms of the longitudinal fields $E_z$ and $H_z$**:

$$E_x = -\frac{j}{k_c^2} \left(\beta \frac{\partial E_z}{\partial x} + \omega\mu \frac{\partial H_z}{\partial y}\right)$$

$$E_y = \frac{j}{k_c^2} \left(-\beta \frac{\partial E_z}{\partial y} + \omega\mu \frac{\partial H_z}{\partial x}\right)$$

$$H_x = \frac{j}{k_c^2} \left(\omega\epsilon \frac{\partial E_z}{\partial y} - \beta \frac{\partial H_z}{\partial x}\right)$$

$$H_y = -\frac{j}{k_c^2} \left(\omega\epsilon \frac{\partial E_z}{\partial x} + \beta \frac{\partial H_z}{\partial y}\right)$$

Where $k_c$ is the **Cutoff Wavenumber**, defined as:

$$k_c^2 = k^2 - \beta^2 = \omega^2\mu\epsilon - \beta^2$$

This is a massive mathematical breakthrough! It means we do not need to solve for all six components of the electromagnetic field independently. We only need to find the scalar field $\psi$ (which is $E_z$ for TM modes, or $H_z$ for TE modes), and all the other fields are immediately obtained through simple derivatives!

---

## The 2D Helmholtz Wave Equation & Separation of Variables

Both $E_z$ and $H_z$ must satisfy the 2D Helmholtz wave equation inside the waveguide:

$$\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2} + k_c^2 \psi = 0$$

We solve this using the method of **Separation of Variables**, assuming the solution splits into independent $x$ and $y$ functions:

$$\psi(x, y) = X(x) Y(y)$$

Substitute this into the Helmholtz equation and divide the entire equation by $X Y$:

$$\frac{1}{X} \frac{d^2 X}{dx^2} + \frac{1}{Y} \frac{d^2 Y}{dy^2} + k_c^2 = 0$$

Because $x$ and $y$ are completely independent spatial variables, the terms $\frac{1}{X} \frac{d^2 X}{dx^2}$ and $\frac{1}{Y} \frac{d^2 Y}{dy^2}$ must each equal negative constants, which we define as $-k_x^2$ and $-k_y^2$:

$$\frac{d^2 X}{dx^2} + k_x^2 X = 0 \implies X(x) = A\cos(k_x x) + B\sin(k_x x)$$

$$\frac{d^2 Y}{dy^2} + k_y^2 Y = 0 \implies Y(y) = C\cos(k_y y) + D\sin(k_y y)$$

Where the separation constants are bound by:

$$k_x^2 + k_y^2 = k_c^2$$

Now, the constants $A, B, C, D, k_x,$ and $k_y$ must be locked down by physical boundary conditions at the conducting walls. Let us do this for both TM and TE modes!

---

## Derivation of TM Modes ($H_z = 0$) & Why Certain Modes Cannot Exist

In Transverse Magnetic (TM) modes, $H_z = 0$ everywhere, and we solve for $E_z(x, y) = X(x)Y(y)$.

The boundary condition for a perfect electric conductor demands that the **tangential electric field must vanish at the walls**:
* At the side walls ($x = 0$ and $x = a$): $E_z(0, y) = 0$ and $E_z(a, y) = 0$.
* At the top and bottom walls ($y = 0$ and $y = b$): $E_z(x, 0) = 0$ and $E_z(x, b) = 0$.

Let us apply these conditions one by one:

1. **At $x = 0$:** 
   $$X(0) = A\cos(0) + B\sin(0) = A = 0$$
   Therefore, $A = 0$, leaving $X(x) = B\sin(k_x x)$.

2. **At $y = 0$:** 
   $$Y(0) = C\cos(0) + D\sin(0) = C = 0$$
   Therefore, $C = 0$, leaving $Y(y) = D\sin(k_y y)$.

3. **At $x = a$:** 
   $$X(a) = B\sin(k_x a) = 0$$
   For a non-trivial wave ($B \neq 0$), $\sin(k_x a)$ must equal zero. This forces:
   $$k_x a = m\pi \implies k_x = \frac{m\pi}{a} \quad (m = 1, 2, 3\dots)$$

4. **At $y = b$:** 
   $$Y(b) = D\sin(k_y b) = 0$$
   This forces:
   $$k_y b = n\pi \implies k_y = \frac{n\pi}{b} \quad (n = 1, 2, 3\dots)$$

Combining these, the longitudinal electric field for any $TM_{mn}$ mode is:

$$E_z(x, y) = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)$$

### The Crucial Test: Why $TM_{00}, TM_{10},$ and $TM_{01}$ CANNOT Exist!

Look closely at the sine functions in our solution:
* **What happens if $m = 0$?** 
  $$\sin\left(\frac{0 \cdot \pi x}{a}\right) = \sin(0) = 0 \implies E_z(x, y) = 0$$
* **What happens if $n = 0$?** 
  $$\sin\left(\frac{0 \cdot \pi y}{b}\right) = \sin(0) = 0 \implies E_z(x, y) = 0$$

If either $m = 0$ or $n = 0$, the longitudinal field $E_z$ collapses to absolute zero everywhere! 

Furthermore, recall our transverse equations: for TM modes ($H_z = 0$), all transverse fields ($E_x, E_y, H_x, H_y$) are directly proportional to derivatives of $E_z$. If $E_z = 0$, then **every single electric and magnetic field component in the waveguide vanishes to zero!**

> **Fundamental Rule:** For TM modes, **neither $m$ nor $n$ can be zero**! 
> Modes like $TM_{00}$, $TM_{10}$, and $TM_{01}$ are physically impossible. 
> The lowest possible TM mode that can exist in a rectangular waveguide is **$TM_{11}$** ($m=1, n=1$).

---

## Derivation of TE Modes ($E_z = 0$) & Why $TE_{10}$ Exists While $TE_{00}$ Does Not

In Transverse Electric (TE) modes, $E_z = 0$ everywhere, and we solve for $H_z(x, y) = X(x)Y(y)$.

The boundary condition requires that the tangential electric fields along the metal walls must be zero:
* At $x = 0$ and $x = a$, the tangential electric field is $E_y$. Looking at our expansion equations with $E_z = 0$:
  $$E_y = \frac{j\omega\mu}{k_c^2} \frac{\partial H_z}{\partial x} = 0 \implies \left.\frac{\partial H_z}{\partial x}\right|_{x=0, a} = 0$$
* At $y = 0$ and $y = b$, the tangential electric field is $E_x$:
  $$E_x = -\frac{j\omega\mu}{k_c^2} \frac{\partial H_z}{\partial y} = 0 \implies \left.\frac{\partial H_z}{\partial y}\right|_{y=0, b} = 0$$

Notice the fascinating difference: **For TE modes, the normal derivative of the magnetic field must vanish at the walls!**

Let us apply this to our general solution $X(x) = A\cos(k_x x) + B\sin(k_x x)$:

1. **At $x = 0$:**
   $$\frac{dX}{dx} = -A k_x \sin(k_x x) + B k_x \cos(k_x x)$$
   $$\left.\frac{dX}{dx}\right|_{x=0} = B k_x \cos(0) = B k_x = 0 \implies B = 0$$
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

### The Crucial Test: Why $TE_{10}$ CAN Exist, but $TE_{00}$ CANNOT!

Notice that because our solution uses **cosines**, setting an index to zero does NOT make the field collapse, because $\cos(0) = 1$!

* **Can the $TE_{10}$ mode ($m=1, n=0$) exist?**
  Let us plug in $m=1, n=0$:
  $$H_z(x, y) = H_0 \cos\left(\frac{\pi x}{a}\right) \cos(0) = H_0 \cos\left(\frac{\pi x}{a}\right) \neq 0$$
  Now let us check its transverse fields! Since $H_z$ varies with $x$, its derivative is non-zero:
  $$\frac{\partial H_z}{\partial x} = -H_0 \frac{\pi}{a} \sin\left(\frac{\pi x}{a}\right) \neq 0$$
  This creates a healthy, non-zero transverse electric field:
  $$E_y = \frac{j\omega\mu}{k_c^2} \frac{\partial H_z}{\partial x} = -\frac{j\omega\mu a}{\pi} H_0 \sin\left(\frac{\pi x}{a}\right)$$
  And a transverse magnetic field $H_x$! 
  **Yes, $TE_{10}$ is a completely valid physical mode!** (Similarly, $TE_{01}$ with $m=0, n=1$ is also valid).

* **What about the $TE_{00}$ mode ($m=0, n=0$)?**
  If both $m = 0$ and $n = 0$:
  $$H_z(x, y) = H_0 \cos(0) \cos(0) = H_0 = \text{constant}$$
  A spatially constant $H_z$ has zero derivatives everywhere:
  $$\frac{\partial H_z}{\partial x} = 0 \qquad \text{and} \qquad \frac{\partial H_z}{\partial y} = 0$$
  Plugging these derivatives into our transverse field equations:
  $$E_x = 0, \quad E_y = 0, \quad H_x = 0, \quad H_y = 0$$
  All transverse electric and magnetic fields vanish completely! You are left with only a static, constant longitudinal magnetic field $H_z = H_0$ with zero electric field. Such a state carries zero electromagnetic power ($P = \vec{E} \times \vec{H}^* = 0$) and cannot propagate as a wave!

> **Fundamental Rule:** For TE modes, **$m$ or $n$ can be zero, but they CANNOT both be zero simultaneously ($m=n=0$ is forbidden)**!
> Modes like $TE_{10}$ and $TE_{01}$ are fully allowed, but $TE_{00}$ cannot exist.

---

## Mode Summary & The Cutoff Frequency ($f_c$)

Now we have a complete picture of which modes are physically allowed:

| Mode Type | Field Solution | Allowed Mode Numbers | Forbidden Modes | Lowest Mode |
| :--- | :--- | :--- | :--- | :--- |
| **TM Modes** | $E_z = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)$ | $m \ge 1, \ n \ge 1$ | $TM_{00}, TM_{10}, TM_{01}$ | **$TM_{11}$** |
| **TE Modes** | $H_z = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right)$ | $m \ge 0, \ n \ge 0$ (not both 0) | $TE_{00}$ | **$TE_{10}$** (if $a > b$) |

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

By grounding ourselves in Maxwell's equations, we have uncovered the fundamental physics of rectangular waveguides:
1. **TEM waves cannot exist** in a single hollow conductor because the equipotential boundary forces $\vec{E} = 0$.
2. All transverse fields are derived from the longitudinal fields $E_z$ and $H_z$.
3. **$TM_{00}, TM_{10},$ and $TM_{01}$ cannot exist** because boundary conditions force sines, which collapse to zero if either index is zero. The lowest TM mode is $TM_{11}$.
4. **$TE_{00}$ cannot exist** because constant $H_z$ yields zero transverse fields, but **$TE_{10}$ and $TE_{01}$ are fully valid** because cosines remain non-zero ($\cos(0) = 1$).
5. For $a > b$, **$TE_{10}$ has the lowest cutoff frequency ($f_c = u / 2a$)** and is the fundamental dominant mode.

Now that we know the mathematical roots of these modes, how do these waves actually move down the tube? In **Post 24**, we will follow the wave's internal reflections, unveiling the **Zig-Zag Path** and the **Phase Constant ($\beta$)**!
