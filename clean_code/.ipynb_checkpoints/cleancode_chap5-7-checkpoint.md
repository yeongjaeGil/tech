## First Class Function
---
함수 자체를 argument로써 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴 할수도 있고, 함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있는 함수를 뜻한다.
```python
# -*- coding: utf-8 -*-
def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i)) # square 함수 호출, func == square
    return result

num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)

print(squares)
print(cubes)
print(quads)
```
- 퍼스트 클래스 함수를 사용하면 이미 정의된 여러 함수를 간단히 재활용할 수 있다는 장점이 있다.
- 이런 식으로 재활용이 가능하다. my_map과 같은 wrapper 함수만 정의하면 기존의 함수나 모듈을 수정할 필요없이 편리하게 쓸 수 있다.

```python
# -*- coding: utf-8 -*-
# 단순한 일반 함수
def simple_html_tag(tag, msg):
    print '<{0}>{1}<{0}>'.format(tag, msg)
    
simple_html_tag('h1', '심플 헤딩 타이틀')
print '-'*30

# 함수를 리턴하는 함수
def html_tag(tag):
    
    def wrap_text(msg):
        print '<{0}>{1}<{0}>'.format(tag, msg)
        
    return wrap_text

print_h1 = html_tag('h1') #1
print(print_h1) #2
print_h1('첫 번째 헤딩 타이틀') #3
print_h1('두 번째 헤딩 타이틀') #4
print_p = html_tag('p')
print_p('이것은 패러그래프 입니다.')
```

## Closure (클로저)
- 퍼스트 클래스 함수를 지원하는 언어의 네임 바인딩 기술. 어떤 함수를 함수 자시이 가지고 있는 환경과 함께 저장한 레코드이다.
- 함수가 가진 free variable을 클로저가 만들어지는 당시의 값과 레퍼런스 맵핑하여 주는 역할을 한다.
- 자신의 영역 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고 저장한 뒤, 이 캡처한 값들에 엑세스할 수 있게 도와준다.
- 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억할 수 있다.

```python
# -*- coding: utf-8 -*-
def outer_func(): #1
    message = 'Hi' #3
    
    def inner_func(): #4
        print (message) #6
        
    return inner_func #5

my_func = outer_func() #2
my_func() #7
my_func() #8
my_func() #9
```
- outer_func()을 인자 없이 호출
- message에 'Hi' 할당
- inner_func() 정의하고 return 값으로 inner_func()을 호출

- 클로저는 이렇게 하나의 함수로 여러가지의 함수를 간단히 만들어낼 수 있게 해주며, 기존에 만들어진 함수나 모듈을 수정하지 않고도 wrapper 함수를 이용해 커스터마이징할 수 있게 해준다.
- C) 머신러닝에서 어떻게 활용될 수 있는 지 명확하게 파악을 해봐야 한다.

```python
# -*- coding: utf-8 -*-

def outer_func(): #1
    message = 'Hi' #3
    
    def inner_func(): #4
        print message #6
        
    return inner_func #5

my_func = outer_func() #2
print my_func #7 <-- 추가
```
- 함수 자체를 반환한다.

Decorator
---
- 기존의 코드에 함수와 메서드를 쉽게 수정하기 위한 수단
    - 파라미터의 유효성 검사
    - 사전 조건 검사
    - 기능 전체를 새롭게 정의
    - 함수의 결과를 캐시
#### 함수 데코레이드

```python
# -*- coding: utf-8 -*-
def decorator_function(original_function):
    
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()
    
    return wrapper_function

def display_1():
    print('display_1 함수가 실행됐습니다.')
    
def display_2():
    print('display_2 함수가 실행됐습니다.')

display_1 = decorator_function(display_1)  #1
display_2 = decorator_function(display_2)  #2
display_1()
print(' ')
display_2()
```
- 하나의 데코레이터 함수를 만들어 display_1과 display_2 두개의 함수에 기능을 추가할 수 있다.
- 이를 간단히 하면 다음과 같다.

```python
# -*- coding: utf-8 -*-
def decorator_function(original_function):
    
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()
    
    return wrapper_function

@decorator_function  #1
def display_1():
    print('display_1 함수가 실행됐습니다.')

@decorator_function  #2
def display_2():
    print('display_2 함수가 실행됐습니다.')
# display_1 = decorator_function(display_1)  #3
# display_2 = decorator_function(display_2)  #4

display_1()
display_2()
```
- 여러개의 변수를 받고 싶을 경우
- *args, **kwargs를 통해서 multi arguments를 받아서 처리한다.

```python
# -*- coding: utf-8 -*-
def decorator_function(original_function):
    
    def wrapper_function(*args, **kwargs):  #1
        print '{} 함수가 호출되기전 입니다.'.format(original_function.__name__)
        return original_function(*args, **kwargs)  #2
    
    return wrapper_function

@decorator_function
def display():
    print 'display 함수가 실행됐습니다.'

@decorator_function
def display_info(name, age):
    print 'display_info({}, {}) 함수가 실행됐습니다.'.format(name, age)

display()
print('')
display_info('John', 25)
```

