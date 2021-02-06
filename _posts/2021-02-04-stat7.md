---
title : "통계물리 (7). Quantum Statistics: Density Operators"
excerpt: "Thermodynamics and Statistical Mechanics by Greiner, Chap.10"
categories :
    - statistical physics
author_profile : true
toc : true
toc_sticky : true
comments : true
use_math : true
---

고전적인 계를 다룰 때 하나의 macrostate에 해당하는 수많은 microstate configuration이 있다는 사실을 배웠던 기억이 있을 것이다. 그리고 일반적인 몇가지의 가정을 가지고 Ensemble 의 관점에서 우리는 특정한 microstate에 계가 존재할 확률을 계산해낼 수 있었다. 그리고 물리량의 기댓값 또한 이렇게 얻어낸 확률밀도를 가지고 ensemble average를 취하는 방식으로 계산했다. 이제 비슷한 논의를 양자계에 적용시켜보자.

먼저 양자계의 microstate가 어떻게 정의되는지 생각해보자. 고전적 계에서 microstate는 위상공간 내의 한 점 $(\vec{r}_i,\vec{p}_i)$에 대응되었다. 그러나 양자계에서는 불확정성 원리에 의해 위치와 운동량을 동시에 결정할 수 없으므로 위상공간 내의 한 점을 정확히 찾아내지 못한다. 따라서 위상공간의 자취 $(\vec{r}_i(t),\vec{p}_i(t))$를 얻어낼 수 없기 때문에 파동함수 $\Psi(\vec{r}_1,\dots,\vec{r}_N,t)$의 time evolution을 통해 계의 거동을 기술한다.

어떤 에너지 $E$, 부피 $V$, 입자 수 $N$을 가지는 고립계를 생각하자. 그러면 이 계 전체의 파동함수는 슈뢰딩거 방정식의 해로 다음과 같이 주어진다.

$$i\hbar\frac{\partial}{\partial t}\Psi(\vec{r}_1,\dots,\vec{r}_N,t)=\hat{H}(\vec{r}_i,\vec{p}_i)\Psi(\vec{r}_1,\dots,\vec{r}_N,t)$$

주어진 계가 고립계이기 때문에 계의 총 에너지 $E$는 보존량이고, $\Psi$는

$$\Psi(\vec{r}_1,\dots,\vec{r}_N,t)=\Psi_E(\vec{r}_1,\dots,\vec{r}_N)\exp\left\{-i\frac{Et}{\hbar} \right\}$$

로 쓸 수 있다. 이 때 $\Psi_E$는 해밀토니안의 고유상태로

$$\hat{H}\Psi_E(\vec{r}_1,\dots,\vec{r}_N) =E\Psi_E(\vec{r}_1,\dots,\vec{r}_N)$$

를 만족한다. 여기서 $E$가 고정된 값으로 주어졌기 때문에 매우 특정한 $\Psi_E$만이 계의 파동함수가 될 수 있지만, 거시적인 계에서는 에너지 고윳값의 간격이 매우 작아지고, 고유상태의 degeneracy로 인해 특정한 $E$를 고윳값으로 가지는 많은 해가 존재할 수 있게 된다.

게다가 거시적인 계에서는 에너지의 불확정성 $\Delta E$가 항상 존재하므로 에너지 $E$와 $E+\Delta E$ 사이에 무수히 많은 상태가 존재할 수 있다. 이는 거시적인 계의 에너지가 연속적인 분포를 가지는 것으로 해석할 수 있다. 그리고 고전적인 계에서 microstate가 위상공간의 한 점에 대응되었던 것 처럼, 양자계에서 microstate는 계의 파동함수 $\Psi(\vec{r}_1,\dots,\vec{r}_N,t)$에 대응된다. 이로부터 $E$와 $E+\Delta E$ 사이에 있는 상태의 수 $g(E) = \Omega(E)/\Delta E$를 구해낼 수 있다. 

앞서 보았듯, 양자계의 경우 microstate가 위상공간 위의 한 점이 아니라 파동함수에 대응되기 때문에 물리량의 ensemble average도 파동함수로부터 구해진다. 양자역학에서 어떤 관측가능한 물리량(Observable) $f(\vec{r}_i,\vec{p}_i)$은 Hermitian operator로 $\hat{f}(\vec{r}_i,\vec{p}_i)$ 주어진다. 따라서 $\hat{f}(\vec{r}_i,\vec{p}_i)$의 고윳값은 모두 실수로 주어지고, 고유상태 $\phi_f$는 서로 직교하는 성질을 갖는다.

