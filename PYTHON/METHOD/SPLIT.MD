# SPLIT

## 기본문법
```python
str.split(separator, maxsplit)
```
- separator
  - 문자열을 나눌 구분자
  - 생략 시 공백이 기본값
- maxsplit 
  - 문자열을 나눌 최대 횟수
  - 생략 시 전체를 나눔

## 동작 방식
- 구분자를 기준으로 문자열을 나눈다.
- 구분자를 지정하지 않으면 공백이 기본 구분자로 사용
- maxsplit 값을 지정하면 그 횟수만큼만 분할하며, 나머지 문자열은 마지막 요소로 반환된다.

## 예시
1. 공백을 기준으로 문자열 분할
```python
text = 'Python is fun'
result = text.split()
print(result)
```
> ['Python', 'is', 'fun']

2. 특정 구분자로 문자열 분할
```python
text = 'apple,banana,orange'
result = text.split(',')
print(result)
```
> ['apple', 'banana', 'orange']

3. `maxsplit` 사용
```python
text = 'apple,banana,orange,grape'
result = text.split(',', 2)
print(result)
```
> ['apple', 'banana', 'orange,grape'] 

4. 공백 문자열을 여러 개 포함한 경우
```python
text = '   Python    is    fun   '
result = text.split()
print(result)
```
> ['Python', 'is', 'fun']

5. 줄바꿈과 탭으로 분할
```python
text = 'Hello\tWorld\nPython'
result = text.split()
print(result)
```
> ['Hello', 'World', 'Python']

## 활용
- 텍스트 처리
  - cvs 데이터 처리
  - 로그 파일 분석
- 입력 처리
  - 사용자 입력을 여러 부분으로 나누어 처리해야 할 때 활용
- 문자열 분석
  - 긴 문장에서 단어 별로 나우거나 특정 패턴에 따라 구분