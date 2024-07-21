1. `git init`
- 현재 디렉토리를 앞으로 git 이 관리하는 디렉토리로 초기화하는 명령어
- window 폴더 -> 보기 -> 숨긴 항목을 체크 -> `.git` 폴더가 보인다.
- 변화를 본격적으로 추적

2. `git add`
- 확정 전 대기
- `git add .`
  - 맨 뒤에 `.` 을 입력하면 모든 파일을 Staging Area(확정 전 대기실)로 이동한다.

3. `git commit`
- 버전을 확정한다.
- 반드시 커밋 메세지를 함께 입력해야 한다.
- `git commit -m "first upload"`

4. `git status`
- 변경된 파일들의 상태를 한 눈에 확인

5. `git restore`
- 변경된 내용을 모두 삭제(이전 버전으로 돌리기)
- 실제 개발에서는 많이 쓰이지는 않는다!

6. `git log`
- commit 내역들을 한 눈에 확인
- `q` 를 누르면 git log 에서 탈출 가능하다.

7. `git commit --amend`
- 직전 커밋 메세지 수정 명령어
- 직전 커밋에서 누락된 파일을 추가함
  - 누락된 파일을 staging area 에 추가한 후 위 명령어를 입력
  - 누락된 파일까지 직전 커밋에 추가된다.
- 명령어 입력 시 vi 에디터가 열린다.
  - vi 명령어
    - `esc`: 명령 모드로 변경
      - `:wq`: 저장 후 종료
    - `i`: 입력 모드로 변경(현재 커서)
    - `a`: 입력 모드로 변경(바로 다음 위치로 커서)
8. it clone <주소>
- 원격 저장소 전체를 복사(다운로드)하는 것
- 최초 1번만 실행하면 된다.

9. git push/pull
- 원격 저장소에 변경사항 업로드/다운로드
- 최초 push/pull 진행 시, 어느 브랜치에 올려야 할 지 모름
  - 아래 명령어로 실행(이 후로는 그냥 git push/pull 만)
  - git push -u origin master
  - git pull origin master
  -u 옵션 : --set-upstream 
  (push/pull 은 origin 의 master 브랜치에서 가져오겠다.)

10. git remote add origin <주소>
- 원격 저장소와 로컬 저장소를 연동

11. git remote -v
- 연동 잘 되었는 지 확인하는 명령어