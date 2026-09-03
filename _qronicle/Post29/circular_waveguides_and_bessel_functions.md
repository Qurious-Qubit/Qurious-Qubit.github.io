---
layout: post
title: "Bending the Boundaries: Circular Waveguides & Bessel Functions"
description: "What happens when you bend a waveguide into a cylinder? Let us step from Cartesian into Cylindrical coordinates and see why Bessel functions emerge."
order: 29
slug: "29"
topic: [Theory, Derivation, EM-Theory, Microwave-Engg, L3-Advanced]
images:
  - /images/qronicle/post29/image1.jpg
  - /images/qronicle/post29/image2.jpg
references:
  - name: "Microwave Engineering - David M. Pozar (Circular Waveguides)"
    link: "https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553"
  - name: "Bessel Functions and Circular Waveguides - Microwaves101"
    link: "https://www.microwaves101.com/encyclopedias/circular-waveguide"
  - name: "Fields and Waves in Communication Electronics - Ramo, Whinnery, Van Duzer"
    link: "https://www.wiley.com/en-us/Fields+and+Waves+in+Communication+Electronics%2C+3rd+Edition-p-9780471585510"
resources:
  - name: "Roots of Bessel Functions and Derivatives Table"
    link: "https://www.rfcafe.com/references/electrical/bessel-roots.htm"
  - name: "Circular Waveguide Calculator - everything RF"
    link: "https://www.everythingrf.com/rf-calculators/circular-waveguide-calculator"
---

## Shifting into Curvature

Up to this point in our journey, all our waveguides have had straight, flat walls meeting at crisp $90^\circ$ corners. Cartesian coordinates $(x, y, z)$ served us well, and simple sines and cosines easily solved the boundary conditions.

Now, imagine taking that metallic pipe and bending its cross-section into a smooth, seamless cylinder with an internal radius $a$.

Conceptually, a **Circular Waveguide** does the exact same job as a rectangular one: it is a hollow metal tube that guides electromagnetic waves via internal reflection. It has a cutoff frequency, a phase constant, phase and group velocities, and wave impedances that follow the exact same physical rules.

However, the math takes an adventurous turn! When boundaries are curved, standard sines and cosines cannot naturally describe radial fields. To solve the wave equation, we must transition to **Cylindrical Coordinates** $(r, \phi, z)$ and summon one of the most celebrated tools in mathematical physics: **Bessel Functions**.

---

## 1. The Wave Equation in Cylindrical Coordinates

In cylindrical coordinates, any point inside the pipe is defined by:
* $r$: The radial distance from the center axis ($0 \le r \le a$).
* $\phi$: The azimuthal angle around the circle ($0 \le \phi \le 2\pi$).
* $z$: The longitudinal direction of wave travel down the pipe.

Assuming wave propagation along the $+z$ axis as $e^{-j\beta z}$, the 3D Helmholtz equation expands into:

