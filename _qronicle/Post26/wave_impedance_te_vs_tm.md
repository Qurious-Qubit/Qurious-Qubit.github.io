---
layout: post
title: "The Impedance of a Box: Wave Impedance in TE vs TM Modes"
description: "Why does free space have a constant 377 Ohm impedance, while a waveguide's impedance swings from zero to infinity? Let us derive wave impedance for TE and TM modes."
order: 26
slug: "26"
topic: [Theory, Derivation, Microwave-Engg, L2-Intermediate]
images:
  - /images/qronicle/post26/image1.jpg
  - /images/qronicle/post26/image2.jpg
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

In a **Transverse Electric** mode, the electric field is strictly transverse to the direction of propagation. This means there is zero longitudinal electric field along the length of the tube:

$$E_z = 0 \quad \text{and} \quad H_z \neq 0$$

If we take Maxwell's curl equations ($\nabla \times \vec{E} = -j\omega\mu \vec{H}$) and expand the spatial derivatives for a wave propagating as $e^{-j\beta z}$, we find a direct relationship between the transverse electric field and transverse magnetic field:

$$Z_{TE} = \frac{E_x}{H_y} = \frac{\omega\mu}{\beta}$$

Now, let us substitute our master equation for the phase constant ($\beta$) that we derived in Post 24:

$$\beta = \frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

Plugging this expression for $\beta$ into the denominator:

$$Z_{TE} = \frac{\omega\mu}{\frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

The angular frequency $\omega$ in the numerator and denominator cancel out cleanly:

$$Z_{TE} = \frac{u \mu}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

Remember that the wave speed in the dielectric is $u = 1/\sqrt{\mu\epsilon}$. If we multiply $u$ by $\mu$, we get:

$$u \mu = \frac{\mu}{\sqrt{\mu\epsilon}} = \sqrt{\frac{\mu}{\epsilon}} = \eta$$

Which is nothing other than the intrinsic impedance ($\eta$) of the material filling the pipe! Substituting $\eta$ gives us our final closed-form equation:

$$Z_{TE} = \frac{\eta}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

### The Physical Meaning of $Z_{TE}$:
Look at the denominator! Since the wave propagates above cutoff ($f > f_c$), the term under the square root is a fraction strictly less than $1$. 

* Because we are dividing $\eta$ by a number smaller than $1$, **$Z_{TE}$ is always strictly higher than the intrinsic impedance of free space ($Z_{TE} > \eta$)!**
* As you drop your operating frequency closer and closer to cutoff ($f \to f_c$), the denominator shrinks towards zero, causing the impedance to **shoot to infinity ($\infty$)**.
* **The Waveguide acts like an OPEN CIRCUIT at cutoff!**

---

## 2. Wave Impedance for TM Modes ($Z_{TM}$)

In a **Transverse Magnetic** mode, the magnetic field is strictly transverse to the direction of propagation. This means there is zero longitudinal magnetic field along the length of the tube:

$$H_z = 0 \quad \text{and} \quad E_z \neq 0$$

Using Maxwell's second curl equation ($\nabla \times \vec{H} = j\omega\epsilon \vec{E}$) and isolating the transverse field components, we get the dual relationship:

$$Z_{TM} = \frac{E_x}{H_y} = \frac{\beta}{\omega\epsilon}$$

Once again, substitute our master equation for $\beta$:

$$Z_{TM} = \frac{\frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}}{\omega\epsilon} = \frac{1}{u\epsilon} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

Since $u = 1/\sqrt{\mu\epsilon}$, the factor $1/(u\epsilon)$ simplifies directly:

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

In **Post 27**, we will explore **Dominant Modes, Degenerate Modes, and The Dreaded Square Waveguide Disaster**!
