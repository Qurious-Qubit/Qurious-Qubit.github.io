---
layout: post
title: "The Impedance of a Box: Wave Impedance in TE vs TM Modes"
description: "Why does free space have a constant 377 Ohm impedance, while a waveguide's impedance swings from zero to infinity? Let us derive wave impedance for TE and TM modes."
order: 27
slug: "27"
topic: [Theory, Derivation, Microwave-Engg, L2-Intermediate]
images:
  - /images/qronicle/post27/image1.jpg
  - /images/qronicle/post27/image2.jpg
references:
  - name: "Microwave Engineering - David M. Pozar (Wave Impedance)"
    link: "https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553"
  - name: "Waveguide Impedance and Matching - Microwaves101"
    link: "https://www.microwaves101.com/encyclopedias/waveguide-impedance"
  - name: "Electromagnetic Waves and Radiating Systems - Jordan & Balmain"
    link: "https://archive.org/details/electromagneticw00jord"
resources:
  - name: "Rectangular Waveguide Characteristic Impedance Formulas"
    link: "https://www.rfcafe.com/references/electrical/waveguide-impedance.htm"
  - name: "RF and Microwave Impedance Calculator - everything RF"
    link: "https://www.everythingrf.com/rf-calculators"
---

## What Does a Wave "Feel"?

Whenever an electrical signal travels through a medium, it experiences an opposition to its flow. In regular DC circuits, we call this resistance ($R$). In AC circuits and transmission lines, we call it characteristic impedance ($Z_0 = 50 \ \Omega$).

In open vacuum or air, an unbounded electromagnetic wave experiences the **Intrinsic Impedance of Free Space** ($\eta$):

$$\eta = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 377 \ \Omega \quad (\text{or } 120\pi \ \Omega)$$

Notice that $\eta$ is a fixed number. It depends purely on the physical constants of the medium (permeability $\mu$ and permittivity $\epsilon$). It does not care about frequency, shape, or boundaries.

However, the moment you force an electromagnetic wave inside a hollow metal pipe, everything changes! Because the wave bounces back and forth off the conducting walls at an angle, the forward-flowing energy sees an effective impedance that is heavily frequency-dependent and radically different depending on whether the wave is **Transverse Electric (TE)** or **Transverse Magnetic (TM)**.

Welcome to the world of **Wave Impedance** ($Z$).

---

## Defining Wave Impedance

By definition, the wave impedance ($Z$) is the ratio of the transverse electric field to the transverse magnetic field that are perpendicular to the direction of wave travel ($z$):

$$Z = \frac{E_{\text{transverse}}}{H_{\text{transverse}}} = \frac{E_x}{H_y} = -\frac{E_y}{H_x}$$

Let us systematically derive how this impedance behaves for both TE and TM modes.

---

## 1. Wave Impedance for TE Modes ($Z_{TE}$)

In a **Transverse Electric (TE)** mode, the electric field is strictly transverse to the direction of propagation. This means there is zero longitudinal electric field along the length of the tube:

$$E_z = 0 \quad \text{and} \quad H_z \neq 0$$

### The Step-by-Step Derivation from Faraday's Law
Let us look at Maxwell's curl equation for the electric field (Faraday's Law in phasor form):

$$\nabla \times \vec{E} = -j\omega\mu \vec{H}$$

Writing out the curl in Cartesian components:

$$\hat{x} \left(\frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}\right) + \hat{y} \left(\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x}\right) + \hat{z} \left(\frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y}\right) = -j\omega\mu (H_x \hat{x} + H_y \hat{y} + H_z \hat{z})$$

Because the wave travels forward along $+z$ as $e^{-j\beta z}$, every $z$-derivative brings down $-j\beta$:

$$\frac{\partial}{\partial z} = -j\beta$$

Now, let us examine the $\hat{y}$ component of this equation:

$$\frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x} = -j\omega\mu H_y$$

Substitute $\frac{\partial}{\partial z} = -j\beta$:

$$-j\beta E_x - \frac{\partial E_z}{\partial x} = -j\omega\mu H_y$$

Here is where the magic of the TE condition happens: **$E_z = 0$ everywhere!** 
Because $E_z = 0$, its spatial derivative is also zero ($\frac{\partial E_z}{\partial x} = 0$). The equation simplifies into a direct, beautiful balance between $E_x$ and $H_y$:

