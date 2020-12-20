---
title : "1.1 Classical harmonic chain : phonons"
categories :
    - Condensed mattehr field theory
author_profile : true
toc : true

---

# 1.1 Classical harmonic chain : phonons

고체로 이루어진 어떤 계의 해밀토니안은 다음과 같이 주어진다.

$$H = H_e + H_i + H_{ei} \\
\begin{cases}
H_e = \sum_i \frac{\bold{p}_i^2}{2m} + \sum_{i<j}V_{ee}(\bold{r}_i-\bold{r}_j),\\
H_ i= \sum_I \frac{\bold{p}_I^2}{2m} + \sum_{I<J}V_{ii}(\bold{R}_I-\bold{R}_J),\\
H_{ei} = \sum_{iI}V_{ei}(\bold{R}_I-\bold{r}_i)
\end{cases}$$

실제로는 스핀에 의한 기여, 무질서도나 결함에 의한 기여 등 고려하지 않은 여러 상호작용이 있을 테지만 지금은 위의 경우만 고려하기로 하자. 주어진 해밀토니안을 보면 전자-전자 상호작용, 전자-이온 상호작용, 이온-이온 상호작용 이렇게 세가지의 상호작용이 나타난다는 것을 알 수 있다. 지금은 그 중에서도 고체 내에서 격자를 이루고 있는 이온간의 상호작용만을 떼서 고전적인 입자로 생각해 볼 것이다. 문제를 간단히 하기 위해서 이온 사이의 평균 간격이 $a$인 1차원의 이온 사슬을 생각하자. 그리고 이온들끼리의 상호작용만 고려하기로 했기 때문에 $H_e = H_i = 0$으로 둔다. 

만약에 이 시스템의 온도가 $0K$이라면 각 이온은 움직임 없이 자신의 자리에 고정되어 있을 것이다. 온도가 조금 올라갔다고 생각하면 각 이온들은 온도에 해당하는 열에너지만큼 자신의 평균 위치에서 조금 벗어나 진동할텐데, 이 때의 에너지는 2차 함수 형태로 근사할 수 있을 것이다. 그리고 이 때 계의 해밀토니안은 다음과 같이 쓰여진다.

$$H = \sum_{I=1}^N \lbrack \frac{P_I^2}{2M}+\frac{k_s}{2}(R_{I+1} - R_{I} - a)^2 \rbrack$$

이 해밀토니안은 각각 질량 $M$을 가진 입자 $N$개가 탄성 계수 $k_s$인 용수철로 연결되어 있는 모습을 나타낸다. 위의 해밀토니안을 가지고 해밀턴 방정식을 풀면 이들의 운동을 알아내는 것이 가능은 하겠지만, 일반적인 고체 내에서 이 방법을 사용해서 풀 수 있는 문제는 몇 되지 않는다. 따라서 우리는 해밀토니안이 아닌 라그랑지언의 시간적분으로 주어지는 액션이라는 것을 도입해서 이 문제를 탐구하고자 한다.

### Lagrangian formulation and equation of motion

지금의 경우에 시스템의 라그랑지안은 다음과 같이 주어진다.

$$L = \sum_I P_I\dot{R_I}-H = \sum_{I=1}^N \lbrack \frac{M\dot{R_I}^2}{2} - \frac{k_s}{2}(R_{I+1} - R_{I} - a)^2 \rbrack$$

그리고 이를 시간 영역 $[0,t_0]$에서 적분하면 라그랑지안의 액션을 얻는다.

$$S = \int_0^{t_0} dt L(R,\dot{R}) \qquad where\enspace (R,\dot{R}) =\{R_I,\dot{R_I}\} $$

그리고 우리는 입자의 갯수 $N$이 상당히 많은 계를 다루기 때문에 시스템의 경계조건은 무시하기로 하자. 게다가 격자의 진동이 매우 약하다면 이들 이온은 자신의 중심 위치에서 크게 벗어나지 않을 것이다.(즉 $|R_I(t)-\bar{R_I}| \ll a$) 그리고 $R_I(t) = \bar{R_I} + \phi_I(t)$를 위 라그랑지안에 대입하면

$$L = \sum_{I=1}^N \lbrack \frac{M}{2}\dot{\phi_I^2} - \frac{k_s}{2}(\phi_{I+1} - \phi_{I})^2 \rbrack.$$

그리고 이 시스템을 거시적 스케일에서 본다면 이 격자 사이의 간격 $a$를 매우 작다고 여길 수 있을테고, 그렇다면 $\phi$를 더이상 불연속적인 값이 아닌 연속적인 값으로 생각할 수 있을 것이다. 이렇게 $\phi$를 연속적인 값으로 여기게된다면, 원자 수준에서 일어나는 일들이 만들어내는 거시적인 현상을 탐구할 수 있다. 이 것을 continuum limit이라고 한다.

Continuum limit을 적용한다면 위에서 주어진 양들은 다음과 같이 변한다.

$$\phi_I \rarr a^{1/2}\phi(x)| _{x=Ia} ,\qquad \phi_{I+1} - \phi_I \rarr a^{3/2}\partial_x\phi(x)|_{x=Ia}, \qquad \sum_{I=1}^N \rarr \frac{1}{a}\int_0^Ldx.$$

이 때 $L = Na$이고 $\phi(x,t)$는 $[length]^{1/2}$의 차원을 가진다. 이 새로운 표현으로 라그랑지안을 다시 쓰면 다음과 같다.