$$\frac{1}{r}\frac{\partial}{\partial r}\left(r \frac{\partial \psi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2 \psi}{\partial \phi^2} + k_c^2 \psi = 0$$

Where $\psi$ represents the longitudinal field ($E_z$ for TM modes, or $H_z$ for TE modes), and $k_c^2 = k^2 - \beta^2$ is our cutoff wavenumber.

To solve this partial differential equation, we assume that the radial behavior $R(r)$ and angular behavior $\Phi(\phi)$ act independently:

$$\psi(r, \phi) = R(r)\Phi(\phi)$$

Substitute this into our wave equation, divide by $R\Phi$, and multiply the entire equation by $r^2$:

$$\left[\frac{r}{R} \frac{d}{dr}\left(r \frac{dR}{dr}\right) + k_c^2 r^2\right] + \left[\frac{1}{\Phi} \frac{d^2\Phi}{d\phi^2}\right] = 0$$

---

## The Logic of "Summing to Zero"

Look at the equation above. It is cleanly partitioned into two brackets:
* The left bracket depends **only on radius $r$**.
* The right bracket depends **only on angle $\phi$**.

Imagine you have two independent dials in your hands: Dial 1 spins $r$, and Dial 2 spins $\phi$. 

If you turn Dial 1, the first bracket might want to change its value. But Dial 2 knows nothing about Dial 1! The only way two completely independent functions can always sum to zero for any possible combination of $r$ and $\phi$ is if **both brackets are locked to equal an unvarying constant**.

Let us set the angular bracket equal to a constant, call it $C$:

$$\frac{1}{\Phi} \frac{d^2\Phi}{d\phi^2} = C \implies \frac{d^2\Phi}{d\phi^2} = C \Phi$$

### Why Must the Constant Be Specifically $-n^2$?
We have two physical choices for the sign of constant $C$:
* **Choice A (Positive constant, e.g., $+5$):** The mathematical solution is a real exponential ($e^{\sqrt{C}\phi}$). This means as you walk around the circle, the electromagnetic field grows exponentially, shooting off to infinity! That is physically impossible.
* **Choice B (Negative constant, e.g., $-n^2$):** The mathematical solution is harmonious sines and cosines:

  $$\Phi(\phi) = A \cos(n\phi) + B \sin(n\phi)$$

Furthermore, because a circle connects back on itself after one full $360^\circ$ rotation ($2\pi$ radians), the field must satisfy the continuity condition $\Phi(\phi) = \Phi(\phi + 2\pi)$. 

This requires $n$ to be an integer: **$n = 0, 1, 2, 3\dots$**

---

## 2. Solving the Radius: Enter Bessel Functions

Now, substitute $-n^2$ back into the radial portion of the equation:

$$r^2 \frac{d^2 R}{dr^2} + r \frac{dR}{dr} + (k_c^2 r^2 - n^2)R = 0$$

This famous differential equation is known as **Bessel's Differential Equation**. Its general mathematical solution is a linear combination of two functions:

$$R(r) = C J_n(k_c r) + D Y_n(k_c r)$$

Let us understand what these two functions actually are, and why one of them must be completely eliminated:

### 1. Bessel Function of the First Kind: $J_n(x)$
The function $J_n(x)$ represents cylindrical standing waves that oscillate and slowly decay in amplitude as radius increases (much like ripples radiating outward when a stone is dropped into a pond).

Mathematically, it is defined by the infinite power series:

$$J_n(x) = \sum_{m=0}^{\infty} \frac{(-1)^m}{m! \, (m+n)!} \left(\frac{x}{2}\right)^{2m+n}$$

Let us examine how $J_n(x)$ behaves as $x \to 0$ (at the dead center of the hollow pipe, $r = 0$):
* **For $n = 0$ ($0^{\text{th}}$ order):**
  $$J_0(x) \approx 1 - \frac{x^2}{4} \implies J_0(0) = 1$$
  It has a completely finite, smooth peak at the center (just like a cosine curve $\cos(0) = 1$).
* **For $n \ge 1$ (higher orders):**
  $$J_n(x) \approx \frac{1}{n!} \left(\frac{x}{2}\right)^n \implies J_n(0) = 0$$
  It smoothly passes through zero at the center (just like a sine curve $\sin(0) = 0$).

In all cases, **$J_n(x)$ is finite, smooth, and well-behaved everywhere across the pipe**.

---

### 2. Bessel Function of the Second Kind (Neumann Function): $Y_n(x)$
The second independent solution, $Y_n(x)$ (sometimes denoted as $N_n(x)$), is defined as:

$$Y_n(x) = \frac{J_n(x) \cos(n\pi) - J_{-n}(x)}{\sin(n\pi)}$$

Now, let us look at how $Y_n(x)$ behaves as $x \to 0$ (approaching the center axis $r = 0$):
* **For $n = 0$:**
  $$Y_0(x) \approx \frac{2}{\pi} \left[ \ln\left(\frac{x}{2}\right) + \gamma \right] \quad (\text{where } \gamma \approx 0.5772)$$
  Because the natural logarithm of zero approaches negative infinity ($\ln(0) \to -\infty$), **$Y_0(x) \to -\infty$**!
* **For $n \ge 1$:**
  $$Y_n(x) \approx -\frac{(n-1)!}{\pi} \left(\frac{2}{x}\right)^n$$
  Because $x$ is in the denominator, as $x \to 0$, dividing by zero causes **$Y_n(x) \to -\infty$**!

---

### The Physics Sanity Check: Why $D$ MUST Be Set to Zero ($D = 0$)

Look at what would happen if we allowed $D \neq 0$:
Inside our hollow metallic pipe, the center axis ($r = 0$) is simply empty space (air or vacuum). There is no wire, no charge filament, and no source sitting at $r = 0$.

If $D$ were anything other than zero, the term $D Y_n(k_c r)$ would cause the electric and magnetic fields at the center of the pipe to **blow up to negative infinity ($-\infty$)**!

An infinite electromagnetic field would mean an infinite energy density:

$$u_{\text{energy}} = \frac{1}{2}\epsilon |\vec{E}|^2 + \frac{1}{2}\mu |\vec{H}|^2 \to \infty$$

The universe does not allow an empty pipe to hold infinite energy! 

Therefore, to keep our physical fields finite, continuous, and physically realistic at $r = 0$, **the coefficient $D$ must be strictly set to zero**:

$$D = 0$$

*(Note: The only time $Y_n$ is allowed in microwave engineering is in a **coaxial cable**, where a solid metal inner conductor occupies the center region from $r = 0$ to $r = a_{\text{inner}}$. In a coax, $r = 0$ is excluded from the dielectric space, so $Y_n$ can safely exist! But in a hollow circular waveguide, the center is included, so $Y_n$ is strictly forbidden).*

Setting $D = 0$ eliminates the singularity and leaves us with the clean, physical radial profile:

$$R(r) = C J_n(k_c r)$$

---

## 3. Applying Boundary Conditions at the Metal Wall ($r = a$)

Now we apply the solid metal wall boundary condition at the outer radius $r = a$:

1. **For TM Modes ($H_z = 0, E_z \neq 0$):** 
   The tangential electric field $E_z$ must drop to zero at the conducting wall:

   $$J_n(k_c a) = 0$$

   This means $k_c a$ must land precisely on a zero-crossing (root) of the Bessel function $J_n$. We call the $p$-th root of $J_n$ the number $p_{np}$:

   $$k_c = \frac{p_{np}}{a} \implies f_{c(TM)} = \frac{u \cdot p_{np}}{2\pi a}$$

2. **For TE Modes ($E_z = 0, H_z \neq 0$):** 
   The boundary condition requires the radial derivative of the magnetic field to vanish at the metal wall:

   $$J'_n(k_c a) = 0$$

   Here, $k_c a$ must land on a zero-crossing of the derivative of the Bessel function. We call this root $p'_{np}$:

   $$k_c = \frac{p'_{np}}{a} \implies f_{c(TE)} = \frac{u \cdot p'_{np}}{2\pi a}$$

---

## 4. The Toll Booth Roots & The Dominant Mode

Just like in rectangular waveguides, the mode with the **lowest absolute cutoff frequency** is the dominant mode. Since $u, 2, \pi,$ and $a$ are fixed constants, the dominant mode is strictly dictated by the **smallest root** in the math tables!

Let us look up the smallest roots:

| Mode Index $(n, p)$ | TM Root ($p_{np}$) | TE Root ($p'_{np}$) |
| :--- | :--- | :--- |
| **$(0, 1)$** | $2.405 \ (TM_{01})$ | $3.832 \ (TE_{01})$ |
| **$(1, 1)$** | $3.832 \ (TM_{11})$ | **$1.841 \ (TE_{11})$** |
| **$(2, 1)$** | $5.136 \ (TM_{21})$ | $3.054 \ (TE_{21})$ |
| **$(0, 2)$** | $5.520 \ (TM_{02})$ | $7.016 \ (TE_{02})$ |

Look at the table! The smallest number across the entire board is **$1.841$**.

This root belongs to the derivative of the first-order Bessel function, corresponding to the **$TE_{11}$ mode**.

Therefore, **$TE_{11}$ is the Dominant Mode of a circular waveguide!**

### The Degeneracy Quirk
Notice something interesting in the table? 
* The root for $TM_{11}$ is **$3.832$**.
* The root for $TE_{01}$ is also **$3.832$**.

In a circular waveguide, $TM_{11}$ and $TE_{01}$ share the exact same cutoff frequency! If you operate high enough to turn on $TE_{01}$, you will unavoidably excite $TM_{11}$ as well.

---

## Rectangular vs. Circular: The Engineering Trade-off

If rectangular waveguides are so great, why do engineers ever bother with circular waveguides?

1. **Bandwidth:** Rectangular waveguides win hands down. In a rectangular guide ($a = 2b$), the ratio between the dominant mode ($TE_{10}$) and the second mode ($TE_{20}$) is a factor of $2.0$. In a circular guide, the ratio between $TE_{11}$ ($1.841$) and the next mode $TM_{01}$ ($2.405$) is only about $1.3$. The single-mode bandwidth in a circular guide is significantly narrower!
2. **Polarization Twist:** In a rectangular waveguide, the flat vertical walls lock the polarization in place. In a circular waveguide, because the cylinder has perfect rotational symmetry, any slight dent or ovality will cause the electric field vector of the $TE_{11}$ mode to slowly rotate and twist as it travels down the pipe, causing polarization loss at the receiver.
3. **The Superpower: Rotary Joints!** 
   Imagine a high-power airport radar antenna or a satellite dish that must continuously spin $360^\circ$ to sweep the sky. You cannot spin a rectangular waveguide without mechanically ripping it apart. A circular waveguide, with its radial symmetry, is the only structure capable of acting as a low-loss **Rotary Joint**, allowing physical rotation while pumping megawatts of microwave power!

---

## Quantum Bench Insight: 3D Cavity Quantum Electrodynamics

In quantum information processing, cylindrical 3D microwave cavities machined out of ultra-pure copper or superconducting aluminum are widely utilized for **3D Circuit QED**.

Because circular cavities can be lathed with extraordinary geometric precision, they support ultra-high quality factors ($Q > 10^7$). When coupled to a superconducting transmon qubit, these cylindrical cavities serve as ultra-clean quantum memories capable of storing Schrödinger cat states and multi-photon quantum states with coherence times extending past milliseconds!

---

## Wrapping Up the Series

Over the course of these seven posts, we have demystified guided wave physics from top to bottom:
1. **Post 23:** The Hollow Pipe Paradox: Why TEM Waves Cannot Exist and the Momentum Budget.
2. **Post 24:** Deriving TE and TM Modes: Boundary Conditions and Forbidden States.
3. **Post 25:** The Zig-Zag Path: Phase Constant ($\beta$) and Internal Bouncing.
4. **Post 26:** The Relativity Illusion: Phase Velocity vs. Group Velocity ($v_p \cdot v_g = u^2$).
5. **Post 27:** The Impedance of a Box: Wave Impedance in TE vs. TM Modes.
6. **Post 28:** Dominant Modes, Degenerate Modes, and the Square Waveguide Disaster.
7. **Post 29:** Bending the Boundaries: Circular Waveguides, Bessel Functions, and Rotary Joints.

You now possess the foundational knowledge that bridges classical microwave engineering with modern quantum hardware design!
