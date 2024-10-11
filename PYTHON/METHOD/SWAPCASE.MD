# SWAPCASE

## 동작 방식
- 문자열에 포함된 모든 문자의 대소문자를 반대로 변환
- 대문자는 소문자, 소문자는 대문자로 변환
- 대문자나 소문자가 아닌 문자는 변환되는 않고 그대로 유지

## 사용법
```python
text = 'Hello World!'
result = text.swapcase()
print(result) 
```
> 'hELLO wORLD!'

## 예시
1. 기본 사용
```PYTHON
text = 'Python is FUN!'
print(text.swapcase())
```
> 'pYTHON IS fun!'

2. 혼합된 대소문자
```python
text = 'hACKeRRank'
print(text.swapcase())
```
> 'HackErRANK'

3. 숫자와 기호가 포함된 경우
```python
text = '12345!@#$%'
print(text.swapcase())
```
> '12345!@#$%'

## 활용
- 대소문자가 섞인 문자열을 다룰 때 대소문자 변환을 한번에 처리할 수 있어 유용
- 가독성을 높이거나, 특정한 변형을 적용할 때 사용