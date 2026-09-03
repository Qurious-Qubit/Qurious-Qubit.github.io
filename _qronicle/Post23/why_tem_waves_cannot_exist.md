---
layout: post
title: "The Hollow Pipe Paradox: Why TEM Waves Cannot Exist"
description: "Why can a standard coaxial cable carry a TEM wave, but a hollow metal pipe completely chokes it? Let us understand single conductors, field loops, and the wave momentum budget."
order: 23
slug: "23"
topic: [Theory, EM-Theory, Microwave-Engg, L1-Foundational]
images:
  - /images/qronicle/post23/image1.jpg
  - /images/qronicle/post23/image2.jpg
references:
  - name: "Microwave Engineering - David M. Pozar (TEM and Guided Waves)"
    link: "https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553"
  - name: "Why TEM Modes Cannot Exist in a Waveguide - Microwaves101"
    link: "https://www.microwaves101.com/encyclopedias/waveguide-basics"
  - name: "MIT OpenCourseWare: Guided Electromagnetic Waves"
    link: "https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/"
resources:
  - name: "Field Configurations in Transmission Lines vs Waveguides"
    link: "https://www.rfcafe.com/references/electrical/waveguide-frequency-data.htm"
  - name: "Standard Rectangular Waveguide Technical Specifications"
    link: "https://www.everythingrf.com/tech-resources/waveguides-specifications"
---

## The Mystery of the Missing Wire

Whenever we want to power an appliance at home or route an audio signal, we always use a pair of conductors: a Phase and a Neutral wire, or the central core and outer braided shield of a coaxial cable. We have been taught since high school that electricity needs a closed "go-and-return" loop to flow.

However, as we push our operating frequencies into the microwave regime ($1 \text{ GHz}$ to $100 \text{ GHz}$) for radar systems or quantum computing control racks, ordinary cables begin to fail:

1. **The Skin Effect**: At gigahertz speeds, electrons refuse to travel through the bulk copper. They crowd onto an ultra-thin outer skin of the wire, causing AC resistance and ohmic heat losses to skyrocket.
2. **Dielectric Losses**: In a standard coaxial cable, the plastic insulator sitting between the inner and outer conductor gets shaken back and forth billions of times per second by the alternating electric field. It acts like a sponge, soaking up our precious microwave signal and turning it into heat.

To solve this, microwave engineers made a daring move: **they threw away the center wire and discarded the plastic insulator completely!**

What remains is a **rectangular waveguide**: simply a hollow metallic pipe made of brass or copper, enclosing pure empty space or air.

Instead of flowing electrons down a wire, we launch an electromagnetic wave directly into the empty cavity, allowing the metallic walls to act like mirrors that guide the wave forward.

In quantum computing labs, superconducting hollow cavities made of high-purity aluminium are prized because eliminating dielectric loss protects delicate qubit states like $\vert 0 \rangle$ and $\vert 1 \rangle$ from decaying into heat.

Now comes a profound question that puzzles almost every engineer when they first meet a waveguide: **Why can't a wave travel down this hollow pipe the same simple way it travels down a coaxial cable?**

---

## What on Earth is a "TEM" Mode?

In a coaxial cable, in free space, or along parallel wires, electromagnetic signals travel as a **Transverse Electromagnetic (TEM)** wave.

Let us break down what "Transverse" means in plain English:

Imagine an electromagnetic wave traveling down a pipe along the forward direction, which we call the **$z$-axis**.

* **Transverse** simply means lying flat in the cross-section perpendicular to travel—in the **$x-y$ plane**!
* In a **TEM wave**, the **Electric Field ($\vec{E}$)** points strictly across the cross-section ($E_z = 0$).
* The **Magnetic Field ($\vec{H}$)** also points strictly across the cross-section ($H_z = 0$).
* **Neither field has any component pointing forward or backward along the direction of travel ($z$).**

A TEM wave is the simplest, cleanest wave in nature. It travels at the natural speed of light, has zero cutoff frequency, and suffers zero dispersion.

So why can a coaxial cable happily carry a TEM wave, but the moment you pull the center wire out to make a hollow waveguide, **a TEM wave becomes 100% impossible?**

Let us understand the fascinating physics behind this paradox.

---

## The Single-Conductor Paradox

Let us ask a very basic question: **Where do electric field lines come from, and where do they go?**

According to Gauss's Law, electric field lines must originate on positive charges ($+$) and terminate on negative charges ($-$).

