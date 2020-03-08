# 1865. 동철이의 일 분배

## 개요

------

동철이가 차린 전자회사에는 N명의 직원이 있다.

그런데 어느 날 해야할 일이 N개가 생겼다.

동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.

직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.

여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.

직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.

우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.

## 구현방법

------

Pem을 활용하여 계산하였다.

순열을 만든 다음 확률을 곱했는데 가지치기를 해주 었다. 

만약 info가 max_percentage 보다 작게 되면 더이상 할 필요가 없었기 떄문에 그만 두는 코드를 작성 하였다.



## 결과

------

20분

## 회고

------

```
if max_percentage >= info:
```

처음에 저부분에 = 을 뺴먹어서 계속 들어 갔었다 하지만 =을 추가하니 금방 해결 된 문제 였다.