$$\hat{f}\phi_f = f\phi_f$$

이 때 각각의 고윳값은 계로부터 얻어낼 수 있는 관측량에 해당한다. 양자계의 특성 때문에 하나의 microstate에 대해서도 각 측정에 대해 항상 같은 측정값을 주지 않기 때문에 확률을 고려해주어야 한다. microstate $\Psi_E$로부터 고윳값 $f$를 얻어낼 확률은

$$\langle \phi_f \vert \Psi_E^{(i)}\rangle = \int d^3r_1\cdots d^3r_N \phi_f^{\ast (i)}(\vec{r}_1,\dots,\vec{r}_N)\Psi_E^{(i)}(\vec{r}_1,\dots,\vec{r}_N)$$

이고, 한 microstate에 대해 관측가능량 $f$의 기댓값은

$$\langle \Psi_E^{(i)} \vert \hat{f}\vert \Psi_E^{(i)}\rangle = \int d^3r_1\cdots d^3r_N \Psi_E^{(i)\ast}(\vec{r}_1,\dots,\vec{r}_N) \hat{f}(\vec{r}_i,\vec{p}_i)\Psi_E^{(i)}(\vec{r}_1,\dots,\vec{r}_N)$$

로 주어진다. 하지만 계가 어떤 microstate에 있는지도 정확히 알 수 없고, 단지 계가 microstate $\Psi_E^{(i)}$에 있을 확률 $\rho_i$만을 알 수 있기 때문에 관측가능량 $f$의 기댓값은 이를 고려해서 다음과 같이 주어진다.

$$\langle\hat{f}\rangle = \sum_{i,k} \rho_{ki} \langle \Psi_E^{(i)} \vert \hat{f}\vert \Psi_E^{(k)}\rangle$$

그리고 각각의 microstate $\Psi_E^{(i)}$를

$$\Psi_E^{(i)} = \sum_k a_k^{(i)}\phi_k$$

로 전개할 수 있으므로

$$\langle\hat{f}\rangle = \sum_i \rho_i \sum_{k,k'}a_{k'}^{(i)}a_{k}^{(i)\ast}\langle\phi_k\vert\hat{f}\vert\phi_{k'}\rangle\\=\sum_{k,k'}\left(\sum_i \rho_i a_{k'}^{(i)}a_{k}^{(i)\ast} \right)\langle\phi_k\vert\hat{f}\vert\phi_{k'}\rangle$$

가 성립한다. 괄호 안의 항을

$$\rho_{k'k}=\sum_i \rho_i a_{k'}^{(i)}a_{k}^{(i)\ast}$$

로 쓰면 최종적으로

$$ \langle\hat{f}\rangle = \sum_{k,k'}\rho_{k,k'}\langle\phi_k\vert\hat{f}\vert\phi_{k'}\rangle$$

를 얻는다. 그리고 $\rho_{k'k}$를 연산자 $\hat{\rho}$를 고유상태 $\phi_k$로 전개했을 때의 행렬성분으로 해석하면

$$\langle\hat{f}\rangle=\sum_{k,k'}\langle\phi_{k'}\vert\hat{\rho}\vert\phi_k\rangle\langle\phi_k\vert\hat{f}\vert\phi_{k'}\rangle$$

이므로

$$\langle\hat{f}\rangle=\sum_{k'}\langle\phi_{k'}\vert\hat{\rho}\hat{f}\vert\phi_{k'}\rangle=\text{Tr}\,(\hat{\rho}\hat{f})$$

로 표현할 수도 있다. 이는 관측가능량 $\hat{f}$의 ensemble average는 $\hat{f}$와 계가 특정 microstate에 있을 확률을 의미하는 $\hat{\rho}$의 Trace로 표현할 수 있다는 것을 의미한다. 이 때 연산자 $\hat{\rho}$를 **밀도 연산자(Density operator)**라 부른다.
 

## Reference

[1] Thermodynamics and Statistical Mechanics, Greiner,Neise,and Stoecker, Springer-Verlag, 1995