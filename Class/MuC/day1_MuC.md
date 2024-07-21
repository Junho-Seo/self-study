# CLI (Command Line Interface)

- 터미널을 통해 사용자가 컴퓨터와 상호작용

## 경로

1. 루트 디렉터리 (`/`)
- 모든 파일과 폴더를 담고 있는 최상의 폴더
- 윈도우의 경우 보통 `C드라이브`
1. 홈 디렉터리 (`~`)
- 현재 로그인 된 사용자의 홈 폴더
- 윈도우 : `C:/사용자(Users)/현재 사용자 계정`
- MAC : `/Users/현재 사용자 계정`
1. 절대 경로 : 루트 디렉터리로부터 목적 지점까지의 경로
- ex) `C:/Users/사용자 계정/Desktop`
1. 상대 경로 : 현재 작업하고 있는 디렉터리 기준으로 계산된 경로
- `./` : 현재 작업하고 있는 폴더
- `../` : 현재 작업하고 있는 폴더의 부모폴더
- ex) `./SSAFY` (현재 작업 폴더에 있는 SSAFY폴더)

---

## 터미널 명령

1. touch : 파일 생성
- 띄워쓰기로 구분하여 여러 파일 한꺼번에 생성 가능
- 숨김 파일을 만들기 위해서는 `.`을 파일명 앞에 붙입니다.

```bash
touch text.txt

```

2.mkdir : 폴더 생성

- 띄어쓰기 구분해서 여러 폴더를 한꺼번에 생성 가능
- 폴더 이름에 공백을 넣고 싶은 경우 따옴표로 묶어서 입력

```bash
mkdir myFolder
mkdir 'ssafy start'

```

1. ls : 현재 디렉터리의 폴더 및 파일 목록 보여줌
- `a` : all 옵션. 숨김 파일까지 모두 보여줍니다.
- `l` : long 옵션. 용량, 수정 날짜 등 파일 정보를 자세히 보여줍니다.

```bash
#기본 사용
ls

#all 옵션
ls -a

# all과 long옵션 함께 사용
ls -a -l

# 여러 옵션 축약
ls -al

```

1. mv
- 폴더 또는 파일을 다른 폴더로 이동할 때 사용
- 폴더 및 파일 이름을 변경할 때 사용

```bash
# text.txt를 myFolder로 이동
mv text.txt myFolder

# myFolder를 testFolder로 이름 변경
mv myFolder testFolder

```

1. rm : 폴더 또는 파일 삭제
- 휴지동 이동 없이 완전 삭제
- ``를 사용해서 `rm *.txt` 입력 시 txt 파일 전체 삭제
- 와일드 카드
    - `` : 0개 이상의 문자를 대체할 수 있습니다.
    - `?` : 임의의 한 문자
    - `[abcd]` : 괄호 안의 문자 중 하나와 일치할 경우\
        - [abcd가].txt -> a.txt, b.txt, c.txt, d.txt, 가.txt
- `r` : 폴더 삭제 옵션

```bash
rm -r testFolder

```

1. start, open : 파일 또는 폴더 열기
- `window`에서 start, `Mac`에서 open

```bash
start test.txt

```

1. cd : 현재 작업 중인 디렉터리 변경
- `cd ~` : 홈 디렉터리로 이동
- `cd ..` : 부모 디렉터리로 이동
- `cd -` : 이동 전 디렉터리로 이동 (뒤로가기)

```bash
cd testFolder

```

---

## bash의 유용한 단축키

- `위, 아래 방향키` : 과거에 작성했던 명령어 조회
- `tab` : 폴더 및 파일 이름 자동 완성
- `ctrl + a`: 커서가 맨 앞으로 이동
- `ctrl + e`: 커서가 맨 뒤로 이동
- `ctrl + w`: 커서 앞 단어 삭제
- `ctrl + l` : 터미널 화면 청소
- `ctrl + insert` : 복사
- `shift + insert` : 붙여넣기


#############################################################


# Git 기초 내용

### git 설정

