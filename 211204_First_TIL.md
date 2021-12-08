# 211204 TIL 

## 1. git bash 설치
- 경로 설정 하기 [블로그 참고 : https://patiencelee.tistory.com/618]

- vi 편집기 명령어 정리 블로그
https://blockdmask.tistory.com/25

## 2. VScode와 git 연결
### VScode에서 git에 커밋하는 방법
1. Vscode에서 F1 -> __git clone__ 검색하고 브라우저에 접속하여 권한 허용
2. VScode에서 터미널을 열어(Ctrl+`) repository 연결된 것을 확인
3. 터미널에서 다음 명령어 순차적으로 입력
    * __git add .__ #모든 변경사항을 저장하겠다는 뜻
    * __git commit -m__ "메시지 내용" #로컬저장소에 저장
    * __git push origin__ #GitHub(클라우드)에 저장 // #git remote 명령어로 원격저장소명을 알 수 있다.

## 3. git bash 명령어

- git init //깃 생성..? 선언? 그런 느낌

- git remote add origin 레파지토리주소 // https://github.com/아이디/레파지토리이름.git (로컬 저장소와 원격 저장소와 연결)

- git status //현재 깃 상태를 체크한다.

- git add . //변경된 파일들 모두 트랙킹

- git commit -m "커밋메시지" //커밋 메시지 설정

- git push origin master //깃은 pull과 push가 있는데 원격으로 올리는 것을 push라 한다.

- git pull origin master

## 4. 깃허브 블로그 만들기

- repository 생성하기