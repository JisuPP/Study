```python
str.swapcase()
- 메서드를 사용하여 대문자는 소문자로, 소문자는 대문자로 변환
```
```python
str.split()
- 문자열을 공백 기준으로 분리하여 리스트로 반환합니다.
```
```python
enumerate(iterable, start=0)
- 반복 가능한 객체를 인덱스화 함께 순회하고 반환합니다.
- iterable: 인덱스를 부여하고 싶은 반복 가능한 객체.
- start: 인덱스의 시작 값. 기본값은 0 입니다.
```
```python
zip(iterables, iterables)
- 여러 개의 iterable 객체들을 동시에 순회할 수 있게 해준다.
- 각 iterable의 요소들을 묶어 튜플 형태로 반환한다.
```
```python
str.startswith(prefix, start[,end])
- 문자열이 특정 접두사로 시작하는지를 확인하는 데 사용
- prefix : 확인하고자 하는 접두사 문자열
- start(선택적) : 검사할 시작 위치, 기본값 0
- end(선택적) : 검사할 끝 위치, 기본갑 문자열 끝
```
```python
str.endswith(suffix[, start[, end]])
- 문자열이 특적 문자열로 끝나는지 여부를 확인
- True 혹은 False를 반환
- suffix : 확인하고자 하는 접마사 문자열, 튜플 제공 가능
- start(선택적) : 검사할 시작 위치, 기본값 0
- end(선택적) : 검사할 끝 위치, 기본값 문자 끝
```
```python
separator.join(iterable)
- 리스트나 튜플 등의 이터러블(iterable) 객체의 요소들을 하나의 문자열로 결합하는 데 사용
- 각 요소는 지정된 구분자(separator)로 연결
- separator : 요소들을 결합할 때 사용할 문자열
- iterable : 문자열로 결합할 문자열들의 리스트, 튜플 또는 기타 이터러블 객체
```
```python
str.lstrip([chars])
- 문자열의 왼쪽에서 특정 문자를 제거하는 데 사용
- 기본 호출 시 공백 제거
- 예시 : text.lstrip('0')
```
```python
list_name.append(element)
- list_name : 요소를 추가할 리스트의 이름입니다.
- element : 리스트의 끝에 추가할 요소입니다.
- 리스트 자료형에서 사용되는 메소드
- 리스트의 끝에 새로운 요소를 추가하는 기능을 합니다.
```
```python
abs(number)
- 숫자의 절댓값을 반환하는 함수이다.
```
```python
list_name.extend(iterable)
- list_name : 기존 리스트의 이름
- iterable : 리스트에 추가할 요소들이 담긴 반복 가능한 객체
- 기존 리스트에 다른 리스트나 반복 가능한 객체의 모든 요소를 한꺼번에 추가하는 기능을 한다.
- 여러 요소를 한꺼번에 추가한다.
```
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
- 사전의 키와 값 쌍을 `(key, value)` 형태의 튜플로 구성된 뷰 객체로 반환
```
```python
divmod(a, b)
- 두 숫자를 입력받아 몫과 나머지를 한 번에 계산해주는 함수
- 튜플을 반환
- 첫번째 요소는 몫
- 두번째 요소는 나머지
```
```python
filter(function, iterable)
- fuction : 각 요소에 대해 평가할 함수. 각 요소를 입력받아 True or False를 반환
- iterable : 필터링할 반복 가능한 객체
```
```python
str.find(sub[, start[, end]])
- 특정 서브 스트링이 주어진 문자열 내에서 처음 등장하는 위치를 반환하는 데 사용
- sub : 찾고자 하는 서브스트링
- start : 선택사항. 검색을 시작할 인덱스
- end : 선택사항. 검색을 종료할 인덱스
- 서브 스트링이 발견되면 첫번째로 나타나는 위치를 반환
- 서브 스트링이 반견되지 않으면 `-1`반환
```
```python
eval(expression, globals=None, locals=None)
- 문자열로 표현된 표현식을 실행하고 그 결과를 반환하는 데 사용
- expression : 실행하고자 하는 표현식을 표함한 문자열
- globals : 선택사항. 전역 변수로 사용될 사전
- locals : 선택사항. 지역 변수로 사용될 사전
```
```python
str.isdigit()
- 문자열의 각 문자가 숫자인지 여부를 판단
- bool 형식으로 반환
```
```python
str.strip([chars])
- 문자열 양 쪽 끝에 있는 특정 문자를 제거
```
```python
import math
math.sqrt(x)
- 제곱근을 계한하는 함수
```
```python
import math
math.gcd(a, b)
- 두 수 의 최대 공약수 반환
```
```python
str.rfind(substring, start, end)
- 문자열에서 특정 부분 문자열(substring)이 마지막으로 등장하는 인덱스를 반환
- 문자열의 오른쪽에서부터 탐색 시작
- 첫 번째로 발견된 부분 문자열의 인덱스를 반환
- substring : 찾고자 하는 부분 문자열
- start : 선택사항, 탐색을 시작할 인덱스
- end : 선택사항, 종료할 인덱스
```
```python
list or str.index(value, start, end)
- 특정 값이 처음으로 등장하는 위치 반환
- value : 찾고자 하는 값
- start : 선택사항, 검색을 시작할 인덱스
- end : 선택사항, 검색을 종료할 인덱스
```
```python
import math
math.factorial(n)
- 주어진 정수 n에 대한 팩도리얼 값을 계산해 반환하는 함수
```