### 1. The Coaxial Cable: Two Separate Conductors
In a coaxial cable, you have **two completely separate pieces of metal**:
* The inner center wire carries a positive voltage ($+V$).
* The outer shield carries a negative / ground reference ($0 \text{ V}$).

Because there are two separate conductors, electric field lines have an easy life: they start on positive surface charges on the inner wire, shoot radially outward across the gap, and terminate on negative surface charges on the outer shield! 

Meanwhile, current flowing forward on the inner wire and returning on the outer shield creates magnetic field lines that wrap neatly around the center wire in closed concentric circles. 

Everything is transverse ($E_z = 0, H_z = 0$), and the TEM wave cruises happily down the cable.

```
       COAXIAL CABLE (TWO CONDUCTORS)
           [Outer Shield (-)]
               |  |  |  |
             <-- E-Field <--
               |  |  |  |
           [ + Inner Core + ]   <-- Supports True TEM Mode!
               |  |  |  |
             --> E-Field -->
               |  |  |  |
           [Outer Shield (-)]
```

### 2. The Hollow Waveguide: Only ONE Continuous Conductor
Now look at our rectangular waveguide. There is no inner wire. **There is only one single, continuous piece of metal forming the entire outer perimeter.**

Can electric field lines start on one wall and terminate on an opposite wall?
* In basic electrostatics, a continuous piece of solid metal is an **equipotential surface**—every single point on the metal wall is at the exact same electrical potential ($V_0$).
* If an electric field line started on the top wall and landed on the bottom wall, there would have to be a voltage difference between them! But they are part of the exact same continuous metal pipe. **You cannot have a voltage difference between a metal pipe and itself!**

Could the electric field lines avoid the walls and simply curl into closed loops floating in the empty air of the cross-section?
* Here, **Faraday's Law of Induction** blocks the door:

  $$\oint \vec{E} \cdot d\vec{l} = -\frac{\partial}{\partial t} \iint \vec{B} \cdot d\vec{A}$$

* In simple words: an electric field line can only close on itself in a loop if there is an **alternating magnetic flux punching through the center of that loop**!
* Since our proposed electric loop lies flat in the transverse $(x, y)$ cross-section, the magnetic flux would have to punch through along the **$z$-direction** ($B_z \neq 0$).
* **BUT IN A TEM WAVE, BY DEFINITION, $B_z = 0$!**
* There is no longitudinal magnetic field to punch through the loop. Therefore, Faraday's law strictly forbids electric field lines from closing on themselves!

What about magnetic field lines?
* Magnetic field lines always form closed loops ($\nabla \cdot \vec{B} = 0$).
* By **Ampere's Law**, for magnetic field lines to form closed loops in the transverse $(x, y)$ plane, there must be an electric current or an alternating electric field punching through the center:

  $$\oint \vec{H} \cdot d\vec{l} = \iint \frac{\partial \vec{D}}{\partial t} \cdot d\vec{A}$$

* But in a TEM wave, **$E_z = 0$**! And there is no central wire carrying current!

### The Trap Closes
* Transverse electric field lines cannot start or end on the walls (no second conductor).
* Transverse electric field lines cannot form closed loops (because $B_z = 0$).
* Transverse magnetic field lines cannot form closed loops (because $E_z = 0$ and no inner wire).

Therefore, if you try to enforce $E_z = 0$ and $H_z = 0$ inside a single hollow conductor, the mathematics forces **every single electric and magnetic field component to collapse to absolute zero!**

A TEM wave cannot exist inside a hollow pipe!

---

## Why Having a $z$-Component Saves the Day!

Now, observe how beautifully physics resolves this deadlock the moment we permit a field component along the $z$-axis:

### Case 1: Allow $H_z \neq 0$ (Transverse Electric, or TE Mode)
Suppose the electric field remains purely transverse ($E_z = 0$), but we allow an alternating **magnetic field along the length of the pipe ($H_z \neq 0$)**.

Suddenly, Faraday's Law is satisfied! That forward-pointing $H_z$ acts like a **magnetic axle** punching straight through the cross-section. 

Because $H_z$ punches through the transverse plane, electric field lines can now happily curl into closed loops around it! The electric field no longer needs positive or negative charges to begin or end—it forms beautiful, stable circulating loops inside the empty pipe.

This gives birth to **Transverse Electric (TE) Modes**!

### Case 2: Allow $E_z \neq 0$ (Transverse Magnetic, or TM Mode)
Suppose the magnetic field remains purely transverse ($H_z = 0$), but we allow an alternating **electric field along the length of the pipe ($E_z \neq 0$)**.

