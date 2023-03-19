# Planetary motion simulation

In this project I intend to create a custom planetary orbit simulation - eventually in a GUI.

- [Planetary motion simulation](#planetary-motion-simulation)
  - [The maths behind it](#the-maths-behind-it)
    - [The gravitational force between two bodies](#the-gravitational-force-between-two-bodies)
    - [The gravitational force between multiple bodies](#the-gravitational-force-between-multiple-bodies)


## The maths behind it

Here is all of the theory behind the code in this repository.

### The gravitational force between two bodies

We can express the magnitude of the graviatational force between two bodies, i and j, using the following formula:

$$F_{i,j} = -\frac{Gm_im_j}{r_{i,j}^2}$$

Note that this is the force that body i exerts on body j, here $m_i,m_j$ are the masses of body i and j respectively and $r_{i,j}$ is the distance between them. The force is negative as gravity is `attractive` meaning that the force always points towards the other body. 

This force acts along the line between the bodies, we can calculate this direction as follows:

$$\hat{\bold{r}}_{i,j} =\frac{\bold{r}_j - \bold{r}_j}{|\bold{r}_j - \bold{r}_j|}$$

Thus the most complete form of the force is given by:

$$\bold{F}_{i,j} = -\frac{Gm_im_j}{r_{i,j}^2}\hat{\bold{r}}_{i,j}$$

### The gravitational force between multiple bodies