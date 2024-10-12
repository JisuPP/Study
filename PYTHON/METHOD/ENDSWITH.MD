# ENDSWITH

## 문법
```python
string.endswith(suffix[, start[, end]])
```
- suffix
  - 검사할 접미사
  - 문자열 또는 튜플 형태
- start
  - 검사할 문자열의 시작 위치
  - 기본값 : 문자열의 처음
- end
  - 검사할 문자열의 끝 위치
  - 기본값 : 문자열의 끝

## 반환값
- 문자열이 지정된 접미사로 끝나면 `True`를 반환
- 그렇지 않은 경우 `False`를 반환

## 예시
1. 기본 사용법
```python
text = 'Python is fun'
print(text.endswith('fun'))
print(text.endswith('Fun'))
```
```
True
False
```

2. `start`와 `end`를 사용하는 경우
```python
text = 'Python is fun'
print(text.endswith('is', 0, 9))
print(text.endswith('Python', 0, 6))
```
```
True
False
```

3. 튜플을 사용하여 여러 접미사 확인
```python
text = 'document.pdf'
print(text.endswith(('.pdf', '.docx')))
print(text.endswith(('.jpg', '.png')))
```
```
True
False
```

4. 문자열의 특정 범위에서 검사
```python
text = 'Hello, world!;
print(text.endswith('world!', 0, 12))
```
> True

## 활용
- 파일 확장자 검사
  - 파일이 특정 확장자로 끝나는지 확인할 때 사용
```python
file_name = 'example.txt'
if file_name.endswith('.txt'):
    print('This is a text file.')
```
> This is a text file.

- URL 확인
  - URL이 특정 도메인이나 경로로 끝나는지 검사할 때 사용
```python
url = 'https://www.example.com/index.html'
if url.endswith('.html'):
    print('This is an HTML page.')
```
> This is an HTML page.

- 문자열 필터링
  - 데이터셋이나 리스트에서 특정 접미사로 끝나느 데이터를 추출할 때 활용