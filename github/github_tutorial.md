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
```

2) Git file 올리기
```
$git add README.txt  
$git commit -m <EXPLAIN(ex:"내가 이 파일을 왜 만들었는지 설명")> 
    *[-m]은 'message' 약자  
$git push origin master
```

3) 다른 커밋보기  
```
$git log  
    * commit 91dc12bd216c64c5862dc120253bb852c80d8721 같이 나오면 앞에서 7자리 혹은 전체로 돌아갈 수 있음.  
$git checkout <COMMIT_ID (ex:91dc12b)>
    * 돌아가려면 두번째 커밋 번호를 적든 '-'를 기술  
$git checkout -   
    * checkout 명령어를 사용해서 원하는 시점으로 파일을 되돌릴 수 있다.  
```

4) Github 원격저장소의 커밋을 로컬 저장소에 내려받기 
```
$ git clone https://Github.com/yeongjaeGil/git-test.git .
$ git pull origin master
```

### 2. 용어 정리
---
- [.git] 폴더에는 Git으로 생성한 버전들의 정보와 원격저장소 주소등이 들어있다. 이를 로컬 저장소라고 부른다.  
- origin:Github 원격저장소의 닉네임
- master: 커밋을 올리는 '줄기'의 이름, git이 제공하는 기본적인 브랜치
- Branch: 새로운 가지로 커밋을 만들려면 브랜치를 먼저 만들어야 함.
- HEAD: branch 혹은 commit을 가리키는 포인터.

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