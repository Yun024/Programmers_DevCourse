# [어서와! 자료구조와 알고리즘은 처음이지?] <br> 9강 실습: dummy head를 가지는 연결 리스트 노드 삭제 
[문제 링크](https://school.programmers.co.kr/learn/courses/57/lessons/13781) 

### 구분

어서와 자료구조와 알고리즘은 처음이지? > 파트9. 연결 리스트(Linked Lists) (3)

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

<hr>

### 문제설명
<p>제 9 강에서 소개된 추상적 자료구조 LinkedList 는 dummy head node 를 가지는 연결 리스트입니다. 이 클래스의 아래와 같은 메서드들을, 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.

`popAfter()`<br>
`popAt()`

이 때, popAt() 메서드의 구현에서는 popAfter() 를 호출하여 이용하도록 합니다. (그렇게 하지 않을 수도 있지만, 여기에서는 popAfter() 의 이용에 의해서 코드 구현이 보다 쉬워지는 것을 확인하기 위함입니다.)

초기 코드로 들어 있는 것은 solution() 함수를 포함하여 다른 부분은 수정하지 말고, def popAfter(self, prev): 와 def popAt(self, pos): 의 메서드 몸체만 구현하세요.

만약, popAt() 메서드에 인자로 주어진 pos 가 올바른 범위의 값을 가지지 않는 경우에는 IndexError exception 을 발생시키도록 합니다. 이렇게 하기 위한 코드는 raise IndexError 입니다.</p>


> 출처: 어서와! 자료구조와 알고리즘은 처음이지?, https://school.programmers.co.kr/learn/courses/57
