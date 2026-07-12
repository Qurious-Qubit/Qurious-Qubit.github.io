---
layout: post
title: "The Characteristic Impedance: Where Wires Meet Waves"
description: "Since electrical signals act like waves, do they experience impedance just like EM waves in space? Let's derive the Characteristic Impedance from scratch."
order: 12
slug: "12"
topic: [Theory, Derivation, Microwave-Engg, L2-Intermediate]
references:
  - name: "Characteristic Impedance — Lesson 5"
    link: "https://www.youtube.com/watch?v=cAsg4PeolEw&list=PL2fRCJxWQiS8qheVohpFJSl1WF6lNNBWh&index=6"
---

## A Fascinating Similarity

In our previous posts, we saw that the voltage and current in a transmission line perfectly obey the exact same differential wave equations as Electromagnetic waves in free space. 

Now, if you remember our discussion on [Intrinsic Impedance](https://qurious-qubit.github.io/qronicle/post-6/), we saw that when an EM wave travels through a medium, the ratio of the Electric Field ($\mathbf{E}$) to the Magnetic Field ($\mathbf{H}$) is a constant value ($\eta$). 

Since Voltage ($V$) is logically analogous to the E-field, and Current ($I$) is analogous to the H-field, we can guess that there must be a similar constant ratio between $V$ and $I$ as the wave travels down the wire. Let's not just assume it, though. Let's check that mathematically!

---

## Setting Up the Total Space-Time Wave

Let's look at just the forward-traveling wave. To really understand how the derivatives work, we need to look at the complete wave that depends on both space ($z$) and time ($t$). 

From our last post, we know the forward-moving current and voltage look like this:

$$I(z, t) = I_0 e^{-\gamma z} e^{j\omega t}$$

$$V(z, t) = V_0 e^{-\gamma z} e^{j\omega t}$$

Notice that $V_0$ and $I_0$ are not just static constants—they are the initial amplitudes of a time-varying field! The $e^{-\gamma z}$ part tells us how the wave changes as it moves through space, and the $e^{j\omega t}$ part tells us how it oscillates in time.

Now, let's bring back our very first Telegrapher's Equation (the Voltage Equation) that we derived earlier:

$$-\frac{\partial V}{\partial z} = R I + L \frac{\partial I}{\partial t}$$

---

## The Derivation

Let's plug our total space-time wave equations into this Telegrapher's equation. 

First, let's take the spatial derivative of the voltage ($\frac{\partial V}{\partial z}$). Because we are differentiating with respect to $z$, the time part ($e^{j\omega t}$) stays exactly the same, and the derivative of $e^{-\gamma z}$ simply brings down a $-\gamma$:

$$-\frac{\partial V}{\partial z} = -(-\gamma V_0 e^{-\gamma z} e^{j\omega t}) = \gamma V_0 e^{-\gamma z} e^{j\omega t}$$

Next, let's look at the right side of the equation. We need to take the time derivative ($\frac{\partial I}{\partial t}$) of our current. Because we are differentiating with respect to time ($t$), the spatial part ($e^{-\gamma z}$) is untouched, and taking the derivative of $e^{j\omega t}$ pulls out a $j\omega$:

$$R(I_0 e^{-\gamma z} e^{j\omega t}) + L(j\omega I_0 e^{-\gamma z} e^{j\omega t})$$

Now, let's equate both sides:

$$\gamma V_0 e^{-\gamma z} e^{j\omega t} = I_0 e^{-\gamma z} e^{j\omega t} R + j\omega L I_0 e^{-\gamma z} e^{j\omega t}$$

Notice that the entire wave term ($e^{-\gamma z} e^{j\omega t}$) is common everywhere. We can beautifully cancel it out from both sides, leaving only the amplitudes:

$$\gamma V_0 = I_0 (R + j\omega L)$$

---

## Defining the Characteristic Impedance ($Z_0$)

We are looking for the ratio of Voltage to Current ($V_0 / I_0$). Let's rearrange our equation to find it:

$$\frac{V_0}{I_0} = \frac{R + j\omega L}{\gamma}$$

This ratio is exactly what we call the **Characteristic Impedance ($Z_0$)**. But we can simplify this further. Do you remember what the propagation constant ($\gamma$) is from our previous derivation? 

$$\gamma^2 = (R + j\omega L)(G + j\omega C)$$

Which means $\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$. Let's substitute this into our $Z_0 equation:

$$Z_0 = \frac{R + j\omega L}{\sqrt{(R + j\omega L)(G + j\omega C)}}$$

To clean this up, we can write the numerator as $\sqrt{(R + j\omega L)^2}$:

$$Z_0 = \sqrt{ \frac{(R + j\omega L)^2}{(R + j\omega L)(G + j\omega C)} }$$

The $(R + j\omega L)$ term in the top and bottom perfectly cancels out, leaving us with the final, elegant formula:

$$Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}}$$

---

## The Lossless Reality

Just like we did in the last post, let's see what happens in a perfect, lossless superconducting cable inside a quantum dilution refrigerator. 

Because the line is lossless, the resistance is zero ($R = 0$) and the conductance leakage is zero ($G = 0$). If we plug those into our new formula:

$$Z_0 = \sqrt{\frac{0 + j\omega L}{0 + j\omega C}} = \sqrt{\frac{j\omega L}{j\omega C}}$$

The $j\omega$ terms cancel out, and we are left with:

$$Z_0 = \sqrt{\frac{L}{C}}$$

It is absolutely fascinating! Look at how beautifully nature mirrors itself. 

For an Electromagnetic wave in free space, the Intrinsic Impedance is $\eta = \sqrt{\frac{\mu}{\epsilon}}$ (Permeability over Permittivity). 
For an electrical wave traveling in a wire, the Characteristic Impedance is $Z_0 = \sqrt{\frac{L}{C}}$ (Inductance over Capacitance). 

We have just proven that sending a microwave pulse down a coaxial cable is fundamentally the exact same physics as shining a beam of light through space!