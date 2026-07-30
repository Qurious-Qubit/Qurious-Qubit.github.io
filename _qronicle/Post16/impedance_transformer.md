---
layout: post
title: "The Shape-Shifting Wire: Deriving the Input Impedance Equation"
description: "Did you know the impedance of a cable changes depending on where you stand? Let us derive the most powerful equation in microwave engineering."
order: 16
slug: "16"
topic: [Theory, Derivation, Microwave-Engg, Quantum-Tech, L2-Intermediate]
images:
  - /images/qronicle/post16/image1.png
references:
  - name: "Lecture: Impedance Transformation and Parameter Relations (EMPossible)"
    link: "https://www.youtube.com/watch?v=y3pr_o80twc"
  - name: "Input Impedance of Transmission Line in Microwave Engineering by Engineering Funda"
    link: "https://www.youtube.com/watch?v=9efn7DQ72u8"
resources:
  - name: "What is the difference between characteristic..."
    link: "https://electronics.stackexchange.com/questions/318058/what-is-the-difference-between-characteristic-impedance-and-input-impedance-in-t"
---

## The Illusion of Fixed Impedance

In basic DC electronics, a $100 \ \Omega$ resistor is always $100 \ \Omega$, no matter how long the wire connecting it to the battery is. But in the world of high-frequency microwaves and quantum hardware, this rule completely breaks down. 

On a transmission line, **impedance is not a fixed number.** Because the voltage and current are physically traveling waves that bounce and interfere, the ratio of Voltage to Current (which is the very definition of Impedance) actually changes depending on exactly where you measure it along the wire!

Let us derive this mathematically from scratch and uncover the most powerful "cheat code" in microwave engineering.

---

## The Three Impedances

Before we dive into the math, we need to clearly define the three different impedances at play in a microwave circuit:

1. **The Load ($Z_L$):** This is the literal, physical component soldered to the end of the wire. It could be a simple Resistor, a Capacitor, an Inductor, or a complex qubit chip.
2. **The Characteristic Impedance ($Z_0$):** Imagine a transmission line that stretches out to infinity. A wave traveling down this line would never hit an end, so it would never reflect. The constant, natural resistance it feels as it travels forever is $Z_0$. 
3. **The Input Impedance ($Z_{in}$):** If we take that infinite line, chop it to a specific length $l$, and cap it with our load $Z_L$, the microwave generator at the input gets confused. The reflections from $Z_L$ travel back and mix with the forward wave. The *new, combined* impedance that the generator physically feels at the input is $Z_{in}$.

---

## Setting Up the Geometry

Let us find exactly what $Z_{in}$ is. We place our load ($Z_L$) at the physical end of our cable, which we will call position $z = 0$. 

Now, imagine we walk backward along the wire toward the microwave generator. Let us say we walk back a distance $l$. Because we moved backward from $0$, our physical position on the wire is $z = -l$.

By Ohm's law, the input impedance $Z_{in}$ at this exact spot is simply the total voltage at that spot divided by the total current:

$$Z_{in} = \frac{V(-l)}{I(-l)}$$

---

## Bringing Back the Waves

From our previous derivations, we know the total voltage and current at any point on the wire is just the sum of the forward-traveling wave and the reflected wave. 

Let us write them out. We will use the Reflection Coefficient ($\Gamma$) to represent the bouncing wave:

$$V(z) = V_0^+ (e^{-\gamma z} + \Gamma e^{+\gamma z})$$

$$I(z) = \frac{V_0^+}{Z_0} (e^{-\gamma z} - \Gamma e^{+\gamma z})$$

Now, let us plug our position ($z = -l$) into these equations. Because we are plugging in a negative length, the minus signs in the exponents will flip:

$$V(-l) = V_0^+ (e^{\gamma l} + \Gamma e^{-\gamma l})$$

$$I(-l) = \frac{V_0^+}{Z_0} (e^{\gamma l} - \Gamma e^{-\gamma l})$$

