---
layout: post
title: "Uncoupling the Waves: Deriving the Exact Wave Equation for Voltage and Current"
description: "How do we solve equations that depend on each other? A simple mathematical trick to decouple the Telegrapher's equations and reveal the hidden wave."
order: 11
slug: "11"
topic: [Theory, Derivation, Microwave-Engg, L2-Intermediate]
references:
  - name: "Wave Equation Solutions — Lesson 4"
    link: "https://www.youtube.com/watch?v=0vaVfslHk04&list=PL2fRCJxWQiS8qheVohpFJSl1WF6lNNBWh&index=5"
---

## The Problem of Coupled Equations

In our previous post, we successfully derived the Telegrapher's Equations for a small section of a transmission line. We found two beautiful equations governing the voltage ($V$) and current ($I$):

Equation 1 (Voltage): 
$$-\frac{\partial V}{\partial z} = R I + L \frac{\partial I}{\partial t}$$

Equation 2 (Current): 
$$-\frac{\partial I}{\partial z} = G V + C \frac{\partial V}{\partial t}$$

If we compare this with our classical EM Wave equations, we observe a very clear similarity: the spatial derivative (change over distance) is dependent on time. But there is a big catch here! 

The voltage's spatial derivative depends on the *current*, and the current's spatial derivative depends on the *voltage*. In mathematics, we call these **coupled differential equations**. Because they are tangled together, we cannot just solve them individually right away. We have to somehow uncouple them.

