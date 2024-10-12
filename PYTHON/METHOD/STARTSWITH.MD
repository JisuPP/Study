# STARTSWITH

## 문법
```python
string.startswith(prefix[, start[, end]])
```
- prefix
  - 검사할 접두사
  - 문자열 또는 튜플 형태
- start
  - 검사할 문자열의 시작 위치
  - 기본값 : 문자열의 처음
- end
  - 검사할 문자열의 끝 위치
  - 기본값 : 문자열의 끝

## 반환값
- 문자열이 지정된 접두사로 시작하면 `True` 반환
- 그렇지 않은 경우 `False` 반환

## 예시
1. 기본 사용법
```python
text = 'Python is fun'
print(text.startswith('Python'))
print(text.startswith('python'))
```
```
True
False
```

2. `start`와 `end`를 사용하는 경우
```python
text = 'Python is fun'
print(text.startswith('is', 7))
print(text.startswith('Python', 7))
```
```
True
False
```

3. 튜플을 사용하여 여러 접두사 확인
```python
text = 'Python is fun'
print(text.startswith('Python', 'Java'))
print(text.startswith('Java', 'C++'))
```
```
True
False
```

4. 문자열이 특정 범위에서 시작하는지 검사
```python
text = 'Hello, world'
print(text.startswith('world', 7, 12))
```
> True

## 활용
- 파일 확장자 확인
  - 파일이 즉정 확장자로 시작하는지 확인할 때 유용
```python
file_name = 'example.txt'
if file_name.startswith('example'):
    print('This is an example file.')
```
> This is an example file
- URL 검사
  - URL이 특정 프로토콜로 시작하는지 확인할 때 사용
```python
url = 'http://www.example.com'
if url.startswith('http://'):
    print('This is a secure website.')
```
> This is a secure website.
- 데이터 필터링
  - 리스트나 데이터셋에서 특정 패턴으로 시작하는 데이터를 추출할 때 사용