Let us divide these two to find our input impedance $Z_{in}$:

$$Z_{in} = \frac{V_0^+ (e^{\gamma l} + \Gamma e^{-\gamma l})}{\frac{V_0^+}{Z_0} (e^{\gamma l} - \Gamma e^{-\gamma l})}$$

The $V_0^+$ terms perfectly cancel out, and the $Z_0$ in the denominator flips up to the top:

$$Z_{in} = Z_0 \left[ \frac{e^{\gamma l} + \Gamma e^{-\gamma l}}{e^{\gamma l} - \Gamma e^{-\gamma l}} \right]$$

---

## Expanding the Reflection Coefficient

We already know the formula for the Reflection Coefficient at the load: $\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$. Let us plug this into our equation:

$$Z_{in} = Z_0 \left[ \frac{e^{\gamma l} + \left( \frac{Z_L - Z_0}{Z_L + Z_0} \right) e^{-\gamma l}}{e^{\gamma l} - \left( \frac{Z_L - Z_0}{Z_L + Z_0} \right) e^{-\gamma l}} \right]$$

To get rid of the ugly fraction inside the fraction, we multiply the top and bottom by $(Z_L + Z_0)$:

$$Z_{in} = Z_0 \left[ \frac{(Z_L + Z_0)e^{\gamma l} + (Z_L - Z_0)e^{-\gamma l}}{(Z_L + Z_0)e^{\gamma l} - (Z_L - Z_0)e^{-\gamma l}} \right]$$

Now, let us cleanly group all the $Z_L$ terms together and all the $Z_0$ terms together:

**Numerator:** $Z_L(e^{\gamma l} + e^{-\gamma l}) + Z_0(e^{\gamma l} - e^{-\gamma l})$

**Denominator:** $Z_L(e^{\gamma l} - e^{-\gamma l}) + Z_0(e^{\gamma l} + e^{-\gamma l})$

---

## The Lossless Magic (Enter Euler)

This is where the maths becomes beautiful. In quantum hardware, our coaxial cables are superconducting, which means they are completely lossless! Therefore, the attenuation constant is zero ($\alpha = 0$), and the propagation constant is purely imaginary ($\gamma = j\beta$). 

If we replace $\gamma$ with $j\beta$, those exponential additions and subtractions turn directly into our favourite trigonometric functions, thanks to Euler's identity!

* $e^{j\beta l} + e^{-j\beta l} = 2\cos(\beta l)$
* $e^{j\beta l} - e^{-j\beta l} = 2j\sin(\beta l)$

Let us plug these trigonometric functions back into our grouped Numerator and Denominator:

**Numerator:** $Z_L (2\cos(\beta l)) + Z_0 (2j\sin(\beta l))$

**Denominator:** $Z_L (2j\sin(\beta l)) + Z_0 (2\cos(\beta l))$

The 2's cancel out completely from the top and bottom. Finally, let us divide the top and bottom by $\cos(\beta l)$ to turn those sines into tangents:

$$Z_{in} = Z_0 \left[ \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)} \right]$$

---

## The Profound Physical Meaning

Take a long look at that final equation. It proves something incredible: **A transmission line is a mathematical Impedance Transformer.** 

If you have a $100 \ \Omega$ load ($Z_L$), but your microwave generator is sitting $l$ meters away, the generator *does not see* $100 \ \Omega$. Depending on exactly how long the cable is (the length $l$), and the frequency of the wave (which changes $\beta$), the physical length of the cable mathematically transforms that $100 \ \Omega$ into a completely different complex impedance!

Because of the $\tan(\beta l)$ function, the impedance actually spins in a circle as you walk backward along the wire, repeating perfectly every half-wavelength. 

In our next post, we will look at how quantum engineers exploit this exact tangent function to create perfect impedance matches out of thin air, using nothing but carefully cut lengths of empty wire!