## 팀 개발을 위한 git/github 시작하기
---
### 1. git 그리고 github
버전 관리란 무엇인가?  
- 내가 원하는 시점(버전)으로 이동할 수 있게 해주는 것이 버전관리이며, 이를 도와두는 툴이 버전 관리 시스템이다.
- 협업을 하는 경우?
    - 팀 프로젝트에 참여하는 인원이 많을 수록, 프로젝트 기간이 길수록 어느 파일이 최종 업데이트 파일인지 확인할 길이 막막해진다. 그래서 여럿이 함께 작업하는 협업 프로젝트에는 버전 관리가 필요함.
    - 내가 원하는 시점마다 깃발을 꽂고, 깃발이 꽂힌 시점으로 자유롭게 이동할 수 있다면 편안하게 새로운 소스코드를 추가하거나 삭제하면 된다: Git
    - Git은 데이터를 저장할 공간만 있다면 어디서나 사용할 수 있다. (드롭박스, 구글 클라우드...)
        - 이런 Git 호스팅 사이트중 하나가 Github이다.
    - Github에 소스코드를 올려두면 시간, 공간의 제약 없이 협업할 수 있다. : 누구든지 기여할 수 있는 공개저장소 프로젝트를 오픈소스라고 한다.

1) Git 초기 설정

```
$git init
$git config --global user.email <E_mail(ex:"yjgil123@gmail.com")>
$git config --global user.name <ID (ex:"yeongjaeGil")>
$git remote add origin <Git repo (ex:https://Github.com/yeongjaeGil/git-test.git)>
$git config credential.helper store # 한번만 저장하면됨
```

2) Git file 올리기

```
$git add <filename(ex:README.txt)>
    :파일들을 스테이지에 추가 (새로 만든 파일은 반드시 추가해야함(untracked).)
$git commit -m <EXPLAIN(ex:"내가 이 파일을 왜 만들었는지 설명")> 
    :stage에 있는 파일을 commit
    *[-m]은 'message' 약자 
$git commit -a
    : add 명령을 생략하고 바로 커밋하고 싶을 경우, untracked 파일은 커밋되지 않는다.
$git push [-u] [원격 저장소(ex:origin)] [브랜치 이름(ex:master)]
    : 한번 등록 이후에는 git push만 하면 된다.
$git reset [filename]
    : 파일을 스테이지에서 내린다.(unstaging)
```

좋은 커밋 7가지 규칙
- 1. 제목과 본문을 빈 줄로 분리한다.
- 2. 제목은 50자 이내로 쓴다.
- 3. 제목을 영어로 쓸 경우 첫글자는 영어로 쓴다.
- 4. 제목에는 마침표를 넣지 않는다.
- 5. 제목을 영어로 쓸 경우 동사원형으로 시작한다.
- 6. 본문을 72자 단위로 줄바꿈한다.
- 7. 어떻게 보다 무엇과 왜를 설명한다.

3) 다른 커밋보기  

```
$git log  
    * commit 91dc12bd216c64c5862dc120253bb852c80d8721 같이 나오면 앞에서 7자리 혹은 전체로 돌아갈 수 있음.  
$git checkout <COMMIT_ID (ex:91dc12b)>
    * 돌아가려면 두번째 커밋 번호를 적든 '-'를 기술  
$git checkout -   
    * checkout 명령어를 사용해서 원하는 시점으로 파일을 되돌릴 수 있다.  
$git status [-s]
$git log --oneline --all --decorate
    : 7자리씩 알아보기 쉽게 로그가 나온다.
    * --oneline: 커밋 메세지를 한 줄로 요약해서 보여줌
      --graph: 커밋 옆에 브랜치의 흐름을 그래프로 보여줌
      --decorate: 원래는 --decorate=short옵션을 의미. 브랜치와 태그 등의 참조를 간결히 표시
      --all: all 옵션이 없을 경우 HEAD와 관계없는 옵션은 보여주지 않는다.
$git log -n <숫자>
    : 최신 숫자개수 만큼의 로그를 보여준다.
```

4) Github 원격저장소의 커밋을 로컬 저장소에 내려받기 

```
$ git clone <Github address (ex:https://Github.com/yeongjaeGil/git-test.git .)>
$ git pull [원격저장소(ex:origin)] [브랜치 이름(ex:master)]
    : 원격저장소의 변경사항을 워킹트리에 반영. (git fetch + git merge)
$ git fetch [원격저장소위치] [브랜치 이름]
    : 원격저장소의 브랜치와 커밋들을 로컬저장소와 동기화함. 옵션을 생략하면 모든 원격저장소에서 모든 브랜치를 가져온다.
$ git merge 브랜치 이름
    : 지정한 브랜치의 커밋들을 현재 브랜치 및 워킹트리에 반영
```

5) 리눅스 인증