$$-j\beta E_x = -j\omega\mu H_y$$

Cancel $-j$ on both sides:

$$\beta E_x = \omega\mu H_y$$

Dividing both sides by $\beta H_y$ gives us the wave impedance directly:

$$Z_{TE} = \frac{E_x}{H_y} = \frac{\omega\mu}{\beta}$$

*(Similarly, looking at the $\hat{x}$ component with $E_z = 0$, we get $-(-j\beta E_y) = -j\omega\mu H_x \implies -\frac{E_y}{H_x} = \frac{\omega\mu}{\beta}$).*

---

### Two Intuitive Ways to Understand $Z_{TE} = \frac{\omega\mu}{\beta}$

If you want to understand this intuitively without getting lost in vector calculus, there are two wonderful ways to visualize it:

#### Perspective A: The Balance of Derivatives
* **Space Variation ($\beta$):** As the wave travels along $z$, the electric field changes in space at a rate dictated by the phase constant: $\frac{\partial E_x}{\partial z} \sim \beta E_x$.
* **Time Variation ($\omega\mu$):** Meanwhile, the magnetic field oscillates in time at angular frequency $\omega$, creating a time rate of change of magnetic flux: $\frac{\partial B_y}{\partial t} \sim \omega\mu H_y$.
* Faraday's law states that in a TE wave (where $E_z = 0$), the spatial rate of change of $E_x$ must directly balance the time rate of change of $H_y$:
  $$\beta E_x = \omega\mu H_y \implies \frac{E_x}{H_y} = \frac{\omega\mu}{\beta}$$
* The numerator $\omega\mu$ comes directly from the time oscillation of the magnetic field, and the denominator $\beta$ comes from the spatial progression of the electric wave!

#### Perspective B: The Zig-Zag Projection Angle
Remember from Post 25 that our guided wave is made of plane waves bouncing off the metal walls at an angle $\theta$ relative to the forward $z$-axis (where $\cos\theta = \frac{\beta}{k}$).
* In an unbounded medium, a plane wave has an intrinsic impedance $\eta = \frac{E_{\text{plane}}}{H_{\text{plane}}} = \sqrt{\mu/\epsilon}$.
* In a **TE wave**, the electric field $\vec{E}$ is purely parallel to the wall, so $100\%$ of it is transverse: $E_{\text{transverse}} = E_{\text{plane}}$.
* But the magnetic field $\vec{H}$ is tilted at the bounce angle $\theta$! Its *transverse projection* across the guide is reduced by $\cos\theta$:
  $$H_{\text{transverse}} = H_{\text{plane}} \cos\theta = H_{\text{plane}} \left(\frac{\beta}{k}\right)$$
* Therefore, the effective impedance seen looking down the guide is:
  $$Z_{TE} = \frac{E_{\text{transverse}}}{H_{\text{transverse}}} = \frac{E_{\text{plane}}}{H_{\text{plane}} \left(\frac{\beta}{k}\right)} = \frac{\eta}{\cos\theta} = \frac{\eta k}{\beta}$$
* Since $\eta = \sqrt{\mu/\epsilon}$ and $k = \omega\sqrt{\mu\epsilon}$, their product is $\eta k = \sqrt{\mu/\epsilon} \cdot \omega\sqrt{\mu\epsilon} = \omega\mu$!
* Substituting $\eta k = \omega\mu$ yields:
  $$Z_{TE} = \frac{\omega\mu}{\beta}$$

---

### Expressing $Z_{TE}$ in Terms of Cutoff Frequency

Now, let us substitute our master equation for the phase constant ($\beta$) that we derived in Post 25:

$$\beta = \frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

Plugging this expression for $\beta$ into the denominator of $Z_{TE} = \frac{\omega\mu}{\beta}$:

$$Z_{TE} = \frac{\omega\mu}{\frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}} = \frac{u \mu}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

Remember that $u = 1/\sqrt{\mu\epsilon}$. Therefore:

$$u \mu = \frac{\mu}{\sqrt{\mu\epsilon}} = \sqrt{\frac{\mu}{\epsilon}} = \eta$$

