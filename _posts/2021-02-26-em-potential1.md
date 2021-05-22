---
title : "전자기학(1). 스칼라 및 벡터 퍼텐셜 & 게이지 변환"
excerpt: "Introduction to electrodynamics 4th ed. by David J. Griffiths, Chap.10"
categories :
    - electrodynamics
author_profile : true
#toc : true
#toc_sticky : true
comments : true
use_math : true
---

이번 포스팅에서는 스칼라 및 벡터 퍼텐셜과 게이지 변환에 대해 알아보겠습니다. 사실 전자기학을 포스팅할 생각은 별로 없었는데 radiation에 대해 좀 알아놔야 할 것 같더라구요. 그래서 포스팅을 하게 되었습니다.

우리는 전자기학 시간에 네 개의 맥스웰 방정식을 배웠습니다.

$$\nabla\cdot\mathbf{E}=\frac{1}{\epsilon_0}\rho,\quad \nabla\times\mathbf{E}=-\frac{\partial \mathbf{B}}{\partial t}
\\\nabla\cdot\mathbf{B}=0,\quad \nabla\times\mathbf{B}=\mu_0 \mathbf{J}+\mu_0\epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

전하밀도 $\rho(\mathbf{r},t)$와 전류밀도 $\mathbf{J}(\mathbf{r},t)$가 주어졌을 때 전기장$\mathbf{E}(\mathbf{r},t)$과 자기장 $\mathbf{B}(\mathbf{r},t)$은 어떻게 주어질까요? 정적인 경우에는 쿨롱 법칙과 비오-사바르 법칙을 이용해 답을 구할 수 있었습니다. 하지만 전기장과 자기장이 시간에 따라 변하는 경우에는 이 법칙들이 잘 맞지 않았습니다. 따라서 정적인 경우와 조금 다른 방법을 써야하는데, 그것이 바로 퍼텐셜을 이용하는 것입니다.

정전기학에서는 $\nabla\times\mathbf{E}=0$이 성립했기 때문에 이로부터 스칼라 퍼텐셜 $\mathbf{E}=-\nabla V$를 정의해서 사용했었죠. 그런데 전기동역학에서는 자기장의 시간변화에 전기장이 영향을 받기 때문에 퍼텐셜의 형태도 수정해야 할 것입니다. 그건 조금 이따가 보기로 합시다.

자기장의 경우 언제나 $\nabla\cdot\mathbf{B}=0$가 성립합니다. 따라서 시간에 대한 의존과 상관없이 벡터퍼텐셜을 $\mathbf{B}=\nabla\times\mathbf{A}$와 같이 쓸 수 있습니다. 이를 다시 패러데이 법칙에 대입하면

$$\nabla\times\mathbf{E}=-\frac{\partial}{\partial t}(\nabla\times\mathbf{A}) $$

$$\nabla\times\left(\mathbf{E}+\frac{\partial \mathbf{A}}{\partial t} \right)=0 $$

이 성립하게 됩니다. 따라서 스칼라 퍼텐셜을

$$\mathbf{E}+\frac{\partial \mathbf{A}}{\partial t}=-\nabla V$$

로 정의할 수 있습니다. 따라서 전기장 $\mathbf{E}$는

$$\mathbf{E}=-\nabla V-\frac{\partial \mathbf{A}}{\partial t}$$

로 쓰여집니다.

이렇게 퍼텐셜 형태로 쓴 전기장과 자기장을 맥스웰 방정식에 대입시켜봅시다. $\nabla\times\mathbf{E}=-\frac{\partial \mathbf{B}}{\partial t}$과 $\nabla\cdot\mathbf{B}=0$은 이미 사용했으니 남은 두 식에만 대입해보면 되겠습니다.

첫번째로 가우스 법칙에 대입하면

$$\nabla^2 V+\frac{\partial}{\partial t}(\nabla\cdot\mathbf{A})=-\frac{1}{\epsilon_0}\rho$$

를 얻고, 이는 푸아송 방정식에 대응됩니다. 두번째로 앙페르 법칙에 대입하면

$$\nabla\times(\nabla\times\mathbf{A})=\mu_0 \mathbf{J}-\mu_0\epsilon_0 \nabla\left(\frac{\partial V}{\partial t}\right)-\mu_0\epsilon_0 \frac{\partial^2 \mathbf{A}}{\partial t^2}$$

