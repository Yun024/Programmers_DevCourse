## Docker 설치 전 확인
### Windows 기능 활성화
제어판 -> 프로그램 -> 프로그램 및 기능 -> Windows 기능 켜기/끄기 클릭

### BIOS설정 -> CPU가상화 활성화 하기
1. 컴퓨터를 부팅하고 `F2` or `Del` 키를 연타하여 BIOS셋팅에 접속
2. 내 컴퓨터 메인보드의 SVM모드 활성화 방법 검색
- Intel CPU 
        +  Intel (VMX) Virtualization Technology, Intel VT-x 또는 VMX 찾아서 활성화
- AMD CPU 
    + AMD Secure Virtual Machine, AMD SVM 또는 SVM Mode  찾아서 활성화
- 내 컴퓨터(B450M MORTAR MAX (MS-7B89))
    + cmd창에서 `wmic baseboard get product` 명령어를 통해 메인보드 확인
    + BIOS - Advanced모드 - OC - CPU Features - SVM Mode`Enabled`

### WSL2 설치
1. Powershell을 **관리자 권한**으로 실행
2. `wsl --install` 명령어를 통해 wsl 설치
3. `wsl --set-default-version 2` WSL 버전 기본값을 2로 변경
4. `wsl --version`을 통해 제대로 설치되었는지 확인



## Docker 설치하기
1.[Docker Homepage](https://www.docker.com/products/docker-desktop/)에서 AMD64 다운받기
11
2. 설치 시작 화면: WSL2를 Backend로 사용하는 것을 추천
22
3. 설치가 끝난 후 컴퓨터를 재시작
33 44 




## 윈도우에서 Docker 실행 두 가지 옵션
- WSL2 백엔드
    + Windows Subsystem For Linux(선호됨)
- Hyper-V 백엔드와 윈도우 컨테이너
    + 마이크로소프트의 Virtual Machine(가상 머신)시스템
    + 무겁고 이미지가 빌딩된 OS에 따라 라이센스 비용이 발생할 수 있음

## Docker 셋팅 확인
### 실행확인
- Docker 아이콘이 메뉴바에서 보이는지 확인
- 터미널(Power shell)에서 `docker version`명령 실행

### 자원할당 확인
- Docker Settings(우측 상단) -> 왼쪽 메뉴 Resources선택
    + CPU.Memory, Disk를 Docker에게 얼마나 할당할지는 WSL2 Backend에서 지정
11 
22

### 백엔드 확인
- Docker Settings(우측 상단) -> 왼쪽 메뉴 General선택 - 스크롤 중간 쯤
