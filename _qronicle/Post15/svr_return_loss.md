---
layout: post
title: "The Bumpy Ride: Standing Waves, SWR, and Return Loss"
description: "When waves collide inside a wire, they create invisible speed bumps. Let us decode SWR and Return Loss to understand how engineers measure signal quality."
order: 15
slug: "15"
topic: [Theory, Derivation, Microwave-Engg, Quantum-Tech, L2-Intermediate]
images:
  - /images/qronicle/post15/image1.webp
references:
  - name: "Reflection Coefficient — Lesson 7"
    link: "https://www.youtube.com/watch?v=6afbWc_L7x0&list=PL2fRCJxWQiS8qheVohpFJSl1WF6lNNBWh&index=8"
  - name: "Return Loss vs VSWR: Understanding Reflections in RF Systems"
    link: "https://www.rfpage.com/return-loss-vs-vswr/"
  - name: "Why Connector Return Loss Causes Signal Problems"
    link: "https://www.connectortips.com/why-connector-return-loss-causes-signal-problems/"
resources:
  - name: "Return Loss vs VSWR: Understanding Reflections in RF Systems"
    link: "https://www.rfpage.com/return-loss-vs-vswr/"
---

## The Invisible Collision

In our last post, we saw that whenever a microwave pulse hits a mismatched load (like a poorly tuned qubit or a bad connector), nature is forced to generate a **Reflection Coefficient ($\Gamma$)**. A portion of our precious signal bounces off the load and travels backward toward the source.

But what actually happens inside the wire when you have a forward-traveling wave and a backward-traveling wave existing in the exact same space at the exact same time? 

They physically crash into each other! As these two waves slide past one another, their voltages add up. 
* In some spots, the peaks perfectly align, creating a massive spike in voltage (**Constructive Interference**).
* In other spots, a peak aligns with a valley, and they cancel each other out, dropping the voltage to zero (**Destructive Interference**).

Because the waves are moving in opposite directions at the same speed, these points of maximum and minimum voltage don't actually travel. They stay frozen in place along the wire. This creates a pulsing envelope of energy known as a **Standing Wave**.

---

## Measuring the Bumps: Standing Wave Ratio (SWR)

To a microwave engineer, a standing wave is basically a series of electrical "speed bumps" along the cable. We need a simple way to measure just how bumpy the ride is. This brings us to the **Standing Wave Ratio (SWR)**.

SWR is simply the physical ratio of the absolute highest voltage peak ($V_{max}$) to the lowest voltage valley ($V_{min}$) on the line. 

Let us derive it mathematically. Let the forward voltage wave be $V^+$ and the reflected voltage wave be $V^-$. From our definition of the reflection coefficient, we know that the magnitude of the reflected wave is $\vert V^- \vert = \vert \Gamma \vert \vert V^+ \vert$.

**Finding the Maximum Voltage ($V_{max}$):**
This happens where the waves constructively interfere and their amplitudes add together:

$$V_{max} = \vert V^+ \vert + \vert V^- \vert$$

Substitute $\vert V^- \vert$ with $\vert \Gamma \vert \vert V^+ \vert$:

$$V_{max} = \vert V^+ \vert + \vert \Gamma \vert \vert V^+ \vert = \vert V^+ \vert (1 + \vert \Gamma \vert)$$

**Finding the Minimum Voltage ($V_{min}$):**
This happens where the waves destructively interfere and subtract from each other:

$$V_{min} = \vert V^+ \vert - \vert V^- \vert$$

$$V_{min} = \vert V^+ \vert - \vert \Gamma \vert \vert V^+ \vert = \vert V^+ \vert (1 - \vert \Gamma \vert)$$

**The SWR Formula:**
By definition, $SWR = V_{max} / V_{min}$.

$$SWR = \frac{\vert V^+ \vert (1 + \vert \Gamma \vert)}{\vert V^+ \vert (1 - \vert \Gamma \vert)}$$

The forward voltage $\vert V^+ \vert$ beautifully cancels out from the top and bottom, leaving us with one of the most famous equations in RF engineering:

$$SWR = \frac{1 + \vert \Gamma \vert}{1 - \vert \Gamma \vert}$$

**How to read SWR:**
* If your load is perfectly matched, $\vert \Gamma \vert = 0$. Your SWR is $1 / 1 = 1$. We call this a "1:1 ratio" (pronounced one-to-one). The line is perfectly smooth!
* If your line is completely disconnected (open circuit), $\vert \Gamma \vert = 1$. Your SWR becomes $2 / 0 = \infty$. You have massive standing waves.

---

## Talking in Power: Return Loss (RL)

While SWR is great for picturing the physical voltage bumps on the wire, quantum and RF engineers generally prefer to think in terms of **Power**, and we love using Decibels (dB). 

Instead of looking at voltage ratios, we want to know: *"How much of my input power was wasted because it bounced back?"* This metric is called **Return Loss**.

In physics, power is proportional to the square of the voltage ($P \propto V^2$).
* Incident Power: $P_{inc} \propto \vert V^+ \vert^2$
* Reflected Power: $P_{ref} \propto \vert V^- \vert^2$

The ratio of Reflected Power to Incident Power is exactly $\vert \Gamma \vert^2$:

$$\frac{P_{ref}}{P_{inc}} = \frac{\vert V^- \vert^2}{\vert V^+ \vert^2} = \vert \Gamma \vert^2$$

**The Return Loss Formula:**
We want to express this in decibels. Because it is called a "loss", engineers prefer it to be a positive number. So we take the ratio of Incident Power to Reflected Power (flipping the fraction):

$$RL = 10 \log_{10} \left( \frac{P_{inc}}{P_{ref}} \right) = 10 \log_{10} \left( \frac{1}{\vert \Gamma \vert^2} \right)$$

Using standard logarithm rules, we can pull the squared power ($2$) out to the front, and invert the fraction by adding a negative sign. This gives us our final formula:

$$RL = -20 \log_{10} \vert \Gamma \vert$$

**How to read Return Loss:**
Return Loss can be a bit counter-intuitive for beginners because **a HIGHER Return Loss is a GOOD thing!** * If $\vert \Gamma \vert = 0.1$ (meaning 10% of the voltage reflected), the Return Loss is $-20 \log_{10}(0.1) = 20 \text{ dB}$. This means the reflected power is 20 dB *weaker* than the forward power. 
* If your Return Loss is 30 dB, your reflection is incredibly tiny (only 0.1% of the power bounced back). 

---

## Why SWR Ruins Quantum Experiments

Imagine you are sending a carefully calibrated microwave pulse down into a dilution refrigerator to flip a qubit. 

If there is a bad connector causing a high SWR, a standing wave will form in the cable. What happens if your delicate qubit chip physically sits exactly at a $V_{min}$ node of that standing wave? The voltage at that specific spot is constantly canceling itself out! You will pump power into the fridge, but the qubit will barely feel the pulse. 

Even worse, all that reflected power ($P_{ref}$) has to go somewhere. It travels backward up the cable and smashes right into your expensive, room-temperature microwave generators and amplifiers. If the Return Loss is too poor (meaning the reflected power is very high), it can literally fry your control electronics!

This is why we measure SWR and Return Loss obsessively. A smooth line means safe equipment and perfectly controlled qubits.