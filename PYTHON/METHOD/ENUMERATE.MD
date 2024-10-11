# ENUMERATE

## 문법
```PYTHON
enumerate(iterable, start=0)
```
- iterable
  - 리스트, 튜플, 문자열 등 반봅 가능한 객체
- start
  - 인덱스의 시작 값을 설정
  - 기본값 : 0

## 반환값
- 인덱스와 해당 값을 튜플로 묶은 반복 가능한 객체를 반환

## 예시
1. 기본 사용법
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
```
0 apple
1 banana
2 cherry
```

2. `start` 인자를 사용하는 경우
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)
```
```
1 apple
2 banana
3 cherry
```

3. 문자열에서 사용
```python
text = 'Python'
for index, char in enumerate(text):
    print(f'Index : {index}, Character : {char}')
```
```
Index: 0, Character: P
Index: 1, Character: y
Index: 2, Character: t
Index: 3, Character: h
Index: 4, Character: o
Index: 5, Character: n
```

4. 리스트 내포와 함께 사용
```python
fruits = ['apple', 'banana', 'cherry']
indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
print(indexed_fruits)
```
> [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

5. 딕셔너리로 변환
```python
fruit = ['apple', 'banana', 'cherry']
indexed_fruits_dict = dict(enumerate(fruits))
print(indexed_fruits_dict)
```
> {0: 'apple', 1: 'banana', 2: 'cherry'}

## 활용
- 코드 간결성
  - 인덱스와 값을 동시에 처리
  - `range(len(list))`와 같은 방식보다 코드가 더 간결
- 유용한 디버깅
  - 인데스 정보와 데이터를 동시에 처리할 수 있어 데이터 처리 및 디버깅이 편리
- 리스트, 튜플, 문자열 등 반복 가능한 모든 객체에서 사용 가능