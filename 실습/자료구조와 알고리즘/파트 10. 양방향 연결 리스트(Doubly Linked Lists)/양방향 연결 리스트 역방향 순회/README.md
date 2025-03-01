# [어서와! 자료구조와 알고리즘은 처음이지?] <br> 10강 실습: 양방향 연결 리스트 역방향 순회 
[문제 링크](https://school.programmers.co.kr/learn/courses/57/lessons/13782) 

### 구분

어서와 자료구조와 알고리즘은 처음이지? > 파트10. 양방향 연결 리스트(Doubly Linked Lists)

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

<hr>

### 문제설명
<p>제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여, 또한 강의 내용에서 언급한 reverse() 메서드를 구현하세요.

이 reverse() 메서드는 양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지 (tail 방향에서 head 방향으로) 순회하면서, 방문하게 되는 node 에 들어 있는 data item 을 순회 순서에 따라 리스트에 담아 리턴합니다.

예를 들어, DoublyLinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [62, 85, 43] 입니다.

이 규칙을 적용하면, 빈 연결 리스트에 대한 역방향 순회 결과로 reverse() 메서드라 리턴해야 할 올바른 결과는 [] 입니다.</p>


> 출처: 어서와! 자료구조와 알고리즘은 처음이지?, https://school.programmers.co.kr/learn/courses/57
