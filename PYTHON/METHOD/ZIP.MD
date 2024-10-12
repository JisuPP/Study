# ZIP

## 문법
```python
zip(*iterables)
```
- iterables
  - 두 개 이상의 리스트, 튜플, 문자열 등 반복 가능한 객체

## 동작 방식
- 주어진 반복 가능한 객체들의 같은 인덱스에 있는 요소들을 튜플로 묶는다.
- 입력된 반복 가능한 객체 중 가장 짧은 길이에 맞춰 반환된다.
- 길이가 다른 경우에는 가장 짧은 객체의 길이만큼만 결과가 나온다.

## 반환값
- 튜플을 원소로 하는 zip객체(iterator)를 반환한다.
- 이 객체는 반복할 수 있다.
- 리스트나 다른 컬렉션 형태로 변환할 수 있다.

## 예시
1. 두 개의 리스트를 묶는 경우
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

result = zip(names, scores)
print(list(result))
```
> [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

2. 길이가 다른 리스트를 묶는 경우
```python
names = ['Alice', 'Bob']
scores = [85, 92, 78]

result = zip(names, scores)
print(list(result))
```
> [('Alice', 85), ('Bob', 92)] 

3. 여러 개의 리스트를 묶는 경우
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
ages = [20, 21, 22]

result = zip(names, scores, ages)
print(list(result))
```
> [('Alice', 85, 20), ('Bob', 92, 21), ('Charlie', 78, 22)]

4. `zip()`을 사용한 리스트 언패킹
```python
zipped = [('Alice', 85, 20), ('Bob', 92, 21), ('Charlie', 78, 22)]

names, scores, ages = zip(*zipped)
print(names)
print(scores)
print(ages)
```
```
('Alice', 'Bob', 'Charlie')
(85, 92, 78)
(20, 21, 22)
```

5. 문자열에서 `zip()` 사용
```python
str1 = 'ABC'
str2 = '123'

result = zip(str1, str2)
print(list(result))
```
> [('A', '1'), ('B', '2'), ('C', '3')]

6. `for` 루프와 함께 사용
```python
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f' {name} scored {score}')
```
```
Alice scored 85
Bob scored 92
Charlie scored 78
```

## 활용
- 데이터 병렬 처리
  - 여러 리스트나 반복 가능한 객체를 동시에 처리할 때 유용
- 코드 간결성
  - 인덱스를 수동으로 관리하지 않고 여러 컬렉션을 동시에 순회할 수 있어 코드를 더 깔끔하게 작성 가능
- 컬렉션 변환
  - 리스트, 튜플, 딕셔너리 등 다른 데이터 구조로 쉽게 변환 가능

## `zip()`을 사용한 딕셔너리 만들기
```python
keys = ['name', 'age', 'score']
values = ['Alice', 20, 85]

result = dict(zip(keys, values))
print(result)
```
> {'name': 'Alice', 'age': 20, 'score': 85}

- `zip()`은 입력된 반복 간으한 객체 중 가장 짧은 길이에 맞춰 작동
- 길이가 다른 객체를 사용할 경우 일부 요소가 무시될 수 있다.
- 더 긴 리스트나 아른 요소도 모두 포함하려면 `iteratool.zip_longest()`를 사용해야 한다.