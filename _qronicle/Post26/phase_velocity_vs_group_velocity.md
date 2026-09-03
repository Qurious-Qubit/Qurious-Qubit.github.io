---
layout: post
title: "The Relativity Illusion: Phase Velocity vs. Group Velocity"
description: "Can anything inside a waveguide travel faster than light? Let us resolve Einstein's apparent paradox and derive the elegant relationship between phase velocity and group velocity."
order: 26
slug: "26"
topic: [Theory, Derivation, EM-Theory, Microwave-Engg, L2-Intermediate]
images:
  - /images/qronicle/post26/image1.jpg
  - /images/qronicle/post26/image2.jpg
references:
  - name: "Microwave Engineering - David M. Pozar (Phase and Group Velocity)"
    link: "https://www.wiley.com/en-us/Microwave+Engineering%2C+4th+Edition-p-9780470631553"
  - name: "Phase and Group Velocity in Waveguides - MIT OCW"
    link: "https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-spring-2009/"
  - name: "Why Phase Velocity Exceeds the Speed of Light - Microwaves101"
    link: "https://www.microwaves101.com/encyclopedias/phase-velocity"
resources:
  - name: "Interactive Wave Packet and Dispersion Simulation"
    link: "https://www.falstad.com/dispersion/"
  - name: "Group Velocity and Dispersion Tutorial"
    link: "https://phys.libretexts.org/Bookshelves/University_Physics"
---

## The "Faster Than Light" Shocker

If you take a first-year electromagnetics textbook and flip to the chapter on waveguides, you will stumble upon a formula that will make your eyes pop out.

Inside a hollow metal waveguide, if you calculate the speed of the propagating wave, you get an answer that is strictly **greater than the speed of light in vacuum ($c$)**:

$$v_p > c$$

Wait a minute! Did we just casually break Albert Einstein's Theory of Special Relativity? Can a standard brass pipe purchased off a shelf in an electronics market really break the cosmic speed limit of the universe?

Don't worry—Einstein can rest peacefully in his grave. Physics is perfectly intact! 

To understand why, we have to make a crucial distinction between two fundamentally different types of speeds: **Phase Velocity ($v_p$)** and **Group Velocity ($v_g$)**.

---

## The Scissors Analogy: Understanding Phase Velocity

To see why $v_p > c$ is an optical illusion, imagine holding an enormous pair of scissors. 

Suppose the blades of the scissors are two light-years long, and you close the handles together at a normal, gentle speed. 

What happens to the point where the two sharp blades criss-cross and touch? As the angle between the closing blades approaches zero, that intersection point races forward along the length of the blades at mind-boggling speed—infinitely faster than light!

Does this intersection point violate relativity? Not at all! The intersection point is not a physical object. It has no mass, carries no energy, and carries zero information. You cannot use the intersection point of two blades to send a Morse code message to an alien in the Alpha Centauri galaxy.

Inside a rectangular waveguide, **Phase Velocity ($v_p$)** is that exact intersection point! Because plane waves are bouncing back and forth off the conducting walls at an angle, the individual wave crests intersect along the waveguide axis. That moving intersection of phase crests races forward faster than light, but it is purely a geometric artifact of the bouncing waves.

A pure, single-frequency continuous sine wave has been running since the beginning of time and will run until the end of time. It has no start, no stop, and no modulation; therefore, it conveys **zero information**.

---

## Group Velocity ($v_g$): The True Signal Speed

To actually send information—like a digital bit ($0$ or $1$), a radar pulse, or a microwave control pulse to flip a quantum qubit from state $\vert 0 \rangle$ to state $\vert 1 \rangle$—you cannot use an infinite continuous wave. You must modulate the wave, creating a finite **wave packet** or envelope.

The speed at which this modulated envelope travels down the waveguide is called the **Group Velocity ($v_g$)**. 

Because this envelope carries the actual physical energy and data, it is bound by the laws of physics. In a waveguide, the wave packet bounces back and forth along the zig-zag path we explored in Post 24. Because it has to travel along the hypotenuse of the zig-zag, its forward progression along the $z$-axis is strictly **slower** than a wave traveling straight through open space:

$$v_g < c$$

The cosmic speed limit is completely respected!

---

## Deriving the Velocities Step-by-Step

Now that the physical intuition is crystal clear, let us derive the exact equations for both velocities from first principles.

Recall our master propagation equation from Post 24:

$$\beta = \sqrt{k^2 - k_c^2}$$