이고, $\nabla\times(\nabla\times\mathbf{A})=\nabla(\nabla\cdot\mathbf{A})-\nabla^2\mathbf{A}$이므로

$$\left(\nabla^2 \mathbf{A}-\mu_0\epsilon_0\frac{\partial^2 \mathbf{A}}{\partial t^2} \right)-\nabla\left(\nabla\cdot\mathbf{A}+\mu_0\epsilon_0\frac{\partial V}{\partial t} \right)=\mu_0\mathbf{J}$$

를 얻습니다. 비록 방정식이 좀 복잡해보이긴 하지만 퍼텐셜을 사용함으로써 전기장과 자기장 각각 3개의 성분을 구해야 했던 문제가 스칼라 퍼텐셜과 벡터 퍼텐셜 성분 3개, 총 4개의 성분을 구하는 문제로 바뀌었습니다. 구해야 할 성분이 두개나 줄었어요! 좋은 소식입니다. 그런데 가만히 살펴보니 전기장과 자기장이 하나로 주어지더라도 퍼텐셜이 유일하게 주어지지 않습니다. 이게 무슨 말이냐구요?

$$\mathbf{E}+\frac{\partial \mathbf{A}}{\partial t}=-\nabla V,\enspace \mathbf{B}=\nabla\times\mathbf{A}$$

퍼텐셜은 맥스웰 방정식으로부터 위와 같이 정의되었다는 것을 기억하실겁니다. 지금은 전기장과 자기장이 먼저 주어져있다고 생각합시다. 이 때 퍼텐셜을 구하려면 적분을 통해 구하면 될 것입니다. 그런데 이 과정에서 퍼텐셜에 적분상수같은 역할을 하는 항들이 붙어나올 수 있기 때문에 퍼텐셜이 유일하게 결정되지 않습니다. 물론 이 '항'이 만족해야 할 조건이 있습니다. 이렇게 퍼텐셜을 선택할 수 있는 자유도가 존재하는데 이를 **게이지 자유도(Gauge freedom)**라고 부릅니다.

그럼 이제 이 '항'들이 가지는 조건이 무엇인지 알아볼 차레입니다. 이를 위해 두 퍼텐셜 $(V,\mathbf{A})$와 $(V',\mathbf{A}')$이 같은 전기장과 자기장을 준다고 가정합시다. 그렇다면

$$\mathbf{A}'=\mathbf{A}+\mathbf{\alpha},\quad V'=V+\beta$$

와 같이 쓸 수 있을 것입니다. 두 퍼텐셜이 같은 자기장을 주어야하기 때문에 $\mathbf{B}=\nabla\times\mathbf{A}$를 적용하면 $\mathbf{\alpha}$는

$$\nabla\times\mathbf{\alpha} =0$$

를 만족해야 합니다. 따라서 $\mathbf{\alpha}$는 어떤 $\lambda$에 대해

$$\mathbf{\alpha}=\nabla\lambda$$

와 같이 쓸 수 있습니다. 또한 두 퍼텐셜은 같은 전기장을 주어야하기 때문에

$$\nabla\beta + \frac{\partial \mathbf{\alpha}}{\partial t}=\mathbf{0} $$

$$\nabla\left(\beta + \frac{\partial\lambda}{\partial t} \right)=\mathbf{0} $$

또한 만족해야 합니다. 따라서 $\beta$는

$$\beta=-\frac{\partial \lambda}{\partial t} $$

로 주어집니다(물론 여기서 시간에만 의존하는 함수에 대한 자유도도 있지만, $\lambda$가 이 항을 포함한다고 생각하기로 합시다). 따라서

$$\mathbf{A}'=\mathbf{A}+\nabla\lambda\\V'=V-\frac{\partial V}{\partial t}$$

인 변환에 대해 전기장과 자기장이 불변한다는 것을 알아내었습니다. 이러한 변환을 **게이지 변환(Gauge transformation)**이라 부릅니다. 게이지 변환을 통해 위에서 얻어낸 퍼텐셜 형태의 맥스웰 방정식을 간단하게 만들 수 있는데, 이는 다음 포스팅에서 알아보겠습니다.



## Reference

[1] Introduction to electrodynamics 4th ed., David J. Griffiths, Cambridge Press, 2017