- 훨씬 더 깔끔하게 기능적으로 묶을 수 있다.
- 일반적으로 데코레이터는 로그를 남기거나 유저의 로그인 상태등을 확인하는데 사용함
- 프로그램의 성능을 테스트하기위해 많이 사용함

```python
# -*- coding: utf-8 -*-
import datetime
import time

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('John', 25)
```
- 이런식으로 실험을 진행할 경우 로그를 남기기에 용이하다. 
- 복수의 데코레이터를 스택해서 사용하면 아래쪽부터 실행된다.
- 이러한 현상을 방지하는 것이 functools 모듈의 wraps 데코레이터이다.

```python
# -*- coding: utf-8 -*-
from functools import wraps
import datetime
import time


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)
    
    @wraps(original_function)  #1
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)  #2
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper

@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('Jimmy', 30)  #3
```
- @wraps(original_function) 데코레이터를 추가해준다.

#### 클래스 데코레이터
- 함수에 적용한 것 처럼 클래스에도 데코레이터를 사용할 수 있다. 유일한 차이점은 데코레이터 함수의 파라미터로 함수가 아닌 클래스를 받는다.
- 클래스 데코레이터를 사용하면 여러 클래스가 특정 인터페이스나 기준을 따르도록 강제할 수 있다. 여러 클래스에 적용할 검사를 데코레이터에서 한 번만 하면 된다.
- 당장은 작고 간단한 클래스를 생성하고 나중에 데코레이터로 기능을 보강할 수 있다.
- 어떤 클래스에 대해서는 유지보수 시 데코레이터를 사용해 기존 로직을 훨씬 쉽게 변경할 수 있다.

- 데코레이터 객체

```python
class WithRetry:
    
    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exception=None):
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)
        
    def __call__(self, operation):
        @wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(self.retries_limit):
            try:
                return operation(*args, **kwargs)
            except self.allowed_exceptions as e:
                logger.info("retrying %s due to %s", operation, e)
                last_raised = e
            raise last_raised
        return wrapped
    
@WithRetry(retries_limit=5)
def run_with_custom_retries_limit(task):
    retun task.run()
```
- @ 연산 전에 전달된 파라미터를 통해 데코레이터 객체를 생성한다. 데코레이터 객체는 __init__ 메서드에서 정해진 로직에 따라 초기화
- 그 다음 @ 연산이 호출
- run_with_custom_retries_limit 함수를 래핑하여 __call__ 매직 메서드를 호출
- __call__ 매직 메서드는 앞의 데코레이터에서 하던 것처럼 원본 함수를 래핑하여 우리가 원하는 로직이 적용된 새로운 함수를 반환
#### 우수 예제
- 파라미터 변환
- 코드 추적
- 파라미터 유효성 검사
    - 모니터링 하고자하는 함수의 실행과 관련됨.
    - 함수 지표 모니터링(CPU 사용률, GPU 사용률)
    - 함수의 실행 시간 측정
    - 언제 함수가 실행되고 전달된 파라미터는 무엇인지 로깅
- 재시도 로직 구현
- 일부 반복 작업을 데코레이터로 이동하여 클래스 단순화
- 모든 데코레이터, 특히 신중하게 설계되지 않은 데코레이터는 코드의 복잡성을 증가시킨다. 따라서, 이 복잡성이 가치가 있어야 한다.
- 재사용량이 많다는건 어떻게 알 수 있나? 코드 리팩토링할지 결정하는 기준은 무엇인가?
- 다음과 같은 사항을 고려했을 경우만 데코레이터 사용을 권한다
    - 처음부터 데코레이터를 만들지 않는다. 패턴이 생기고 데코레이터에 대한 추상화가 명확해지면 그 때 리팩토링 한다.
    - 데코레이터가 적어도 3회 이상 필요한 경우에만 구현
    - 데코레이터 코드는 최소한으로 유지한다.
#### 데코레이터와 관심사의 분리
- 코드 재사용의 핵심은 응집력이 있는 컴포넌트를 만드는 것이다.
- 즉, 최소한의 책임을 가져서 오직 한 가지 일만 해야하며, 그 일을 잘해야 한다.
- 컴포넌트가 작을수록 재사용성이 높아진다.
- 결합과 종속성을 유발하고 소프트웨어의 유연성을 떨어뜨리는 추가 동작이 필요 없이 여러 상황에 쓰일 수 있다.

