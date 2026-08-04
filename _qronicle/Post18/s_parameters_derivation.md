---
layout: post
title: "The Scattering Matrix: Decoding S-Parameters Step-by-Step"
description: "How do we describe complex microwave components like amplifiers and filters? We throw away voltage and current, and introduce S-Parameters to track our bouncing waves."
order: 18
slug: "18"
topic: [Theory, Derivation, Microwave-Engg, Quantum-Tech, L3-Advanced]
images:
  - /images/qronicle/post18/image1.jpg
references:
  - name: "Calculating S-Parameters — Lesson 3"
    link: "https://www.youtube.com/watch?v=pdz_G8vjbb8"
  - name: "S Parameters Explained"
    link: "https://www.youtube.com/watch?v=-Pi0UbErHTY"
  - name: "What is a Vector Network Analyzer (VNA)?"
    link: "https://www.youtube.com/watch?v=Sb3q8f0NBZc&t=23s"
  - name: "How a VNA Works"
    link: "https://youtu.be/15-hd_JjmYY?si=N_BkPPA7Lyj0KBoh"
  - name: "Vector Network Analyzer Basics"
    link: "https://youtu.be/bLfbg2p7PaE?si=xaboAAdiBlUJz4uF"
resources:
  - name: "S-Parameters Matrix Visualization"
    link: "https://i.ytimg.com/vi/-Pi0UbErHTY/maxresdefault.jpg"
---

## The Problem with Voltage and Current

Up until now, we have talked about a single transmission line hitting a single load. But what happens when we insert a component *in the middle* of the line? Think of a microwave amplifier, a bandpass filter, or a quantum processor chip. These devices have an **Input (Port 1)** and an **Output (Port 2)**. We call this a "2-Port Network".

In low-frequency electronics, we would just measure the total Voltage and total Current at each port. But at microwave frequencies, measuring total voltage is nearly impossible because of standing waves—the voltage literally changes depending on exactly where you place your probe!

Instead of measuring the *total* voltage, microwave engineers measure the **Traveling Waves**. We track exactly how much wave energy is going *into* a port, and how much is bouncing *out* of it. This is the foundation of the **Scattering Matrix (S-Parameters)**.

---

## Defining the Waves: 'a' and 'b'

To keep the maths from getting overwhelming, we assign simple letters to our waves. We use **$a$** for waves entering the device, and **$b$** for waves leaving the device. 

For a 2-Port device, we have four possible waves:
* **$a_1$:** The incident wave going INTO Port 1.
* **$b_1$:** The reflected wave coming OUT of Port 1.
* **$a_2$:** The incident wave going INTO Port 2.
* **$b_2$:** The reflected wave coming OUT of Port 2.

The entire behaviour of any microwave component can be described by two simple linear equations that link these waves together:

$$b_1 = S_{11}a_1 + S_{12}a_2$$

$$b_2 = S_{21}a_1 + S_{22}a_2$$

Those **$S$** terms are our Scattering Parameters! Let us break them down one by one.

---

## Scenario 1: Firing a Wave into Port 1

To figure out what $S_{11}$ and $S_{21}$ actually mean physically, we need to isolate them. 

Imagine we hook up our microwave generator to Port 1 and fire a wave ($a_1$) into the device. To prevent any chaos on the other side, we connect a perfectly matched terminator to Port 2. This terminator has the exact characteristic impedance ($Z_0$) of our system (which is usually $50 \ \Omega$ in standard RF labs). 

Because Port 2 is perfectly matched to $Z_0$, any wave that comes out of it will be completely absorbed. Nothing will bounce back in. This mathematically forces **$a_2 = 0$**.

Let us plug $a_2 = 0$ into our master equations:

$$b_1 = S_{11}a_1 + 0$$

$$b_2 = S_{21}a_1 + 0$$

Now, we can isolate and solve for the first two parameters!

### Deriving $S_{11}$ (Input Reflection)

$$S_{11} = \frac{b_1}{a_1}$$

**What is it?** It is the ratio of the wave bouncing out of Port 1 ($b_1$) to the wave we sent into Port 1 ($a_1$). 
This is exactly the **Reflection Coefficient ($\Gamma$)** we learned about in previous posts! It tells us how badly mismatched the input of the device is. In the lab, we often convert this to decibels and call it **Return Loss**.

### Deriving $S_{21}$ (Forward Transmission)

$$S_{21} = \frac{b_2}{a_1}$$

**What is it?** It is the ratio of the wave that successfully makes it out of Port 2 ($b_2$) compared to the wave we pumped into Port 1 ($a_1$). 
This is our **Gain** or **Insertion Loss**. If we are testing an amplifier, $S_{21}$ will be a large number (the wave got bigger). If we are testing a filter, $S_{21}$ tells us how much of our signal survived the journey.

---

## Scenario 2: Firing a Wave into Port 2

Now, let us flip the experiment. We hook our generator up to Port 2 and fire a wave ($a_2$) backwards into the device. We cap Port 1 with our perfect $Z_0$ terminator, meaning absolutely nothing bounces back into Port 1. This forces **$a_1 = 0$**.

Let us plug $a_1 = 0$ into the master equations:

$$b_1 = 0 + S_{12}a_2$$

$$b_2 = 0 + S_{22}a_2$$

Now we can solve for the final two parameters!

### Deriving $S_{22}$ (Output Reflection)

$$S_{22} = \frac{b_2}{a_2}$$

**What is it?** Just like $S_{11}$, this is a Reflection Coefficient, but looking backward into the output port. If you hook a cable up to Port 2, $S_{22}$ tells you how much energy will bounce right back at you.

### Deriving $S_{12}$ (Reverse Transmission)

$$S_{12} = \frac{b_1}{a_2}$$

**What is it?** This tells us how much energy leaks *backwards* through the device. For most components (like an isolator or an amplifier), we want waves to flow one way. We want $S_{21}$ to be high, but we want $S_{12}$ to be as close to zero as possible! This is also known as **Isolation**.

---

## How to read an S-Parameter

There is a very easy trick to remember what the numbers in the subscript mean. Read them as **"Out, In"**.

$S_{\text{Out, In}}$

* **$S_{21}$** = Wave comes OUT of 2, was put IN to 1. (Forward Transmission)
* **$S_{12}$** = Wave comes OUT of 1, was put IN to 2. (Reverse Leakage)
* **$S_{11}$** = Wave comes OUT of 1, was put IN to 1. (Input Reflection)
* **$S_{22}$** = Wave comes OUT of 2, was put IN to 2. (Output Reflection)

---

## Meeting the Vector Network Analyzer (VNA)

How do we actually measure these in the lab? We use an incredibly powerful instrument called a **Vector Network Analyzer (VNA)**. 

A VNA literally automates the exact mathematical scenarios we just derived. When you connect a 2-port device to a VNA, it automatically routes a microwave signal into Port 1 while internally terminating Port 2 to exactly $Z_0$. It measures the bouncing waves to calculate $S_{11}$ and $S_{21}$. Then, in a fraction of a millisecond, it flips internal switches, fires a wave into Port 2, and calculates $S_{22}$ and $S_{12}$.

In quantum engineering, watching the $S_{21}$ transmission curve on a VNA screen is exactly how we measure the resonant frequency of a superconducting qubit. We will dive deeper into how to read these complex measurements (including the famous Smith Chart!) in our upcoming posts.