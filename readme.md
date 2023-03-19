# Planetary motion simulation

In this project I intend to create a custom planetary orbit simulation - eventually in a GUI.

- [Planetary motion simulation](#planetary-motion-simulation)
  - [The maths behind it](#the-maths-behind-it)
    - [The gravitational force between two bodies](#the-gravitational-force-between-two-bodies)
    - [The gravitational force between multiple bodies](#the-gravitational-force-between-multiple-bodies)
    - [Calculating dynamics of planets](#calculating-dynamics-of-planets)
      - [Naive approach](#naive-approach)


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

### Calculating dynamics of planets

We know from newtons 2nd law that:

$$
\bold{F} =
    m\bold{a}
$$

aka `"force = mass * accelaration"`. Thus we can find the accelaration of the i'th planet:

$$
\bold{a}_i = \frac{1}{m}\bold{F}_i
$$

#### Naive approach

This is the naive approach as we assume that the accelaration is constant in time (which isnt true) but if the time step is small enough this should not matter.

If $\bold{a}_i = \frac{1}{m}\bold{F}_i$, then we should be able to calculate $\bold{v}_i$ and $\bold{x}_i$ by integrating with respect to time and using some initial conditions, i.e `inital velocity` and `inital displacement`.

Suppose that the accelaration in an interval $[t_{\gamma},t_{\gamma+1}]$ - where ideally $t_{\gamma+1} - t_{\gamma} << 1$, is denoted by $\bold{a}_{i,\gamma}$ - the same goes for velocity and displacement. In each interval there is a change in the quantity, that I shall denote $\Delta \bold{v}_{i,\gamma}$ for example. It stands to reason that the position of a planet at timestep $\gamma$ is the sum of the previous position and the change in the time interval. For the sake of notation, define $t_{\gamma+1}-t_{\gamma} = \Delta t$.

$$
\Delta\bold{v}_{i,\gamma} = 
    \int_{t_\gamma}^{t_{\gamma+1}}{\bold{a}_{i,\gamma}}dt 
    = 
    {\bold{a}_{i,\gamma}}\Delta t
$$

$$
\bold{v}_{i,\gamma} 
    = 
    \bold{v}_{i,\gamma-1} + \Delta\bold{v}_{i,\gamma}
    =
    \bold{v}_{i,\gamma-1} + \bold{a}_{i,\gamma}\Delta t
$$

$$
\Delta\bold{x}_{i,\gamma} = 
    \int_{t_\gamma}^{t_{\gamma+1}}{\bold{v}_{i,\gamma}}dt
    = 
    \int_{t_\gamma}^{t_{\gamma+1}}{\bold{v}_{i,\gamma -1}+ \bold{a}_{i,\gamma}\Delta t}dt \\
    = 
    \bold{v}_{i,\gamma -1}\Delta t + \bold{a}_{i,\gamma}\Delta t^2
$$

$$
\bold{x}_{i,\gamma} 
    = 
    \bold{x}_{i,\gamma-1} + \Delta\bold{x}_{i,\gamma} \\
    =
    \bold{x}_{i,\gamma-1} + \bold{v}_{i,\gamma -1}\Delta t + \bold{a}_{i,\gamma}\Delta t^2
$$


So long as our time steps are sufficiently small this method should yield some cohesive results. So we have our three equations for getting the orbital trajectory:

1. $\bold{a}_{i,\gamma} = \frac{1}{m}\bold{F}_i$
2. $\bold{v}_{i,\gamma} = \bold{v}_{i,\gamma-1} + \bold{a}_{i,\gamma}\Delta t$
3. $\bold{x}_{i,\gamma} = \bold{x}_{i,\gamma-1} + \bold{v}_{i,\gamma -1}\Delta t + \bold{a}_{i,\gamma}\Delta t^2$

This method yields the following:

![output](https://user-images.githubusercontent.com/90726430/226186864-a193f2f1-7ece-4620-95b5-f41d0c2bbdad.png)