Which leaves us with the celebrated final formula for TE wave impedance:

$$Z_{TE} = \frac{\eta}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

### The Physical Meaning of $Z_{TE}$:
Look at the denominator! Since the wave propagates above cutoff ($f > f_c$), the term under the square root is a fraction strictly less than $1$. 

* Because we are dividing $\eta$ by a number smaller than $1$, **$Z_{TE}$ is always strictly higher than the intrinsic impedance of free space ($Z_{TE} > \eta$)!**
* As you drop your operating frequency closer and closer to cutoff ($f \to f_c$), the denominator shrinks towards zero, causing the impedance to **shoot to infinity ($\infty$)**.
* **The Waveguide acts like an OPEN CIRCUIT at cutoff!**

---

## 2. Wave Impedance for TM Modes ($Z_{TM}$)

In a **Transverse Magnetic (TM)** mode, the magnetic field is strictly transverse to the direction of propagation. This means there is zero longitudinal magnetic field along the length of the tube:

$$H_z = 0 \quad \text{and} \quad E_z \neq 0$$

### The Step-by-Step Derivation from Ampere's Law
Let us look at Maxwell's second curl equation (Ampere's Law in phasor form):

$$\nabla \times \vec{H} = j\omega\epsilon \vec{E}$$

Writing out the Cartesian components:

$$\hat{x} \left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z}\right) + \hat{y} \left(\frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x}\right) + \hat{z} \left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) = j\omega\epsilon (E_x \hat{x} + E_y \hat{y} + E_z \hat{z})$$

Look at the $\hat{x}$ component of this equation:

$$\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} = j\omega\epsilon E_x$$

Because it is a TM mode, **$H_z = 0$ everywhere** (so $\frac{\partial H_z}{\partial y} = 0$). And with forward propagation along $+z$, $\frac{\partial}{\partial z} = -j\beta$:

$$0 - (-j\beta H_y) = j\omega\epsilon E_x$$

$$j\beta H_y = j\omega\epsilon E_x$$

Cancel $j$ on both sides:

$$\beta H_y = \omega\epsilon E_x$$

Now, solve for the ratio of electric field to magnetic field ($\frac{E_x}{H_y}$):

$$Z_{TM} = \frac{E_x}{H_y} = \frac{\beta}{\omega\epsilon}$$

*(Similarly, the $\hat{y}$ component yields $-\frac{E_y}{H_x} = \frac{\beta}{\omega\epsilon}$).*

---

### The Intuitive Perspectives for TM Modes

Notice the mirror symmetry with our TE mode:

#### Perspective A: The Balance of Derivatives
* In a TM mode, the magnetic field's spatial variation along $z$ brings down $\beta H_y$.
* The electric field's time oscillation brings down $\omega\epsilon E_x$ (from displacement current).
* Ampere's law balances the spatial rate of change of $H_y$ with the time rate of change of $E_x$:
  $$\beta H_y = \omega\epsilon E_x \implies \frac{E_x}{H_y} = \frac{\beta}{\omega\epsilon}$$

#### Perspective B: The Zig-Zag Projection Angle
* In a TM wave, the magnetic field $\vec{H}$ is $100\%$ transverse: $H_{\text{transverse}} = H_{\text{plane}}$.
* The electric field $\vec{E}$ is tilted at the bounce angle $\theta$, so its transverse projection across the guide is reduced by $\cos\theta = \beta/k$:
  $$E_{\text{transverse}} = E_{\text{plane}} \cos\theta = E_{\text{plane}} \left(\frac{\beta}{k}\right)$$
* Therefore, the wave impedance looking down the guide is:
  $$Z_{TM} = \frac{E_{\text{transverse}}}{H_{\text{transverse}}} = \frac{E_{\text{plane}} \left(\frac{\beta}{k}\right)}{H_{\text{plane}}} = \eta \cos\theta = \eta \left(\frac{\beta}{k}\right)$$
* Since $\eta = \sqrt{\mu/\epsilon}$ and $k = \omega\sqrt{\mu\epsilon}$, the ratio is $\frac{\eta}{k} = \frac{\sqrt{\mu/\epsilon}}{\omega\sqrt{\mu\epsilon}} = \frac{1}{\omega\epsilon}$!
* Substituting $\frac{\eta}{k} = \frac{1}{\omega\epsilon}$ yields:
  $$Z_{TM} = \frac{\beta}{\omega\epsilon}$$

