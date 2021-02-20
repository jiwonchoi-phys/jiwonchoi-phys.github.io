---
title : "통계물리 (8). Pure and Mixed States"
excerpt: "Thermodynamics and Statistical Mechanics by Greiner, Chap.10"
categories :
    - statistical physics
author_profile : true
#toc : true
#toc_sticky : true
comments : true
use_math : true
---

만약 양자역학적 계가 특정한 microstate $\vert\Psi^{(i)}\rangle$에 있는 경우, 이를 **순수 상태(Pure state)** 라고 부른다. 반면에 계가 여러 microstate $\vert\Psi^{(i)}\rangle$에 확률 $\rho_i$를 가지고 존재할 경우, 이를 **혼합 상태(Mixed state)**라고 부른다. Pure state와 mixed state 모두에 대해 앞서 정의한 밀도 행렬이 정의되고, 따라서 밀도행렬이 주어진다면 임의의 관측가능량에 대한 ensemble average를 계산할 수 있다는 것을 지금부터 확인해보자.

먼저 어떤 계의 밀도연산자가 특정 기저상태 $\vert\phi_k\rangle$에 대해 다음과 같이 행렬 형태로 주어져있다고 생각해보자.

$$\hat{\rho} = \sum_{k,k'} \vert\phi_{k'}\rangle \rho_{k'k} \langle \phi_k\vert$$

지난 포스팅에서 본 것 처럼 밀도행렬의 대각성분 $\rho_{kk}=\langle\phi_k\vert\hat{\rho}\vert\phi_k\rangle$은 계가 상태 $\vert\phi_k\rangle$에 존재할 확률을 의미하고, off-diagonal 성분 $\rho_{k'k}=\langle\phi_{k'}\vert\hat{\rho}\vert\phi_k\rangle$은 상태 $\vert\phi_k\rangle$가 다른 상태 $\vert\phi_{k'}\rangle$로 전이할 확률을 나타낸다.

만약 어떤 계가 상태 $\vert\Psi^{(i)}\rangle$에 있을 확률이 $\rho_{ii}$로 주어지고, $i\neq k$일 때 $\rho_{ik}=0$이라면 밀도 연산자는

$$\hat{\rho}=\sum_i \vert\Psi^{(i)}\rangle \rho_{ii}\langle\Psi^{(i)}\vert$$

와 같이 주어진다. 여기서 하나의 상태 $\vert\Psi^{(i)}\rangle$로만 계가 구성된다면 이는 pure state에 해당하고, 여러 $\vert\Psi^{(i)}\rangle$가 존재할 가능성이 있다면 mixed state라고 볼 수 있다. 따라서 pure state에 해당되는 밀도연산자는

$$\hat{\rho}^{\text{pure}}=\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert$$

로 주어지고, 이는 단순히 상태 $\vert\Psi^{(i)}\rangle$로의 Projection operator이다. $\vert\Psi^{(i)}\rangle$가 서로 정규직교하다면, 밀도행렬의 성분은 $\rho_{ii}=1$이고 다른 성분은 모두 $0$으로 주어지게 될 것이다. 하지만 다른 임의의 기저상태로 $\vert\Psi^{(i)}\rangle$를 표현할 수 있기 때문에, 다른 기저들에 대해 밀도행렬을 구성한다면 비록 pure state지만 off-diagonal element도 포함할 수 있게 된다.

$$\hat{\rho}^{\text{pure}}=\sum_{kk'}\vert\phi_k\rangle\langle\phi_k\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert\phi_{k'}\rangle\langle\phi_{k'}\vert \\ = \sum_{kk'}\vert\phi_k\rangle a_{k}^{(i)}a_{k'}^{(i)\ast} \langle \phi_{k'}\vert$$

여기서 $a_{k}^{(i)}=\langle \phi_k\vert\Psi^{(i)}\rangle$는 $\vert\Psi^{(i)}\rangle$를 $\phi_k$에 대해 전개했을 때의 계수이다. 따라서 이 경우에 밀도행렬의 성분은

$$\rho_{kk'}^{\text{pure}} = a_{k}^{(i)}a_{k'}^{(i)\ast}$$

로 주어지므로, off-diagonal element도 포함한다.

그리고 $\hat{\rho}^{\text{pure}}=\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert$로 정의되므로 pure state에 대해

$$(\hat{\rho}^{\text{pure}})^2 = \hat{\rho}^{\text{pure}}$$

또한 만족한다는 것을 알 수 있다.

하지만 만약 계가 여러개의 $\vert\Psi^{(i)}\rangle$가 각각의 확률 $\rho_{ii}$로 존재한다면 계의 상태는 하나로 정해질 수 없다. 이런 경우를 **혼합 상태(mixed state)**라고 부른다. 그리고 물론 계가 상태 $\vert\Psi^{(i)}\rangle$에 있을 확률 $\rho_{ii}$는

$$\sum_i \rho_{ii}=1,\quad 0\le \rho_{ii} \le 1$$

을 만족해야 한다.

지금부터 특정 기저에 대해 밀도행렬이 주어지면 이로부터 어떻게 양자역학적 관측가능량을 계산할 수 있는지 알아보자. $\hat{f}$를 어떤 관측가능량, $\vert \phi_f\rangle$을 고윳값 $f$에 대응되는 고유상태라고 가정하자. 순수 상태 $\vert\Psi^{(i)}\rangle$가 주어져 있을 때 이로부터 고윳값 $f$를 얻을 확률은 일반적으로 $\vert\langle\phi_f\vert\Psi^{(i)}\rangle\vert^2$를 계산하면 된다. 이는

$$\vert\langle\phi_f\vert\Psi^{(i)}\rangle\vert^2=\langle\phi_f\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert\phi_f\rangle$$

로 쓸 수 있고, $\vert\phi_f\rangle\langle\phi_f\vert=\hat{P}_{\vert\phi_{f}\rangle}$, $\hat{\rho}^{\text{pure}}=\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert$ 이므로

$$\langle\phi_f\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert\phi_f\rangle\\
= \sum_{f'}\langle\phi_{f}\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert\phi_{f'}\rangle\langle\phi_{f'}\vert\phi_f\rangle\\
= \sum_{f'}\langle\phi_{f'}\vert\Psi^{(i)}\rangle\langle\Psi^{(i)}\vert\phi_{f}\rangle\langle\phi_{f}\vert\phi_{f'}\rangle\\
= \sum_{f'}\langle\phi_{f'}\vert \hat{\rho}^{\text{pure}}\hat{P}_{\vert\phi_{f}\rangle}\vert\phi_{f'}\rangle\\
= \text{Tr}\,(\hat{\rho}^{\text{pure}}\hat{P}_{\vert\phi_{f}\rangle}) $$

를 통해 확률을 계산할 수도 있다. 






















## Reference

[1] Thermodynamics and Statistical Mechanics, Greiner,Neise,and Stoecker, Springer-Verlag, 1995