# Path finding for **Mountain Climbing Route** Using Digital Elevation Model (DEM)

Class Project of *Advanced GIS - Dr. Jelokhani*.

by: Moien Rangzan

---

## Intro
It took humans thousands of years of experience and countless lives to find the optimum paths to ascend mountains. Finding the best route for an unexplored mountain requires competent mountain climbers and a lot of supervised surveying, which can be costly and dangerous. For planets other than the earth, the situation is even worse. 

What I wanted to try in this project was to achieve an unsupervised method to find this path with the most available and accessible Remote Sensing data, the Digital Elevation Model (DEM).


## Data

* Downloaded SRTM for Mount **Damavand** from Earth Explorer - I didn't know about *Geemap* by that time.
![SRTM](https://github.com/moienr/DEM_Path_finding/blob/acf146ab85696a931d190e0facb3869e70eb441a/imgs/1_srtm_ee.png)

* Asked my friend, a professional mountain climber, about Mount Damavand, and he suggested the southern ascending path, so I clipped only the south part of Damavand using Raster Clip to reduce computation.
![Cliped](https://github.com/moienr/DEM_Path_finding/blob/acf146ab85696a931d190e0facb3869e70eb441a/imgs/4_clipraster.png)

* Again, with his assistance, I added four locations to aid the Q-Learning agent find his way, including a starting node, a mountain summit, and two resting sites that mountain climbers often visit. and convert them to a raster of the same size and spatial resolution as our SRTM area.
![Points](https://github.com/moienr/DEM_Path_finding/blob/acf146ab85696a931d190e0facb3869e70eb441a/imgs/3_arcgis_points.png)

* Then calculated Slope and Aspect form the DEM, to further help the Agent.

![Slope_Aspect](https://github.com/moienr/DEM_Path_finding/blob/c1b8a516921a03c699f95878fbc8dfbcaad39fc6/imgs/slope_ascpet.png)


## Q-Learning
There are a ton of youtube videos explaining this Algorithm, so I'm not translating my project description to here :))

But here is the Sudo:


>Initialize $\mathbf{Q}(\mathbf{s}, \mathbf{a})$ for all $\mathbf{s} \in \mathcal{S}$ and $\mathbf{a} \in \mathcal{A}(\mathbf{s})$

>Loop forever:

>>  (a) $S \leftarrow$ current (nonterminal) state
  
>>  (b) $\boldsymbol{E} \leftarrow \boldsymbol{\varepsilon}$-greedy $(\boldsymbol{S}, \boldsymbol{Q})$
  
>>  (c) Take action A; observe Resultant reward, $R$, and state, $S^{\prime}$
  
>>  (d) $Q(S, A) \leftarrow Q(S, A)+\alpha\left[R+\gamma \max _a Q\left(S^{\prime}, a\right)-Q(S, A)\right]$



## Logic

### Agent

The Agent can go Up-Down-Left-Right

### Environment

#### Action Reward

* Every move has a punishment unless otherwise.
* We calclulate the `reward` for each action, based on its `neighboring cells`:

if current elevation $>$ next elevation:

$$
\text { reward }=\frac{-\mid \text { current elevation }-\text { next elevation }+1 \mid}{1000}
$$

else if current elevation $<$ next elevation:

$$
\text { reward }=\frac{-\mid \text { current elevation }-\text { next elevation }+1 \mid}{100}
$$

Notice the denominator, going down the hill has ten times more punishment than going uphill; we want our agent to ascend unless it is necessary

we chose 100 in denominator since we ran a `3x3` kernel and maximum difference in elevation between two adjacent pixels were 99.0, so the punishment is somthing betwen `0` and `-1`


#### Slippery slope

The idea is that the steeper the slope, the higher the chance our agent will fall. I chose an exponential function with the power of 10 for this. You can see after the slope of `60` percent that the chance of falling down increases immensely

![Probablity](https://github.com/moienr/DEM_Path_finding/blob/65ada022d4df86494b1fe88ea1b3a3a844a0bee7/imgs/slipping%20func.png)

The aspect comes in if the agent falls; if the aspect is, for example, towards the south, and the agent decides to go right, but he falls, he will fall into the northern pixel.


#### Edges

The edge pixels are dead zones, and has a reward of `-100`



# Resualts