```
$ git config credential.helper store
    :passwdrk .git-credentials에 남는 문제가 있다.
$ git config --unset credential.helper #옵션 삭제
$ rm ~/.git-credentials 
```

### 2. 용어 정리
---
- [.git] 폴더에는 Git으로 생성한 버전들의 정보와 원격저장소 주소등이 들어있다. 이를 로컬 저장소라고 부른다.  
- origin:Github 원격저장소의 닉네임
- master: 커밋을 올리는 '줄기'의 이름, git이 제공하는 기본적인 브랜치
- Branch: 특정 기준에서 줄기를 나누어 작업할 수 있는 기능; 새로운 가지로 커밋을 만들려면 브랜치를 먼저 만들어야 함.
- HEAD: branch 혹은 commit을 가리키는 포인터.
    - 현재 작업 중인 브랜치를 가리킨다
    - 브랜치는 커밋을 가리키므로 HEAD도 커밋을 가리킨다.
    - 결국 HEAD는 현재 작업 중인 브랜치의 최근 커밋을 가리킨다.
- working tree: 일반적인 작업이 일어나는 곳
- local repository: git init으로 생성되는 [.git] 폴더가 로컬 저장소이다.
- remote repository: 로컬 저장소를 업로드하는 곳
- Git 저장소: 넓은 의미로는 작업 폴더

### 3.협업 하기
---
- 협업하기 위해서는 브랜치를 만들고 이동하면 됨
    - 1) 협업자는 커밋을 올릴 브랜치를 각각 만들고
    - 2) 자신이 만든 브랜치로 이동
    - 3) 브랜치에 커밋을 올리기
    - 4) 코딩이 완료되면 브랜치를 합친다
- 미리 브랜치 규칙을 정하는 것이 일반적
    - 1) [master] 브랜치에는 직접 커밋을 오리지 않는다.(동시에 작업하다 꼬일 수 있으니)
    - 2) 기능 개발을 하기 전에 [master] 브랜치를 기준으로 새로운 브랜치를 만든다.
    - 3) 이 브랜치 이름은[feature/기능이름] 형식으로 하고 한명만 커밋을 올린다.
    - 4) [feature/기능이름] 브랜치에서 기능 개발이 끝나면 [master] 브랜치에 이를 합친다.
- checkout: 브랜치를 이동하는 명령어
- merge: 브랜치와 브랜치 합치기; 두버전의 합집합을 구하는 것
    - Fast-forward(빨리 감기 병합): A, A+ -> A+ 로 A가 동일할때 뒷부분 것의 상태로 바꾼다.
    - conflict: AB, AC+ -> ? /이런경우 B와 C가 다르므로, 충돌이 생긴다.; 충돌이 난 부분만 확인하고 무엇을 남길지 수동으로 선택해주면 된다!
    - 두브랜치를 합치는 과정
        - branch1, branch2를 만든 경우, master에 병합을 해야 한다.


```
$git branch 
    : 브랜치 목록/*가 붙어 있으면 HEAD
$git branch <브랜치 이름>
    : <브랜치 이름> 생성
$git checkout <브랜치 이름>
    : <브랜치 이름>으로 이동
$git checkout -b <브랜치 이름> <커밋 체크섬>
    : 특정 커밋에서 브런치를 새로 생성하고 동시에 체크아웃까지 한다. 자주 쓰인다
$git merge <대상 브랜치>
    : 현재 브랜치와 대상 브랜치를 병합한다.
$git rebase <대상 브랜치>
    : 내 브랜치의 커밋들을 대상 브랜치에 재배치 시킨다. 히스토리가 깔끔해져서 자주 사용하지만 조심해야함
$git brance -d <브랜치 이름>
    : 특정 브랜치를 삭제할 때 사용. HEAD 브랜치나 병합되지 않은 브랜치는 삭제할 수 없다.
$git branch -D <브랜치 이름>
    : 강제 삭제
$git log --oneline --all
    : 변경된 브랜치 확인    
```
---
- * revert를 사용해서 커밋을 되돌리는 경우
    - C1<-F1<-C2<-F2<-C3(master)
        - 1. 새로운 브랜치 만들고 수동으로 변경사항을 직접 수정해서 병합
        - 2. rebase -i를 통해 필요한 커밋만 남기고 [master] 브랜치에 push --force
   - git revert F2
   - git revert F1
       -  C1<-F1<-C2<-F2<-C3<-RF2<-RF1(master)
           - 이전 히스토리를 변경하지 않고 작업 이전 상태로 되돌릴 수 있다.
           - 뭘 잘못해서 돌렸는 지에대한 로그도 남길 수 있음!

- * 새로운 commit을 생성하면?
    - 새로 커밋을 생성하면 그 커밋의 부모는 언제나 이전 HEAD 커밋
    - 커밋이 생성되면 HEAD는 새로운 커밋으로 갱신
    - HEAD가 가리키는 브랜치도 HEAD와 함께 새로운 커밋을 가리킨다.