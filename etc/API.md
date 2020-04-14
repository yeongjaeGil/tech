## API: Application Programming Interface

- 두개의 시스템이 서로 상호작용하기 위한 인터페이스
    - 데이터를 주고 받는 인터페이스
    - API라고 하면 보통 REST API를 지칭

- API 접근 권한  
    - Authentication: Identity(정체)가 맞다는 증명
    - Authorization: API를 통한 어떠한 액션을 허용
- API가 Authentication을 하여도 어떠한 액션에 대해서는 Authorization을 허용하지 않을 수 있음
- API의 필수는 첫째도 시큐리티, 둘째도 시큐리티
    - 어떠한 시큐리티(보안) 방안이 없을 경우:
        - DELETE 리퀘스트를 통해서 다른 이용자의 정보를 지울 수도 있음
        - 제 3자에게 데이터 유출로 이어질 수 있음
        - 누가 API를 사용하는지, 어떤 정보를 가져가는지 트래킹 할 수가 없음
- API key?
    - API key란 보통 Request URL 혹은 Request 헤더에 포함되는 긴 스트링
