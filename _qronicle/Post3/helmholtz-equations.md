---
layout: post
title: "From Maxwell to Helmholtz: Deriving the Electromagnetic Wave"
description: "We established Maxwell's equations. Now, let's derive the wave equations that allow microwave control pulses to propagate through space and transmission lines."
order: 3
slug: "3"
topic: [Theory, EM-Theory, L1-Foundational, Derivation]
images:
  - /images/qronicle/post3/image1.jpg
  - /images/qronicle/post3/image2.gif
---

## The Origin of the Wave

In our previous post, we looked at Maxwell's equations—the foundational laws governing electric and magnetic fields. But knowing the rules of static or slowly changing fields isn't enough when we want to control quantum states. When you are running simulations for complex high-frequency components or modeling the electromagnetic dynamics inside physical systems, the software engine is constantly solving for how waves propagate. 

To bridge the gap between classical electromagnetics and quantum control, we need to understand how these fields travel through space and materials as waves. This brings us to the Wave Equation and its time-harmonic cousin, the Helmholtz Equation.

Let's derive how an electromagnetic wave is born in a source-free region (like free space or an ideal dielectric), where there are no free charges ($\rho = 0$) and no free currents ($\mathbf{J} = 0$).

---

## Deriving the Electric Field Wave Equation

We start with Maxwell's equations in our source-free region:

1. $\nabla \cdot \mathbf{E} = 0$
2. $\nabla \cdot \mathbf{B} = 0$
3. $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$
4. $\nabla \times \mathbf{B} = \mu \epsilon \frac{\partial \mathbf{E}}{\partial t}$

To find the wave equation for the electric field, we take the curl of Faraday's Law (Equation 3):

$$
\nabla \times (\nabla \times \mathbf{E}) = \nabla \times \left(-\frac{\partial \mathbf{B}}{\partial t}\right)
$$

Since space and time derivatives are independent, we can swap their order on the right side:

$$
\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t} (\nabla \times \mathbf{B})
$$

Now, we apply a standard vector identity to the left side: $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$. Because we are in a source-free region, $\nabla \cdot \mathbf{E} = 0$, so the left side simply becomes $-\nabla^2 \mathbf{E}$.

Next, we substitute Equation 4 into the right side:

$$
-\nabla^2 \mathbf{E} = -\frac{\partial}{\partial t} \left(\mu \epsilon \frac{\partial \mathbf{E}}{\partial t}\right)
$$

Canceling the negative signs and evaluating the time derivative gives us the **3D Wave Equation for the Electric Field**:

$$
\nabla^2 \mathbf{E} - \mu \epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0
$$

### Simplifying to 1D Propagation

If we assume the electric field is oriented purely along the x-axis and the wave is propagating along the z-axis, the spatial derivatives in x and y drop to zero. The equation simplifies beautifully to:

$$
\frac{\partial^2 E_x}{\partial z^2} - \mu \epsilon \frac{\partial^2 E_x}{\partial t^2} = 0
$$

*(Note: The term $\frac{1}{\sqrt{\mu \epsilon}}$ defines the **velocity** of the wave. In a perfect vacuum, this becomes $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$, the speed of light.)*

---

## Deriving the Magnetic Field Wave Equation

The derivation for the magnetic field mirrors the electric field perfectly. We take the curl of Equation 4:

$$
\nabla \times (\nabla \times \mathbf{B}) = \mu \epsilon \frac{\partial}{\partial t} (\nabla \times \mathbf{E})
$$

Using the same vector identity on the left (and knowing $\nabla \cdot \mathbf{B} = 0$), and substituting Faraday's Law into the right:

$$
-\nabla^2 \mathbf{B} = \mu \epsilon \frac{\partial}{\partial t} \left(-\frac{\partial \mathbf{B}}{\partial t}\right)
$$

This yields the **3D Wave Equation for the Magnetic Field**:

$$
\nabla^2 \mathbf{B} - \mu \epsilon \frac{\partial^2 \mathbf{B}}{\partial t^2} = 0
$$

