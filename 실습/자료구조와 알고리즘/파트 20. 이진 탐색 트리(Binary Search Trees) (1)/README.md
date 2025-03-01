# [어서와! 자료구조와 알고리즘은 처음이지?] <br> 20강 실습: 이진 탐색 트리의 원소 삽입 연산 구현

[문제 링크](https://school.programmers.co.kr/learn/courses/57/lessons/13797) 

### 구분

어서와 자료구조와 알고리즘은 처음이지? > 파트20. 이진 탐색 트리(Binary Search Trees) (1)

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

<hr>

### 문제설명
<p>초기 코드에 주어진 class Node 와 class BinSearchTree 를 기반으로, 이진 탐색 트리 (binary search tree) 에 새로운 원소를 삽입하는 insert(key, data) 연산의 구현을 완성하세요.

class BinSearchTree 에는 이미 insert(key, data) 메서드가 구현되어 있습니다. 이것을 그대로 이용하고, class Node 의 insert(key, data) 메서드를 재귀적 방법으로 구현하세요. 강의에서 언급한 바와 같이, 이미 트리 안에 들어 있는 것과 같은 (중복된) 키를 이용하여 삽입을 시도하는 경우에는 KeyError 예외를 발생시켜야 합니다.

[참고 1] inorder() 메서드의 구현은 그대로 두세요. 테스트에 이용됩니다.

[참고 2] solution() 함수의 구현도 그대로 두세요. 이것을 없애면 테스트가 되지 않습니다.

[참고 3] "코드 실행" 을 눌렀을 때 통과하는 것은 아무런 의미가 없습니다.</p>


> 출처: 어서와! 자료구조와 알고리즘은 처음이지?, https://school.programmers.co.kr/learn/courses/57