Let's do a little mathematical magic to separate them. To make the derivation cleaner, let's move the negative sign to the other side and write time derivatives with a prime ($'$):

$$\frac{\partial V}{\partial z} = -R I - L I'$$

$$\frac{\partial I}{\partial z} = -G V - C V'$$

---

## Decoupling the Voltage Equation

To solve for just Voltage ($V$), we need to completely eliminate Current ($I$) from the first equation. 

First, let's differentiate Equation 1 with respect to distance ($z$):

$$\frac{\partial^2 V}{\partial z^2} = -R \frac{\partial I}{\partial z} - L \frac{\partial^2 I}{\partial t \partial z}$$

Now, look at the terms on the right. We already know what $\frac{\partial I}{\partial z}$ is from Equation 2! But we also need the mixed derivative $\frac{\partial^2 I}{\partial t \partial z}$. To get that, we just differentiate Equation 2 with respect to time ($t$):

$$\frac{\partial^2 I}{\partial t \partial z} = -G V' - C V''$$

Now, we have everything we need. Let's substitute these two current expressions back into our new voltage equation:

$$\frac{\partial^2 V}{\partial z^2} = -R (-G V - C V') - L (-G V' - C V'')$$

Multiply the terms out carefully:

$$\frac{\partial^2 V}{\partial z^2} = R G V + R C V' + L G V' + L C V''$$

Group the matching derivative terms together:

$$\frac{\partial^2 V}{\partial z^2} = R G V + (R C + L G) V' + L C V''$$

And there we have it! We have successfully derived a single equation that purely describes how the voltage behaves in space and time, with no current variable in sight.

---

## The Symmetry of Current

What if we wanted to solve for Current instead? We would follow the exact same process in reverse. We would differentiate Equation 2 with respect to $z$, differentiate Equation 1 with respect to $t$, and substitute. 

If we do the math:

$$\frac{\partial^2 I}{\partial z^2} = -G (-R I - L I') - C (-R I' - L I'')$$

$$\frac{\partial^2 I}{\partial z^2} = G R I + G L I' + C R I' + L C I''$$

$$\frac{\partial^2 I}{\partial z^2} = G R I + (G L + C R) I' + L C I''$$

If we observe closely, we notice something fantastic: **both $I$ and $V$ share the exact same differential equation!** Nature is beautifully symmetric.

---

## Moving to High Frequencies: The Phasor Solution

Now, this equation looks a bit heavy with all those time derivatives ($V'$ and $V''$). But in microwave engineering, we are usually dealing with continuous AC signals oscillating at a specific frequency. 

Because the wave varies in both space ($z$) and time ($t$), we can express the current as a function of both: $I(z, t)$. To make the math easy, we separate the spatial part from the time-oscillating part using Euler's formula: 

$$I(z, t) = I_s(z) e^{j\omega t}$$

Here, $I_s(z)$ is the spatial amplitude, and $e^{j\omega t}$ handles the continuous time oscillation. When you take the time derivative of an exponential, the $j\omega$ simply comes down as a multiplier:
* First derivative: $I' = j\omega I$
* Second derivative: $I'' = (j\omega)(j\omega) I = -\omega^2 I$

Let's substitute these into our current wave equation:

$$\frac{\partial^2 I}{\partial z^2} = G R I + (G L + C R) (j\omega I) + L C (-\omega^2 I)$$

Factor out the $I$:

$$\frac{\partial^2 I}{\partial z^2} = (G R + j\omega G L + j\omega C R - \omega^2 L C) I$$

We can group these terms nicely to make it easier to read:

$$\frac{\partial^2 I}{\partial z^2} = [G(R + j\omega L) + j\omega C(R + j\omega L)] I$$

Factor out $(R + j\omega L)$:

$$\frac{\partial^2 I}{\partial z^2} = (R + j\omega L)(G + j\omega C) I$$

To make our lives easier, engineers bundle that huge chunk of constants into a single term called the **Propagation Constant squared ($\gamma^2$)**:

$$\gamma^2 = (R + j\omega L)(G + j\omega C)$$

So our massive, complicated wave equations elegantly simplify down to just:

$$\frac{\partial^2 V}{\partial z^2} = \gamma^2 V \quad \text{and} \quad \frac{\partial^2 I}{\partial z^2} = \gamma^2 I$$

We have finally arrived at the standard second-order wave equation! 

---

## The Final Wave Solution

Since both voltage and current follow the exact same second-order differential equation, they share the exact same mathematical solution. For any equation of this form, the solution for the spatial part is a combination of two exponentials:

$$V_s(z) = V_0^+ e^{-\gamma z} + V_0^- e^{+\gamma z}$$

To get the *complete* physical wave, we just multiply that time-varying $e^{j\omega t}$ back in:

$$V(z, t) = V_0^+ e^{-\gamma z} e^{j\omega t} + V_0^- e^{+\gamma z} e^{j\omega t}$$

What does this actually mean physically?
* The first term ($e^{j\omega t - \gamma z}$) represents the **forward-traveling wave**. This is the pristine microwave pulse you are sending down the cable from your signal generator to the quantum chip.
* The second term ($e^{j\omega t + \gamma z}$) represents the **reverse-traveling wave**. This is the reflection bouncing back up the cable due to impedance mismatches!

---

## The Real World: The Lossless Line

Now, let us talk practically. In quantum hardware, we use superconducting coaxial cables (like Niobium-Titanium) cooled inside a dilution refrigerator to millikelvin temperatures. Because they are superconducting, the resistance of the wire is basically zero ($R = 0$). Also, the dielectric insulators are so high-quality that there is almost zero leakage current ($G = 0$).

This creates what we call a **Lossless Line**. Let's see what happens to our propagation constant ($\gamma$) under these perfect conditions:

$$\gamma^2 = (0 + j\omega L)(0 + j\omega C)$$

$$\gamma^2 = j^2 \omega^2 L C = -\omega^2 L C$$

Taking the square root (and remembering that $j = \sqrt{-1}$):

$$\gamma = j\omega\sqrt{LC}$$

The propagation constant $\gamma$ is actually a complex number made of an attenuation constant ($\alpha$) and a phase constant ($\beta$), written as $\gamma = \alpha + j\beta$. 

By comparing the terms, we can clearly see that for a lossless line, **$\alpha = 0$** and **$\beta = \omega\sqrt{LC}$**.

This is a massive relief for quantum engineers! It mathematically proves that our microwave pulse will not lose any amplitude or energy ($\alpha = 0$) as it travels down into the fridge. It only experiences a predictable phase shift ($\beta$), which we can easily account for to execute perfect quantum logic gates.