Since $\mathbf{B} = \mu \mathbf{H}$, we can immediately write the exact same generalized wave equation in terms of the magnetic field intensity, $\mathbf{H}$. If the electric field is in the x-axis and propagating along the z-axis, the magnetic field $\mathbf{H}$ will be oriented along the y-axis:

$$
\frac{\partial^2 H_y}{\partial z^2} - \mu \epsilon \frac{\partial^2 H_y}{\partial t^2} = 0
$$

---

## The Helmholtz Equation (Time-Harmonic Fields)

In quantum control and microwave engineering, we rarely deal with arbitrary pulses right out of the gate. We usually work with continuous sinusoidal waves at specific frequencies (like a 5 GHz drive pulse for a transmon qubit). 

When fields oscillate sinusoidally, we can express their time dependence as $e^{i\omega t}$. This is incredibly powerful because every time derivative $\frac{\partial}{\partial t}$ simply becomes a multiplication by $i\omega$. Therefore, a second time derivative $\frac{\partial^2}{\partial t^2}$ becomes $(i\omega)^2 = -\omega^2$.

Substitute this into our wave equation:

$$
\nabla^2 \mathbf{E} - \mu \epsilon (-\omega^2 \mathbf{E}) = 0
$$

$$
\nabla^2 \mathbf{E} + \omega^2 \mu \epsilon \mathbf{E} = 0
$$

By defining the **wavenumber** as $k = \omega \sqrt{\mu \epsilon}$, we arrive at the **Helmholtz Equation**:

$$
\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0
$$

---

## Deriving Wave Impedance: The E and H Relationship

As these waves propagate, the electric and magnetic fields are intrinsically linked. But how do we determine the ratio of their magnitudes? 

Let's look at our 1D wave propagating along the z-axis, with $E_x$ and $H_y$. Using our time-harmonic solutions (where fields oscillate as $e^{i(\omega t - kz)}$), we can look back at Faraday's Law:

$$
\nabla \times \mathbf{E} = -\mu \frac{\partial \mathbf{H}}{\partial t}
$$

Since our electric field only has an x-component and changes only along the z-axis, the curl of $\mathbf{E}$ simplifies down to just one spatial derivative:

$$
\frac{\partial E_x}{\partial z} = -\mu \frac{\partial H_y}{\partial t}
$$

Because our waves follow the $e^{i(\omega t - kz)}$ format, taking a derivative with respect to space ($z$) is the same as multiplying by $-ik$. Taking a derivative with respect to time ($t$) is the same as multiplying by $i\omega$. Substituting these in:

$$
-ik E_x = -\mu (i\omega) H_y
$$

Cancel the negative signs and the imaginary unit ($i$):

$$
k E_x = \mu \omega H_y
$$

Rearrange the equation to find the ratio of the electric field magnitude to the magnetic field magnitude:

$$
\frac{E_x}{H_y} = \frac{\mu \omega}{k}
$$

Earlier, we defined our wavenumber as $k = \omega \sqrt{\mu \epsilon}$. Plugging that in gives:

$$
\frac{E_x}{H_y} = \frac{\mu \omega}{\omega \sqrt{\mu \epsilon}}
$$

The angular frequency ($\omega$) cancels out. Simplifying the remaining terms gives us the **Intrinsic Impedance ($\eta$)**:

$$
\frac{E_x}{H_y} = \sqrt{\frac{\mu}{\epsilon}} = \eta
$$

This proves that the ratio of the electric and magnetic field amplitudes is entirely dictated by the medium they are traveling through.

**In Free Space:**
The permeability is $\mu_0$ and permittivity is $\epsilon_0$. 
$$
\eta_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 377 \, \Omega
$$

**In Dielectric Materials (like a quantum processor substrate):**
When propagating through a material, the permittivity increases by the material's relative dielectric constant ($\epsilon = \epsilon_r \epsilon_0$). Because $\epsilon$ is in the denominator, the intrinsic impedance of the material drops, and the wave travels slower. 

Understanding these impedance shifts is absolutely critical. When routing a microwave signal from a room-temperature generator down into a cryogenic dilution refrigerator, any impedance mismatch between the cables, the connectors, and the quantum chip will cause signal reflections—ruining the precise control required to orchestrate quantum logic gates.