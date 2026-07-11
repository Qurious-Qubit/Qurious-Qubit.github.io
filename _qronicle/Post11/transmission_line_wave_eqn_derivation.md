---
layout: post
title: "The Math of the Rope: Deriving the Telegrapher's Equations"
description: "How do we mathematically prove that a wire acts like a wave? A simple, step-by-step derivation of the Telegrapher's equations using basic circuit theory."
order: 11
slug: "11"
topic: [Theory, Derivation, Microwave-Engg, L2-Intermediate]
images:
  - /images/qronicle/post10/image1.jpg
  - /images/qronicle/post10/image2.webp
  - /images/qronicle/post10/image3.png
resources:
  - name: "Solution to Telegrapher's Equation (ResearchGate)"
    link: "https://www.researchgate.net/profile/Smrity-Dwivedi/post/Solution_to_Telegraphers_Equation/attachment/5b728688cfe4a7f7ca5a29bb/AS%3A659431792578569%401534232199959/download/ma1.pdf"
  - name: "Telegrapher's Equation (GeeksforGeeks)"
    link: "https://www.geeksforgeeks.org/electrical-engineering/telegraphers-equation/"
references:
  - name: "Transmission Lines - Telegrapher's Equations (YouTube)"
    link: "https://www.youtube.com/watch?v=qFBr9xXloAc&list=PL2fRCJxWQiS8qheVohpFJSl1WF6lNNBWh&index=3"
---

## Modeling the "Rope"

In our last post, we talked about how a high-frequency signal doesn't just instantly appear at the end of a wire. Because of the delays in the line, the energy actually travels like a wave on a rope. 

But how do we model this mathematically? We cannot use basic DC circuit rules for the whole cable at once. Instead, we have to take a very small section of the transmission line, with a tiny length of $dl$. 

Even for a simple wire, if we zoom in close enough, we will notice every line has some resistance and inductance along the wire, and some capacitance and conductance leaking between the wires. So, we assume our tiny section of length $dl$ has:
* A lumped inductor ($L$) and resistor ($R$) in series.
* A capacitor ($C$) and a conductance/resistor ($G$) in shunt (parallel).

*(Note: $R, L, G, C$ here are values per unit length, so for a section of length $dl$, their actual values are $R \cdot dl, L \cdot dl$, etc.) image on the right*

---

## Deriving the Voltage Equation

Let's assume the voltage entering this tiny section is $V_{in}$ and the voltage coming out is $V_o$. The current flowing through the line is $I$. 

When the current passes through this small piece of wire, there will be a voltage drop across the series resistor and the series inductor. By applying basic Kirchhoff's Voltage Law (KVL), we can say:

$$V_{in} - I \cdot R \cdot dl - L \cdot dl \frac{\partial I}{\partial t} = V_o$$

Let's bring $V_o$ to the left side and set the equation to zero:

$$V_{in} - V_o - I \cdot R \cdot dl - L \cdot dl \frac{\partial I}{\partial t} = 0$$

Now, we just divide the entire equation by our tiny length, $dl$:

$$\frac{V_{in} - V_o}{dl} - R I - L \frac{\partial I}{\partial t} = 0$$

In calculus, the difference in voltage over a tiny distance $\frac{V_{in} - V_o}{dl}$ is simply the negative spatial derivative of the voltage, $-\frac{\partial V}{\partial z}$. So our final voltage equation becomes:

$$-\frac{\partial V}{\partial z} = R I + L \frac{\partial I}{\partial t}$$

---

## Deriving the Current Equation

Now, let's do the exact same thing for the current. The current entering the section is $I_{in}$ and the current coming out is $I_o$. But some current leaks away through the shunt conductance ($G$) and the shunt capacitor ($C$).

By applying Kirchhoff's Current Law (KCL) at the node, we can write:

$$I_{in} - V \cdot G \cdot dl - C \cdot dl \frac{\partial V}{\partial t} = I_o$$

Bring $I_o$ to the left side:

$$I_{in} - I_o - V \cdot G \cdot dl - C \cdot dl \frac{\partial V}{\partial t} = 0$$

Again, divide the whole equation by $dl$:

$$\frac{I_{in} - I_o}{dl} - G V - C \frac{\partial V}{\partial t} = 0$$

Just like before, $\frac{I_{in} - I_o}{dl}$ is the negative spatial derivative of the current, $-\frac{\partial I}{\partial z}$. So our final current equation becomes:

$$-\frac{\partial I}{\partial z} = G V + C \frac{\partial V}{\partial t}$$

---

## The Big Connection

Let's look at the two final equations we just derived side-by-side:

$$-\frac{\partial V}{\partial z} = R I + L \frac{\partial I}{\partial t}$$

$$-\frac{\partial I}{\partial z} = G V + C \frac{\partial V}{\partial t}$$

These are the famous **Telegrapher's Equations**. 

So, if we observe this carefully, we can notice that the spatial derivative (change in distance) is directly equal to a differential equation in time. These two equations give the complete relationship between the time and space variations of current and voltage across the transmission line.

Does this look familiar? It should! This is very similar to the EM wave derivation we did earlier in our [Helmholtz Equations post](https://qurious-qubit.github.io/qronicle/helmholtz-equations/). In Maxwell's equations, a changing electric field in time creates a changing magnetic field in space, and vice versa. Here in our transmission line, a changing voltage in time creates a changing current in space. 

By simply breaking a wire down into tiny $R, L, G, C$ components, we have mathematically proven that the electrical signal behaves exactly like a traveling wave!

We will derive the excact wave equation in the following posts!!