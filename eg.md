파이썬 스터디 연습문제
---------------------

### 2 - 간단한 함수 작성하기

 1. 일당 계산
    - 15% 세금을 계산하는 함수 작성하기.
    - 시급 5000원 알바가 h 시간 일했을때 받는 월급 계산하기.
 2. 원의 넓이 구하기
 3. 원 -> 달러 변환하기

### 4 - 함수와 변수를 섞어서 프로그램 작성하기
 1. 도넛 모양의 원의 면적을 구하기
 2. 티켓 프로그램
    * 영화관에서 $5 였을때 120명의 사람이 티켓을 산다.
    * $.10 감소 시킬때마다 15명이 더 티켓을 산다.
    * 영화관 주인은 영화 판권때문에 $180 를 쓴다
    * 관객 한명당 $0.04 를 소요하게한다.
    * 가장 많은 수입을 낼수있는 티켓 가격은?
 3. 뉴튼법 이용해서 제곱근 구하기
    * x의 제곱근을 구한다고 가정해보면
    * guess(추측값)과 (x / guess) 의 평균을구한다
    * x와 guess가 충분히 정확한지 확인하고
    * 충분하지않다면 다시 연산 or 충분하다면 값 반환
    * is_good_enough, average, improve 사용
    * if문, abs, pow 등의 내장함수와 조건문 사용해야함.
    * 재귀도 써야되는구나..

### 5 - 조건문과 함수

 1. 각종 구간 나타내는 함수 만들기
    * [0, 5]
    * (0, 5)
    * [0, 5)
 2. 간단한 2차방정식 x에 값이 유효한지 판단하기
    * x^2-2x+1=0
    * x^-9=0
 3. if ~ elif ~ else
    * 은행 이자 프로그램 - $1000 이하이면 4%의 이자, $5000 달러 미만이면 4.5%의 이자 $5000 이상이면 5%의 이자
    `interest(1000) == 4`
    `interest(4999) == 4.5`
 4. 근의 공식 이용해서 `ax^2 + bx + c`의 해의 근의 갯수 알아내기
 5. inline if ( a =  4 if True else 5)
 6. C에서 삼항연산 따라해보기 ( a =  4 or 5 , a = 0 and 4)
 7. 'a is not None'

### 6 - string 관련 연산

 1. [unicode][what-is-unicode] ? [utf-8][wiki-utf8]?
 2. `<type basestring>`
    * `<type 'unicode'>`
    * `<type 'str'>`
 3. `dir('hello world')`
    * `.format`
    * `.join`
    * `.replace`
    * `.startswith`
    * `.endswith`
    * `.split`
 4. `help()`


끝!


 [what-is-unicode]: http://www.unicode.org/standard/translations/korean.html
 [wiki-utf8]: http://en.wikipedia.org/wiki/UTF-8
