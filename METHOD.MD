```
.swapcase()
- 메서드를 사용하여 대문자는 소문자로, 소문자는 대문자로 변환합니다.
```
```
.split()
- 문자열을 공백 기준으로 분리하여 리스트로 반환합니다.
```
```
enumerate(iterable, start=0)
- 반복 가능한 객체를 인덱스화 함께 순회하고 반환합니다.
- iterable: 인덱스를 부여하고 싶은 반복 가능한 객체.
- start: 인덱스의 시작 값. 기본값은 0입니다.
```
```
zip(iterables, iterables)
- 여러 개의 iterable 객체들을 동시에 순회할 수 있게 해준다.
- 각 iterable의 요소들을 묶어 튜플 형태로 반환한다.
```
```
str.startswith(prefix, start[,end])
- 문자열이 특정 접두사로 시작하는지를 확인하는 데 사용
- prefix : 확인하고자 하는 접두사 문자열
- start(선택적) : 검사할 시작 위치, 기본값 0
- end(선택적) : 검사할 끝 위치, 기본갑 문자열 끝
```
```
str.endswith(suffix[, start[, end]])
- 문자열이 특적 문자열로 끝나는지 여부를 확인
- True 혹은 False를 반환
- suffix : 확인하고자 하는 접마사 문자열, 튜플 제공 가능
- start(선택적) : 검사할 시작 위치, 기본값 0
- end(선택적) : 검사할 끝 위치, 기본값 문자 끝
```
```
separator.join(iterable)
- 리스트나 튜플 등의 이터러블(iterable) 객체의 요소들을 하나의 문자열로 결합하는 데 사용
- 각 요소는 지정된 구분자(separator)로 연결
- separator : 요소들을 결합할 때 사용할 문자열
- iterable : 문자열로 결합할 문자열들의 리스트, 튜플 또는 기타 이터러블 객체
```
```
str.lstrip([chars])
- 문자열의 왼쪽에서 특정 문자를 제거하는 데 사용
- 기본 호출 시 공백 제거
- 예시 : text.lstrip('0')
```
```
list_name.append(element)
- list_name : 요소를 추가할 리스트의 이름입니다.
- element : 리스트의 끝에 추가할 요소입니다.
- 리스트 자료형에서 사용되는 메소드
- 리스트의 끝에 새로운 요소를 추가하는 기능을 합니다.
```
```
abs(number)
- 숫자의 절댓값을 반환하는 함수이다.
```
```
list_name.extend(iterable)
- list_name : 기존 리스트의 이름
- iterable : 리스트에 추가할 요소들이 담긴 반복 가능한 객체
- 기존 리스트에 다른 리스트나 반복 가능한 객체의 모든 요소를 한꺼번에 추가하는 기능을 한다.
- 여러 요소를 한꺼번에 추가한다.
```