*   git config --global user.email "메일주소"
*   git config --global [user.name](http://user.name/) "유저네임"

### git global config 설정 확인

*   git config --global -l

* * *

### commit 내역 보기

*   전체 내역 : git log
*   한줄씩 내역 : git log --oneline

### commit 변경 사항 확인

*   git log -p -1(최근 몇개 커밋 볼건지 개수 지정)

### git commit 순서

1.  최초 1번 설정
    *   로컬저장소 초기화 : git init
    *   유저 이름 및 이메일 설정 : git config --global
2.  staging area에 추가 (커밋 하고 싶은 파일)
    *   git add 파일이름
3.  commit (변경사항저장)
    *   git commit -m "커밋 메시지"

* * *

### Stage Area에 있는 파일 Unstage하기

### `git rm --cached` vs `git restore --staged`

*   git rm --cached는 파일을 Git의 `추적 대상에서 완전히 제거`하는 데 사용되고, (커밋 이전에도 사용 가능)
*   git restore --staged는 `스테이징된 변경사항을 취소하는 데만` 사용됩니다. (커밋 이후에 사용 가능)
*   폴더 내의 모든 파일들 및 특정 파일들 선택하고 싶은 경우 와일드 카드 사용
    *   git rm --cached -r \* #-r은 폴더가 있는 경우 사용 (재귀적으로 폴더 내의 모든 파일 처리)
    *   git rm --cached \*.txt

* * *

Git 실습
======

### git log

*   커밋의 내역(`ID, 작성자, 시간, 메세지 등`)을 조회할 수 있는 명령어
*   옵션
    *   `-oneline` : 한 줄로 축약해서 보여줍니다.
    *   `-graph` : 브랜치와 머지 내역을 그래프로 보여줍니다.
    *   `-all` : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
    *   `-reverse` : 커밋 내역의 순서를 반대로 보여줍니다. (최신이 가장 아래)
    *   `p` : 파일의 변경 내용도 같이 보여줍니다.
    *   `2` : 원하는 갯수 만큼의 최근 내역을 보여줍니다. (2 말고 임의의 숫자 사용 가능)

* * *

### 원격 저장소 업로드

1.  원격 저장소 등록

*   `git remote add <이름> <주소>`
    *   git remote add origin [https://github.com/edukyle/TIL.git](https://github.com/edukyle/TIL.git)

1.  원격 저장소 조회

*   `git remote -v`

1.  원격 저장소 삭제

*   `git remote rm <이름>`

1.  원격 저장소에 업로드

*   `git push <저장소 이름> <브랜치 이름>`

**업로드 과정**

    #로컬 git 작업 사항 커밋
    git add .
    git commit -m "작업 내역"
    git log --oneline
    git push origin master
    
    

**주의 사항**

*   `push 오류 날 경우`
    *   원격 저장소의 내용을 먼저 받아오지 않고, 로컬 저장소에서 새로운 커밋을 생성했기 때문에 서로의 커밋 내역이 달라져서 그렇습니다.
    *   만약 로컬 저장소와 원격 저장소의 내용이 다르다면 일단 git pull을 통해 동기화를 시키고 새로운 커밋을 쌓아 나가야 합니다.

* * *

### 원격 저장소 레포 가져오기

1.  원격 저장소 복제 (최초 한번)

*   `git clone <원격 저장소 주소>`

1.  원격 저장소 변경된 내용 가져오기 (로컬저장소와 원격 저장소 동기화 시)

*   `git pull <저장소 이름> <브랜치 이름>`

**주의 사항**

*   `pull 오류 날 경우`
    *   로컬과 원격의 내용이 다른 경우 작업한 내용을 commit 후 pull로 원격 내용 가져오기
    *   충돌이 발생한 경우 수동으로 충돌을 해결한 뒤 다시 commit하기

* * *

### gitignore

*   특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것
    *   민감한 개인 정보가 담긴 파일 (전화번호, 계좌번호, 각종 비밀번호, API KEY 등)
    *   OS(운영체제)에서 활용되는 파일
    *   IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
    *   개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
        *   가상 환경 : `venv/`
        *   `__pycache__/`
*   \*주의 사항 \*\*
*   .gitignore 파일은 .git 폴더와 동일한 위치에 생성합니다.
*   git add 전에 .gitignore에 작성해야 합니다.

* * *

### git reset & revert

1.  git revert

*   특정 커밋에서의 변경 사항을 없었던 일로 만듬 (커밋 삭제되지 않음)
*   이전 커밋을 취소한다는 새로운 커밋을 만듭니다.
*   `git revert <커밋 ID>`

1.  git reset

*   특정 commit으로 되돌아가는 작업
*   특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 모두 삭제
*   `git reset [옵션] <commit id>`
    *   \-soft : 삭제된 commit의 기록을 staging area에 남김
    *   \-mixed : 삭제된 commit의 기록을 working directory에 남김 (기본 옵션 값
    *   \-hard : 삭제된 commit의 기록을 남기지 않음

**과정**

    #커밋 내역 확인
    git log --oneline
    git reset --soft f7b3
    git log --oneline
    
    

**참고**

*   이미 삭제한 commit으로 되돌아가기
    *   `git reflog` : HEAD가 이전에 가리켰던 모든 commit을 보여줌
    *   git reset --hard <복구하고자 하는 commitID>

* * *

### 바로 직전 생성한 commit 수정하기

1.  Commit 메시지 수정

**실습 과정**

    # README.md 파일 생성 후 commit
    $ touch README.md
    $ git add .
    $ git commit -m 'A 기능 구현 완료'
    
    # 직전 커밋 메시지 수정
    $ git commit --amend
    
    #Vim 에디터가 열리면서 직전 commit 메시지를 수정할 수 있음
    # `Insert`키 입력 -> 메시지 수정 -> 메시시 저장(`ESC` ->  `shift+:` -> `wq!`)
    
    #커밋 로그 확인
    $ git log --oneline
    
    

1.  Commit 전체 수정

*   커밋 후에 간단한 수정 사항이 있어 파일 추가 및 내용 수정 이 있는 경우

**실습 과정**

    #커밋이 완료된 상태
    
    #수정 사항 처리
    $ touch b-function.txt
    $ git add .
    
    #수정 사항 직전 커밋에 반영
    $ git commit --amend
    
    #Vim에디터에서 내용 확인 및  저장 (필요하다면 커밋 메시지 내용 수정)
    
    #커밋 로그 확인
    $ git log --oneline