---
title : "통계물리 (4). Microstate and Entropy"
excerpt: "Thermodynamics and Statistical Mechanics by Greiner, Chap.5"
categories :
    - statistical physics
author_profile : true
toc : true
use_math : true
toc_sticky : true
comments : true
---

열역학의 관점에서 계의 특성은 $E,P,V,N$과 같은 양과 관련된 상태방정식을 통해 알아낼 수 있었다. 그리고 이들 상태방정식은 대부분 경험적으로 얻어낸 관계였다. 그러나 계를 구성하는 요소와 상호작용이 복잡해짐에 따라, 경험적인 데이터를 통해 방정식을 구성해내는 것에 한계가 생기게 되고 이와 같은 방식에 대한 물리적인 설명이 불충분하게 되었다. 따라서 계의 거시적인 특성보다는 원자 수준의 미시적ㅇ니 상호작용을 고려하게 되었다. 이로부터 통계역학이 출발하게 된다. 이번 포스팅에서는 통계역학을 구성하는데 필요한 기본 개념인 macrostate, microstate를 살펴보고 엔트로피를 통계역학적 관점에서 재구성해볼 것이다.

먼저 $N$개의 입자가 부피 $V$인 정육면체 내에서 움직이는 계를 생각해보자. 열역학적 관점에서 이 계의 특성은 몇가지의 변수로 주어졌다. 그리고 이 특성이 같은 값을 가진다면 계의 내부에너지, 엔트로피 등은 항상 같다고 할 수 있다. 이를 계의 macrostate라고 부른다. 계를 이루는 입자를 더 자세히 들여다보자. 각 입자들이 구별가능한(distinguishable) 고전적 입자라고 가정하면, 이 계의 상태는 $3N$개의 위치 $q_i$와 $3N$개의 운동량 $p_i$, 총 $6N$개의 값으로 나타낼 수 있다. 그리고 이 상태는 $6N$차원 위상공간 위의 한 점으로 표현해낼 수 있는데 이 하나의 점은 계의 microstate 하나에 대응된다. 그리고 시간이 지남에 따라 이 위상점은 다음과 같은 해밀턴 방정식을 따라 변화한다.

$$\dot{p}_j = -\frac{\partial H}{\partial q_j},\enspace \dot{q}_j = \frac{\partial H}{\partial p_j} ,\quad\text{for}\enspace j=1,\dots,3N.$$

이번에는 각각의 입자들의 운동으로 인해 생기는 압력을 살펴보자. 이 때 이 계가 열역학적 평형을 이루고 있는 상태라면 시간이 지남에 따라 벽에 작용하는 압력 $P$는 변하지 않는다. 그렇지만 계를 이루는 각각의 입자의 위치와 운동량은 시간이 지남에 따라 계속해서 변할 것이기 때문에 위상점은 머물러있지 않고 계속해서 운동하게 된다. 앞서 microstate 하나는 위상공간 내의 한 점에 해당한다고 했었다. 그런데, 시간이 지남에 따라 압력 $P$가 일정할 때에도 위상점이 변화하기 때문에 이 때 계의 macrostate는 하나로 주어진다. **즉, 하나의 macrostate에 대응되는 microstate는 매우 많다.**

예를 들어, 위와 같이 입자 $N$개로 이루어진 고립계를 생각하자. 계의 해밀토니안을 구성하고 나면, 이는 계의 전체 에너지에 대응된다. 그리고 해밀토니안은 각각 입자의 운동량에 의존하고, 이들의 시간 변화는 위의 해밀턴 운동방정식으로 주어진다. 이 계가 고립계이기 때문에 해밀토니안은 시간에 대해 독립적이므로 계의 전체 에너지

$$E=H(q_{\nu}(t),p_{\nu}(t))$$

를 상수로 취급할 수 있다. 즉, 위상점은 같은 에너지 $E$를 주는 자취를 따라서 이동한다. 일반적으로 어떤 물리량 $A(q_{\nu}(t),p_{\nu}(t),t)$의 시간 변화는

$$\frac{dA}{dt} = \frac{\partial A}{\partial t}+\sum_{\nu=1}^{3N}\left(\frac{\partial A}{\partial q_{\nu}}\dot{q}_{\nu}+\frac{\partial A}{\partial p_{\nu}}\dot{p}_{\nu} \right)$$

로 주어진다. 여기에 해밀턴 방정식을 대입하면,

$$\frac{dA}{dt} = \frac{\partial A}{\partial t}+\sum_{\nu=1}^{3N}\left(\frac{\partial A}{\partial q_{\nu}}\frac{\partial H}{\partial p_{\nu}}-\frac{\partial A}{\partial p_{\nu}}\frac{\partial H}{\partial q_{\nu}} \right)\\=\frac{\partial A}{\partial t} + \{A,H\}$$

가 성립한다. 이 때 $\{A,H\}$는 Poisson bracket이다. 만약 $A$가 $H$이면, $\partial H/\partial t =0$이고 $\{H,H\}=0$이기 때문에 에너지 보존 법칙이 성립한다. 








## Reference

[1] Thermodynamics and Statistical Mechanics, Greiner,Neise,and Stoecker, Springer-Verlag, 1995
   .


   