Since $k = \omega/u$ and $k_c = \omega_c/u$ (where $u = 1/\sqrt{\mu\epsilon}$ is the medium's natural speed of light, and $\omega_c = 2\pi f_c$), we can factor out $\omega/u$:

$$\beta = \frac{\omega}{u} \sqrt{1 - \left(\frac{\omega_c}{\omega}\right)^2} = \frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

### 1. Deriving Phase Velocity ($v_p$)

By definition, the phase velocity is the ratio of angular frequency to the phase constant:

$$v_p = \frac{\omega}{\beta}$$

Substitute our expression for $\beta$ into the denominator:

$$v_p = \frac{\omega}{\frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

The $\omega$ in the numerator and denominator cancel out cleanly, flipping $u$ to the top:

$$v_p = \frac{u}{\sqrt{1 - \left(\frac{f_c}{f}\right)^2}}$$

**The Physics Sanity Check:** Since our wave is propagating above cutoff ($f > f_c$), the term under the square root is a fraction strictly less than $1$. Dividing $u$ by a number smaller than $1$ guarantees that **$v_p$ is always greater than $u$**! 

As $f$ drops closer and closer to the cutoff frequency $f_c$, the denominator approaches zero, and $v_p$ shoots off to infinity ($\infty$).

---

### 2. Deriving Group Velocity ($v_g$)

Group velocity is defined as the rate of change of frequency with respect to the phase constant:

$$v_g = \frac{d\omega}{d\beta}$$

Instead of taking an awkward square root derivative directly, it is much simpler to use **implicit differentiation** on our squared equation:

$$\beta^2 = \frac{\omega^2}{u^2} - k_c^2$$

Differentiate both sides with respect to $\omega$ (remembering that $k_c$ is a fixed geometric constant of the pipe, so its derivative is zero):

$$2\beta \frac{d\beta}{d\omega} = \frac{2\omega}{u^2}$$

Divide both sides by $2$ and solve for $d\beta/d\omega$:

$$\frac{d\beta}{d\omega} = \frac{\omega}{\beta u^2}$$

Since group velocity is the exact reciprocal ($v_g = d\omega/d\beta$), we simply flip the fraction:

$$v_g = \frac{\beta u^2}{\omega}$$

Now, substitute our master equation for $\beta = \frac{\omega}{u}\sqrt{1 - (f_c/f)^2}$ back into the numerator:

$$v_g = \frac{\left(\frac{\omega}{u} \sqrt{1 - \left(\frac{f_c}{f}\right)^2}\right) u^2}{\omega}$$

The $\omega$ terms cancel, and one of the $u$ terms cancels, leaving us with:

$$v_g = u \sqrt{1 - \left(\frac{f_c}{f}\right)^2}$$

**The Physics Sanity Check:** This time, $u$ is multiplied by a fraction smaller than $1$. Therefore, **$v_g$ is always strictly less than $u$**! As you approach cutoff ($f \to f_c$), the group velocity drops to zero; the wave packet slows to a dead halt.

---

## The Beautiful Synthesis

Look closely at the final expressions for Phase Velocity and Group Velocity:

$$v_p = \frac{u}{\sqrt{1 - (f_c/f)^2}} \qquad \text{and} \qquad v_g = u \sqrt{1 - (f_c/f)^2}$$

They are near-perfect mirrors of each other! If we multiply them together:

$$v_p \cdot v_g = \left(\frac{u}{\sqrt{1 - (f_c/f)^2}}\right) \cdot \left(u \sqrt{1 - (f_c/f)^2}\right)$$

The square root terms cancel out completely, yielding one of the most elegant equations in all of microwave physics:

$$v_p \cdot v_g = u^2$$

In air or vacuum ($u = c$):

$$v_p \cdot v_g = c^2$$

Isn't that wonderful? The universe maintains perfect balance: whenever the phase velocity shoots up above the speed of light, the group velocity must drop by the exact same proportion to keep the product pinned at $c^2$!

---

## Quantum Bench Insight: Dispersion & Qubit Control

In quantum experiments, we use high-speed Arbitrary Waveform Generators (AWGs) to synthesize shaped microwave pulses (like Gaussian or DRAG pulses) to perform logic gates on superconducting qubits. 

Because $v_g$ is heavily frequency-dependent near cutoff, a microwave pulse containing a range of frequencies will experience **chromatic dispersion**: different frequency components of the pulse travel at different speeds. By the time the pulse arrives at the qubit at the bottom of the dilution refrigerator, its Gaussian shape can become stretched or distorted, leading to gate errors.

To avoid this, microwave and quantum engineers operate waveguides safely far above cutoff, where the $v_g$ curve flattens out into a stable, non-dispersive highway!

---

## What Lies Ahead?

We now understand how fast waves travel down the pipe. But what resistance does a wave feel as it pushes through? 

In free space, an electromagnetic wave sees an intrinsic impedance of about $377 \ \Omega$. But inside a waveguide, the impedance completely changes depending on whether the wave is **Transverse Electric (TE)** or **Transverse Magnetic (TM)**!

In **Post 27**, we will derive the **Wave Impedance** and discover why a waveguide behaves like an open circuit at one moment and a dead short at another!