$$L[\phi] = \int_0^L dx \mathcal{L}(\phi,\partial_x\phi,\dot{\phi}),\qquad \mathcal{L}(\phi,\partial_x\phi,\dot{\phi}) = \frac{m}{2}\dot{\phi}^2 - \frac{k_sa^2}{2}(\partial_x\phi)^2,$$

비슷하게, 이 라그랑지안의 액션은 다음과 같이 주어진다.

$$S[\phi] = \int dt L[\phi] = \int dt \int_0^L dx \mathcal{L}(\phi,\partial_x\phi,\dot{\phi})$$

이로써 연속적인 자유도를 갖는 $\phi$라는 (고전적) 장으로 $N$개의 이온 사슬에 대한 라그랑지안을 써 보았다. 이 라그랑지안이 계에 대한 정보를 다 가지고 있기는 하지만, 이것 만으로는 계의 실제 거동을 알 수 없다. 라그랑지안으로부터 실제 물리적인 움직임을 알아내기 위해서는 라그랑지안을 통해 장의 운동방정식을 알아내야 한다. 장의 운동방정식이라는 개념이 정확히 무엇을 말하는지는 아직 모호하지만 고전적인 입자에서 적용했던 해밀턴의 원리를 장에서도 똑같이 적용해보기로 하자.

$x(t)$의 경로를 갖는 고전적인 점입자 하나가 라그랑지안 $L(x,\dot{x})$에 의해 기술된다고 하자. 해밀턴의 원리는 그 입자가 실제로 움직이는 경로는 액션을 최소화하는 방향으로 움직인다는 것을 말해준다. 즉 경계에서 $0$을 갖는 임의의 함수 $y$를 고려할 때,

$$\lim_{\epsilon \rarr 0} \frac{1}{\epsilon}(S[x+\epsilon y] - S[x])=0$$

위 식을 $\epsilon$에 대해 선형근사 했을 때 고전적 입자의 경로 $x(t)$는 다음과 같은 라그랑주 운동방정식을 만족해야 함을 알 수 있다.

$$\frac{d}{dt}(\partial_{\dot{x}}L) - \partial_x L = 0$$

위와 같은 논의를 이제 $\phi$에 적용시켜보자. 경계에서 $0$을 갖는 임의의 함수 $\eta$를 생각하고 $S[\phi+\epsilon \eta]$를 $\epsilon$에 대해 1차항 까지만 전개한 뒤 해밀턴의 원리를 적용하면 다음과 같은 식을 얻을 수 있다.

$$\lim_{\epsilon \rarr 0} \frac{1}{\epsilon}(S[\phi+\epsilon \eta] - S[\phi])=-\int dt \int_0^L dx(m\ddot{\phi} - k_sa^2\partial_x^2 \phi)\eta = 0$$

위 식이 임의의 $\eta$에 대해 성립해야 하기 때문에 괄호 안의 항이 0이 되어야 함을 알 수 있다. 그런데 괄호 안의 항을 보니 파동방정식의 형태다! 장에 대한 라그랑지안으로부터 해밀턴의 원리를 적용해봤더니 $\phi$가 파동방정식의 해임을 알게 되었다. 이로부터 $\phi$의 가장 기본적인 여기 상태는 진행파의 모양을 가진다는 것을 알 수 있고, 이는 저에너지 영역에서 이온들이 만들어내는 진동이 거시적인 파동을 만들어낸다는 결론에 이르렀다.

### Hamiltonian formalism

앞 절에서 이온들이 이어져 만들어진 조화 고체의 기본적인 여기 상태는 진행파의  형태를 띈다는 것을 확인했었다. 그 진행파에는 얼마의 에너지가 저장되어 있을까? 이 질문에 답하기 위해서는 다시 해밀토니안으로 돌아가야 한다. 시스템의 라그랑지안 밀도가 주어져있다면, 그 계의 정준 운동량 밀도는 해밀턴 방정식에 의해 다음과 같이 주어진다.

$$\pi(x) = \frac{\partial\mathcal{L}(\phi,\partial_x\phi,\dot{\phi})}{\partial \dot{\phi}(x)}$$

이 정준 운동량 밀도는 $\phi$와 비슷하게 연속적인 값을 가진다. 그리고 해밀토니안 밀도는 라그랑지안 밀도의 르장드르 변환으로 다음과 같이 정의된다.

$$\mathcal{H}(\phi,\partial_x\phi,\pi)= \left( \pi\dot{\phi} - \mathcal{L}(\phi,\partial_x\phi,\dot{\phi})\right)|_{\dot{\phi}=\dot{\phi}(\phi,\pi)}$$

그리고 해밀토니안 밀도를 시간에 대해 적분하면 계의 해밀토니안을 얻는다.

이렇게 다시 해밀토니안을 얻고 나면 우리는 진행파의 에너지를 얻을 수 있게 된다. 주어진 라그랑지안으로부터 해밀토니안을 구하면 다음과 같다.

$$H[\pi,\phi] = \int dx\left( \frac{\pi^2}{2m}+\frac{k_sa^2}{2}(\partial_x\phi)^2 \right). $$

만약 1차원에서 오른쪽으로 움직이는 진행파를 생각한다면 $\phi(x,t) = \phi_+(x-vt)$이고, $\pi(x,t)= -mv\partial_x\phi_+(x-vt)$이므로 $H[\pi,\phi] = k_sa^2 \int dx[\partial_x\phi_+(x)]^2$를 얻게 된다. 이는 우리가 기대했던 대로 시간에 의존하지 않고 양의 정부호성을 띈다는 것을 알 수 있다.

## Reference

[1] Condensed matter field theory, Alexander Altland & Ben Simons, Cambridge, 2010