---

### Expressing $Z_{TM}$ in Terms of Cutoff Frequency

Now substitute our master equation for $\beta = \frac{\omega}{u} \sqrt{1 - (f_c/f)^2}$:

$$Z_{TM} = \frac{\frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}}{\omega\epsilon} = \frac{1}{u\epsilon} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

Since $u = 1/\sqrt{\mu\epsilon}$, the leading factor is:

$$\frac{1}{u\epsilon} = \frac{\sqrt{\mu\epsilon}}{\epsilon} = \sqrt{\frac{\mu}{\epsilon}} = \eta$$

This leaves us with the final closed-form expression for TM wave impedance:

$$Z_{TM} = \eta \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

### The Physical Meaning of $Z_{TM}$:
Here, the intrinsic impedance $\eta$ is *multiplied* by the square root fraction!

* Because the square root is a number less than $1$, **$Z_{TM}$ is always strictly lower than the intrinsic impedance of free space ($Z_{TM} < \eta$)!**
* As your operating frequency approaches cutoff ($f \to f_c$), the square root term plunges to zero, causing the impedance to **drop to zero ($0 \ \Omega$)**.
* **The Waveguide acts like a DEAD SHORT CIRCUIT at cutoff!**

---

## The Beautiful Duality

Look at how symmetrically nature organizes these equations:

$$Z_{TE} = \frac{\eta}{\sqrt{1 - (f_c/f)^2}} \qquad \text{and} \qquad Z_{TM} = \eta \sqrt{1 - (f_c/f)^2}$$

If you multiply them together:

$$Z_{TE} \cdot Z_{TM} = \left(\frac{\eta}{\sqrt{1 - (f_c/f)^2}}\right) \cdot \left(\eta \sqrt{1 - (f_c/f)^2}\right) = \eta^2$$

The frequency-dependent square root terms cancel out completely! 

No matter what frequency you operate at, the geometric mean of the TE and TM wave impedances inside a waveguide is always exactly equal to the intrinsic impedance of the filling medium:

$$\sqrt{Z_{TE} \cdot Z_{TM}} = \eta \approx 377 \ \Omega$$

Furthermore, if you push your frequency way up high ($f \gg f_c$), the ratio $(f_c/f)^2$ drops to zero. Both $Z_{TE}$ and $Z_{TM}$ asymptotically converge to $\eta \approx 377 \ \Omega$. This makes complete physical sense: at extremely high frequencies, the wave barely glances off the walls and behaves almost like a free-space plane wave!

---

## The Microwave and Quantum Bench Application

Why do we care so deeply about wave impedance in the lab?

When connecting a standard $50 \ \Omega$ coaxial cable from an instrument (like our Vector Network Analyzer or an Arbitrary Waveform Generator) to a rectangular waveguide or a 3D superconducting qubit readout cavity, we face an enormous impedance mismatch:
* The coax is $50 \ \Omega$.
* The waveguide $TE_{10}$ mode impedance $Z_{TE}$ typically hovers between $400 \ \Omega$ and $500 \ \Omega$.

If you simply connect them directly without proper matching, virtually all your microwave power will bounce off the junction, sending high reflections back into your instruments and spoiling your qubit readout SNR (signal-to-noise ratio). 

To solve this, microwave engineers use precision **coax-to-waveguide adapters**, tuning a tiny antenna probe's depth and placing a sliding short-circuit backwall exactly a quarter-wavelength ($\lambda_g/4$) behind the probe to achieve a flawless impedance transformation.

---

## What Lies Ahead?

We now have a complete mathematical grasp of cutoff frequencies, phase constants, velocities, and impedances. 

Now, let us put on our design engineer hats: How do we actually choose the dimensions of a rectangular waveguide? Why is the width $a$ almost universally chosen to be exactly twice the height ($a = 2b$)? And what disaster happens if you make the waveguide a perfect square?

In **Post 28**, we will explore **Dominant Modes, Degenerate Modes, and The Dreaded Square Waveguide Disaster**!
