# [어서와! 자료구조와 알고리즘은 처음이지?] <br> 10강 실습: 양방향 연결 리스트 노드 삭제
[문제 링크](https://school.programmers.co.kr/learn/courses/57/lessons/13784) 

### 구분

어서와 자료구조와 알고리즘은 처음이지? > 파트10. 양방향 연결 리스트(Doubly Linked Lists)

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

<hr>

### 문제설명
<p>제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여 node 의 삭제 연산에 관련한 아래와 같은 메서드들을 구현하세요.

`popAfter()`
`popBefore()`
`popAt()`

popAfter(prev) 는 인자 prev 에 의하여 주어진 node 의 다음에 있던 node 를 삭제하고, popBefore(next) 는 인자 next 에 의하여 주어진 node 의 이전에 있던 node 를 삭제합니다. 그리고 삭제되는 node 에 담겨 있던 data item 을 리턴합니다.

popAt(pos) 는 인자 pos 에 의하여 지정되는 node 를 삭제하고 그 node 에 담겨 있던 data item 을 리턴하는데, 위 popAfter() 또는 popBefore() 를 호출하여 이용하는 방식으로 구현하세요. 또한, 만약 인자 pos 가 올바른 범위 내에 있지 않은 경우에는 raise IndexError 를 이용하여 IndexError exception 을 일으키도록 구현하세요.

테스트 케이스 1-3 은 각각 (1) popAfter(), (2) popBefore(), (3) popAt() 메서드의 올바른 동작을 검증하는 케이스입니다.</p>


> 출처: 어서와! 자료구조와 알고리즘은 처음이지?, https://school.programmers.co.kr/learn/courses/57