Now, Ampere's Law is satisfied! That forward-pointing $E_z$ acts like an **electric axle** (a displacement current) punching through the cross-section. 

Magnetic field lines can now happily wrap around $E_z$ in closed transverse loops! And the electric field lines themselves now start on surface charges on the metal wall, arch forward in the $z$-direction, and terminate on opposite surface charges further down the guide.

This gives birth to **Transverse Magnetic (TM) Modes**!

### What If BOTH $E_z \neq 0$ and $H_z \neq 0$ Exist?
Can both exist simultaneously? **Absolutely!** 

These are known as **Hybrid Modes** ($HE$ or $EH$ modes). They are common in optical fibers and dielectric waveguides. In simple rectangular metallic waveguides, any hybrid wave can be broken down into a linear combination of pure TE and pure TM modes because the straight metallic walls decouple the boundary conditions neatly.

---

## The Momentum Budget: Demystifying $k_c^2 = k^2 - \beta^2$

Now let us look at the famous equation that governs all guided waves:

$$k_c^2 = k^2 - \beta^2 = \omega^2\mu\epsilon - \beta^2$$

To a layman, this string of Greek letters looks intimidating, but it is simply a **household energy budget**!

Let us break down each player:

1. **The Total Budget ($k = \omega\sqrt{\mu\epsilon}$):** 
   In free space, a wave at frequency $\omega$ has a total wavenumber $k = 2\pi/\lambda$. Think of $k$ as the **total spatial momentum** nature grants the wave.
2. **The Forward Progress ($\beta$):** 
   This is the **Phase Constant**. It measures how much of that total momentum is actually driving the wave forward along the $z$-axis.
3. **The Transverse Cost ($k_c$):** 
   This is the **Cutoff Wavenumber**. Because the wave cannot be TEM and must have non-zero $E_z$ or $H_z$, it cannot travel straight! It is forced to bounce sideways between the metal walls. $k_c$ represents the portion of spatial momentum locked into bouncing across the cross-section ($x$ and $y$).

Nature balances the budget using the Pythagorean theorem:

$$\text{Total Momentum}^2 = \text{Transverse Bounce}^2 + \text{Forward Progress}^2$$

$$k^2 = k_c^2 + \beta^2 \implies k_c^2 = k^2 - \beta^2$$

### How Does This Relate to the TEM Impossibility?
In Post 24, when we expand Maxwell's curl equations, we find that the transverse electric field is given by:

$$E_x = -\frac{j}{k_c^2} \left(\beta \frac{\partial E_z}{\partial x} + \omega\mu \frac{\partial H_z}{\partial y}\right)$$

Notice that **$k_c^2$ sits right in the denominator!**

* If a wave were a true straight-traveling TEM wave, it would have zero sideways bounce: $k_c = 0$, meaning $\beta = k$.
* But if $k_c = 0$, and for TEM $E_z = 0$ and $H_z = 0$, the equation tries to compute:
  $$E_x = \frac{0}{0} \quad (\text{Indeterminate!})$$
* As our electrostatic proof showed, without two separate conductors, those transverse fields collapse to zero.
* But the moment you have a TE or TM mode, the wave pays a non-zero transverse bounce toll ($k_c > 0$). The denominator $k_c^2$ is safely non-zero, and the spatial variations ($\partial E_z/\partial x$ or $\partial H_z/\partial y$) in the numerator breathe life into healthy, propagating transverse fields!

---

## Summary & What Lies Ahead

Let us recap what we have discovered:
1. **Ordinary cables fail** at microwave frequencies due to skin effect and dielectric heating.
2. **A TEM wave cannot exist in a hollow pipe** because you need two separate conductors to sustain transverse electric fields between opposing charges without violating Faraday's or Ampere's loop laws.
3. **Allowing a $z$-component resolves the dilemma**: $H_z \neq 0$ (TE modes) allows electric loops to close, while $E_z \neq 0$ (TM modes) allows magnetic loops to close.
4. **The momentum budget** $k^2 = k_c^2 + \beta^2$ shows that a guided wave must spend part of its spatial momentum bouncing sideways ($k_c$) to satisfy boundary conditions.

Now that we understand *why* waves in a hollow pipe must be TE or TM, a new question arises: **How do we solve for the exact shape of these fields, and why are certain modes like $TM_{10}$ and $TE_{00}$ strictly forbidden while $TE_{10}$ becomes our dominant operating mode?**

In **Post 24**, we will apply boundary conditions to the Helmholtz wave equation and uncover the secrets of **Allowed vs. Forbidden Waveguide Modes**!
