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

### 8 - `for`

`list` 반복하기

```python
for x in ['a', 'b', 'c']:
    print x
```

`dict` 반복하기

```python
for k, v in {'a': 1, 'b': 2}.items():
    print k, v
````

`break` 나 `continue`

```python
for x in xrange(1, 10):
    if x % 2 == 0:
        continue
    if x == 0:
        break
    print x
```

`enumerate`는 리스트에 인덱스를 가지고올수있다.


```python
for i, x in enumerate(['a', 'b', 'c']):
    print 'index: %d, item: %d' % (i, x)
```

`zip`은 두개의 리스트를 합쳐서 `tuple`로 반환한다.

```python
a = ['a', 'b', 'c']
b = [1, 2, 3]
assert [('a', 1), ('b', 2), ('c', 3)] == zip(a, b)
```

`sorted`, `reversed` 는 반복가능한(iterative)한 자료들을 정렬할때 사용함.

### 9 lamba

익명함수, `lambda` 키워드를 사용해서 사용가능.

```
>>> lambda x: x * x
<function <lambda> at 0x1054e01b8>
>>> _(2)
4
```

`sorted`의 `key` 파라미터를 이용해서 복잡한 자료 정렬하기.


```python
a = ['c', 'b', 'a']
b = [2, 1, 3]
assert [('c', 2), ('b', 1), ('a', 3)] == zip(a, b)
sorted_zip = sorted(zip(a, b), key=lambda x: x[0])
assert [('a', 3), ('b', 1), ('c', 2)] == sorted_zip
sorted_zip = sorted(zip(a, b), key=lambda x: x[1])
assert [('b', 1), ('c', 2), ('a', 3)] == sorted_zip
```

### 10 list comprehension

```python
[x for x in ['a', 'b', 'c']]
```

`if`도 사용가능하고 이중 `for`, 삼중 `for`도 사용가능하다.

```python
[x for x in xrange(1, 10) if x % 2 == 0]
```

`map`은 첫번째 파라미터로 함수를받고 두번째인자로 반복가능한 자료를 받는다.

```python
assert [0, 1, 4, 9, 16 ... , 81] == map(lambda x: x * x, xrange(1, 10))
```

`filter`은 첫번째 파라미터로 함수를받고 함수가 true일때,
두번째 인자(반복가능한 자료)의 아이템을 반환한다.

```python
assert [1, 3, 5, 7, 9] == filter(lambda x: x % 2, xrange(1, 10))
```

`reduce`는 첫번째 인자에 함수를 실행시켜서 두번째 인자의 앞
인자부터 함수를 실행시킨결과를 반환한다.

```python
assert 55 == reduce(lambda x, y: x + y, xrange(1, 11))
```

끝!


### 11 파라미터를 넘기는 다양한 방법

`list`를 unpack 할 수 있음

```python
a = [1, 2, 3]
def x(a, b, c):
    assert 1 == a
    asssert 2 == b
    assert 3 == c
x(*a)
```

사실은 이렇겐 잘 안쓰고, 숫자가 정해지지않은 인자를 받을때 이렇게 씀

```python
def x(*args):
    assert 1 == args[0]
    assert 2 == args[1]
    assert 3 == args[3]
    assert isinstance(args, list)
x(1, 2, 3)
```

인자의 이름으로도 함수에 인자를 넘길수있음.

```python
def x(a, key):
    assert 1 == a
    assert 'b' == key
x(1, key='b')
x(a=1, key='b')
#x(a=1, 'b') => 이건 허용안됨, 이름으로 넘기는건 맨마지막에
```

`dict`도 unpack 할 수 있음.

```python
a = {'a': 1, 'b': 2, 'c': 3}
def x(a, b, c):
    assert 1 == a
    assert 2 == b
    assert 3 == c
x(**a) #x(a=1, b=2, c=3) 으로 작동함
```

함수 인자에 default 값을 지정 가능

```python
def x(a, b, c=3):
    assert 1 == a
    assert 2 == b
    assert 3 == c
x(1, 2)
```

이것도 `*args`같이 사용가능함

```python
def x(**kwargs):
    assert 1 == kwargs['a']
    assert 2 == kwargs['b']
    assert isinstance(kwargs, dict)
x(a=1, b=2)
```

마지막으로 `*args`, `**kwargs`를 믹싱

```python
def x(*args, **kwargs):
    assert 1 == args[0]
    assert 1 == kwargs['a']
x(1, a=1)
```

### 11 파라미터를 넘기는 다양한 방법

`list`를 unpack 할 수 있음

```python
a = [1, 2, 3]
def x(a, b, c):
    assert 1 == a
    asssert 2 == b
    assert 3 == c
x(*a)
```

사실은 이렇겐 잘 안쓰고, 숫자가 정해지지않은 인자를 받을때 이렇게 씀

```python
def x(*args):
    assert 1 == args[0]
    assert 2 == args[1]
    assert 3 == args[3]
    assert isinstance(args, list)
x(1, 2, 3)
```

인자의 이름으로도 함수에 인자를 넘길수있음.

```python
def x(a, key):
    assert 1 == a
    assert 'b' == key
x(1, key='b')
x(a=1, key='b')
#x(a=1, 'b') => 이건 허용안됨, 이름으로 넘기는건 맨마지막에
```

`dict`도 unpack 할 수 있음.

```python
a = {'a': 1, 'b': 2, 'c': 3}
def x(a, b, c):
    assert 1 == a
    assert 2 == b
    assert 3 == c
x(**a) #x(a=1, b=2, c=3) 으로 작동함
```

함수 인자에 default 값을 지정 가능

```python
def x(a, b, c=3):
    assert 1 == a
    assert 2 == b
    assert 3 == c
x(1, 2)
```

이것도 `*args`같이 사용가능함

```python
def x(**kwargs):
    assert 1 == kwargs['a']
    assert 2 == kwargs['b']
    assert isinstance(kwargs, dict)
x(a=1, b=2)
```

마지막으로 `*args`, `**kwargs`를 믹싱

```python
def x(*args, **kwargs):
    assert 1 == args[0]
    assert 1 == kwargs['a']
x(1, a=1)
```

### 12 데코레이터

사용방법, high order function?

```python
@decorator
def fn(x):
    print x

fn(1) # decorator(fn)(1)


@decorator(a=1)
def fn(x):
    print x

fn(1) # decorator(a=1)(fn)(1)
```

디버그할때 뭔가 이상하게 찍힌다. `functools.wraps` 사용해봅시다

### 13 class

 - 클래스 이름은 `PascalCase`로 적습니다.
 - 모든 클래스의 메소드는 `self`를 첫번째 인자로 받습니다. (자바에서 `this` 같은거)
 - 생성자는 `__init__`로 정의할수있습니다. 근데 자바마냥 오버로딩은 못해요.
 - 상속은 `class Human(Animal)` 같은 방식으로 받습니다. 물론 여러개도 받을수있습니다. `class HyoJun(Human, Animal)` 같이

 [what-is-unicode]: http://www.unicode.org/standard/translations/korean.html
 [wiki-utf8]: http://en.wikipedia.org/wiki/UTF-8


 [what-is-unicode]: http://www.unicode.org/standard/translations/korean.html
 [wiki-utf8]: http://en.wikipedia.org/wiki/UTF-8
