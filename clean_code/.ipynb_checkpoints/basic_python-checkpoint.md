## Magic Method
---
- 클래스 안에 정의할 수 있는 스페셜 메소드이며 클래스를 int, str, list등의 파이썬의 빌트인 타입과 같은 작동을 하게 해준다
- +,-,>,< 등의 오퍼레이터에 대해 각각 데이터 타입에 맞는 메소드로 오버로딩하여 백그라운드 연산 진행

```python
# -*- coding: utf-8 -*-
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return '아이템: {}, 가격: {}'.format(self.name, self.price)
    
    def __add__(self, other):
        return '가격 총합: {}'.format(self.price + other.price)
    def __lt__(self,other):
        if self.price < other.price:
            return True
        else:
            return False
food_1 = Food('아이스크림', 3000)
food_2 = Food('과자', 1000)

# 인스턴스 출력
print(food_1)
print(food_1+food_2)
print(food_1>food_2)
```

- 이런 식으로 원하는 방식으로 만들 수 있다.
- 더 간단하게 클래스들을 설계할 수 있다.
- magic method reference
- Table [magic-table](#appendix-magic-method)

---
## APPENDIX magic method
<table class="table table-striped table-hover">
	<caption>Binary Operators</caption>
	<thead>
		<tr>
			<th scope="col">Operator</th>
			<th scope="col">Method</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>+</td>
			<td>object.__add__(self, other)</td>
		</tr>
		<tr>
			<td>-</td>
			<td>object.__sub__(self, other)</td>
		</tr>
		<tr>
			<td>*</td>
			<td>object.__mul__(self, other)</td>
		</tr>
		<tr>
			<td>//</td>
			<td>object.__floordiv__(self, other)</td>
		</tr>
		<tr>
			<td>/</td>
			<td>object.__div__(self, other)</td>
		</tr>
		<tr>
			<td>%</td>
			<td>object.__mod__(self, other)</td>
		</tr>
		<tr>
			<td>**</td>
			<td>object.__pow__(self, other[, modulo])</td>
		</tr>
		<tr>
			<td>&gt;&gt;</td>
			<td>object.__lshift__(self, other)</td>
		</tr>
		<tr>
			<td>&lt;&lt;</td>
			<td>object.__rshift__(self, other)</td>
		</tr>
		<tr>
			<td>&amp;</td>
			<td>object.__and__(self, other)</td>
		</tr>
		<tr>
			<td>^</td>
			<td>object.__xor__(self, other)</td>
		</tr>
		<tr>
			<td>|</td>
			<td>object.__or__(self, other)</td>
		</tr>
	</tbody>
</table>
&nbsp;

<table class="table table-striped table-hover">
	<caption>Extended Assignments</caption>
	<thead>
		<tr>
			<th scope="col">Operator</th>
			<th scope="col">Method</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>+=</td>
			<td>object.__iadd__(self, other)</td>
		</tr>
		<tr>
			<td>-=</td>
			<td>object.__isub__(self, other)</td>
		</tr>
		<tr>
			<td>*=</td>
			<td>object.__imul__(self, other)</td>
		</tr>
		<tr>
			<td>/=</td>
			<td>object.__idiv__(self, other)</td>
		</tr>
		<tr>
			<td>//=</td>
			<td>object.__ifloordiv__(self, other)</td>
		</tr>
		<tr>
			<td>%=</td>
			<td>object.__imod__(self, other)</td>
		</tr>
		<tr>
			<td>**=</td>
			<td>object.__ipow__(self, other[, modulo])</td>
		</tr>
		<tr>
			<td>&lt;&lt;=</td>
			<td>object.__ilshift__(self, other)</td>
		</tr>
		<tr>
			<td>&gt;&gt;=</td>
			<td>object.__irshift__(self, other)</td>
		</tr>
		<tr>
			<td>&amp;=</td>
			<td>object.__iand__(self, other)</td>
		</tr>
		<tr>
			<td>^=</td>
			<td>object.__ixor__(self, other)</td>
		</tr>
		<tr>
			<td>|=</td>
			<td>object.__ior__(self, other)</td>
		</tr>
	</tbody>
</table>
&nbsp;

<table class="table table-striped table-hover">
	<caption>Unary Operators</caption>
	<thead>
		<tr>
			<th scope="col">Operator</th>
			<th scope="col">Method</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>-</td>
			<td>object.__neg__(self)</td>
		</tr>
		<tr>
			<td>+</td>
			<td>object.__pos__(self)</td>
		</tr>
		<tr>
			<td>abs()</td>
			<td>object.__abs__(self)</td>
		</tr>
		<tr>
			<td>~</td>
			<td>object.__invert__(self)</td>
		</tr>
		<tr>
			<td>complex()</td>
			<td>object.__complex__(self)</td>
		</tr>
		<tr>
			<td>int()</td>
			<td>object.__int__(self)</td>
		</tr>
		<tr>
			<td>long()</td>
			<td>object.__long__(self)</td>
		</tr>
		<tr>
			<td>float()</td>
			<td>object.__float__(self)</td>
		</tr>
		<tr>
			<td>oct()</td>
			<td>object.__oct__(self)</td>
		</tr>
		<tr>
			<td>hex()</td>
			<td>object.__hex__(self)</td>
		</tr>
	</tbody>
</table>
&nbsp;

<table class="table table-striped table-hover">
	<caption>Comparison Operators</caption>
	<thead>
		<tr>
			<th scope="col">Operator</th>
			<th scope="col">Method</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>&lt;</td>
			<td>object.__lt__(self, other)</td>
		</tr>
		<tr>
			<td>&lt;=</td>
			<td>object.__le__(self, other)</td>
		</tr>
		<tr>
			<td>==</td>
			<td>object.__eq__(self, other)</td>
		</tr>
		<tr>
			<td>!=</td>
			<td>object.__ne__(self, other)</td>
		</tr>
		<tr>
			<td>&gt;=</td>
			<td>object.__ge__(self, other)</td>
		</tr>
		<tr>
			<td>&gt;</td>
			<td>object.__gt__(self, other)</td>
		</tr>
	</tbody>
</table>
---