```python
def log_execution(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("started execution of %s", function.__qualname__)
        return function(*kwargs, **kwargs)
    return wrapped

def measure_time(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        logger.info("function %s took %.2f", function.__qualname__,time.time()-start_time)
        return result
    return wrapped
@measure_time
@log_excution
def operation():
    # some thing
    pass
```
#### 좋은 데코레이터 분석
- 훌륭한 데코레이터가 갖춰야 할 특성
    - 캡슐화와 관심사의 분리: 좋은 데코레이터는 실제로 하는 일과 데코레이팅하는 일의 책임을 명확히 구분해야 한다. 어설프게 추상화를 하면 안된다. 즉, 데코레이터의 클라이언트는 내부에서 어떻게 구현했는지 전혀 알 수 없는 블랙박스 모드로 동작해야 한다.
    - 독립성: 데코레이터가 하는 일은 독립적이어야 하며 데코레이팅되는 객체와 최대한 분리되어야 한다.
    - 재사용성: 데코레이터는 하나의 함수 인스턴스에만 적용되는 것이 아니라 여러 유형에 적용 가능한 형태가 바람직하다. 왜냐하면 하나의 함수에만 적용된다면 데코레이터가 아니라 함수로 대신할 수도 있기 때문이다. 충분히 범용적이어야 한다.
---
Descriptor
---
- 다른 언어에서도 생소한 개념
- 파이썬의 객체지향 수준을 한 단계 더 끌어올려주는 혁신적인 기능으로 이 기능을 잘 활용하면 보다 견고하고 재사용성이 높은 추상화를 할 수 있다.
- 디스크립터의 기능을 제대로 활용하는 예는 라이브러리나 프레임워크에서 많이 발견할 수 있다.
    - C) 라이브러리 코드 파악할 때 도움이 될 듯
- 디스크립터를 활용한 코드 재사용 방법
- 디스크립터의 좋은 사용 예를 살펴보고 자체 라이브러리의 API에 어떻게 활용할 수 있는 지 살펴본다.

#### 디스크립터 매커니즘
- 동작방식은 복잡하지 않는데, 세부 구현 시 주의사항이 많다.
- 디스크립터를 구현하려면 최소 두 개의 클래스가 필요
    - 클라이언트 클래스는 디스크립터 구현의 기능을 활용한 도메인 모델로 솔루션을 위해 생성한 일반적인 추상화 객체.
    - 디스크립터 클래스는 디스크립터 로직의 구현체이다.
    - 단지 디스크립터 프로토콜을 구현한 클래스의 인스턴스. 이 클래스는 다음 매직 메서드 중 최소 한 개 이상을 포함해야함
        - __get__
        - __set__
        - __delete__
        - __set_name__


---
Generator
---
- 프로그램 성능을 향상시키는 제너레이터 만들기
- 고성능이면서도 메모리를 적게 사용하는 반복을 위한 방법(메모리를 줄이기 위해)
- 제너레이터는 한 번에 하나씩 구성요소를 반환해주는 이터러블을 생성해주는 객체
- 거대한 요소를 한꺼번에 메모리에 저장하는 대신 특정 요소를 어떻게 만드는지 아는 객체를 만들어서 필요할 때마다 하나씩만 가져오는 것이다.

```python
# 현재 구현하고자 하는 함수: pusrchase정보를 '하나씩' 받아서 업데이트 시킴
def _load_purchase(filename):
    purchases = []
    with open(filename) as f:
        *_, price_raw = line.partition(",")
        purchases.append(float(price_raw))
    return purchases

# 파일에서 모든 정보를 읽어서 리스트에 저장한다. 그러나 성능에 문제가 있다. 파일에 상당히 많은 데이터가 있다면 로드하는데 시간이 오래 걸리고 메인 메모리에 담지 못할 만큼 큰 데이터일 수도 있다. 그러면 purchases를 하나씩 들고가서 들고 있을 이유가 없다.

def load_purchases(filename):
    with open(filename) as f:
        for line in f:
            *_, price_raw = line.partition(',')
            yield float(price_raw)
# 이렇게 수정하면 메모리 사용량이 급격하게 떨어진다. 결과를 담을 리스트가 필요 없어졌으며 return 문 또한 사라졌다.
# 이 경우 load_purchases 함수를 제너레이터 함수 또는 제너레이터라고 보른다
```
- 어떤 함수라도 yield를 붙이면 제너레이터 함수가 된다.
- 모든 제너레이터 객체는 이터러블(iterable)이다.
    - 이터러블은 for 루프와 함께 사용할 수 있다.
    - 이터러블을 사용하면 다형성을 보장하는 이와 같은 강력한 추상화가 가능하다
#### 제너레이터 표현식
- 제너레이터를 사용하면 많은 메모리를 절약할 수 있다. 리스트나 튜플, 세트처럼 많은 메모리를 필요로 하는 이터러블이나 컨테이너의 대안이 될 수 있다.
- list comprehension에 의해 정의될 수 있는 리스트나 세트, 사전처럼 제너레이터도 제너레이터 표현식으로 정의할 수 있다. 
```python
>>> [x**2 for x in range(10)]
>>> (x**2 for x in range(10))
>>> sum(x**2 for x in range(10))
```
---
test coder 만들기
---

``` python
#예외처리 코드
try:
    print(logger) #해당 함수
except NameError: #해당 기능에서 나올 수 있는 에러를 넣는다.
    print('NameError: logger는 존재하지 않습니다.')
```