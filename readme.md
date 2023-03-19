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

<img width="600" alt="Screenshot 2023-03-19 at 12 14 38" src="https://user-images.githubusercontent.com/90726430/226174607-2f524f2b-6dae-4bc4-bc34-0e75dcc5f777.png" style="display: block; margin: 0 auto">

$$F_{i,j} = -\frac{Gm_im_j}{r_{i,j}^2}$$

Note that this is the force that body i exerts on body j, here $m_i,m_j$ are the masses of body i and j respectively and $r_{i,j}$ is the distance between them. The force is negative as gravity is `attractive` meaning that the force always points towards the other body. 

This force acts along the line between the bodies, we can calculate this direction as follows:

$$
\hat{\bold{r}}_{i,j} =
    \frac
        {\bold{r}_j - \bold{r}_j}
        {|\bold{r}_j - \bold{r}_j|}
$$

Thus the most complete form of the force is given by:

$$
\bold{F}_{i,j} = 
    -\frac
        {Gm_im_j}
        {r_{i,j}^2}\hat{\bold{r}}_{i,j}
$$

### The gravitational force between multiple bodies

In the case of multiple body systems we need to consider the force that each body exerts on each other body that isn't it's-self, we can express this in our notation with a sum.

$$
\bold{F}_i =
    \sum_{i \neq j}
        \bold{F}_{i,j}
$$

Where $\bold{F}_i$ is the total force acting on body i.