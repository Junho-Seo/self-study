1. `pwd`
현재 디렉토리(폴더) 전체 경로를 출력

2. `ls`
현재 디렉토리의 파일/폴더 리스트 출력

3. `.` `..`
- `.` 현재 디렉토리를 의미
- `..` 현재의 상위 디렉토리(부모 폴더)

4. `touch <파일명>`
- 파일 생성

5. `mkdir <폴더명>`
- 폴더(디렉토리) 생성

6. `cd`
- 작업 중인 디렉토리를 변경(위치 이동)
```
# 한 번에 이동도 가능
cd ../../../
cd startcamp/prompt-engineering/new_dir/
```

7. `start`
- 폴더/파일을 열기 (Mac에서는 open 사용)

8. `mv <이동하고 싶은 파일> <이동 경로>`
- 파일 이동
```
mv new.txt new_dir
mv new_dir/new.txt .
```

9. `rm`
- 파일 삭제
- 디렉토리 삭제는 `-r` 옵션 추가
```
rm new.txt
rm -r new_dir
```
