
- 패스워드 정책
```sql
SET GLOBAL validate_password_policy=LOW;
select password('<테스트할 패스워드>');

```
- 권한 검색
```
SELECT host, user, authentication_string FROM mysql.user; 
```

- 1. 데이터 베이스 생성
```sql
CREATE DATABASE test default CHARACTER SET UTF8;
show databases;
```
- 2. 데이터 베이스를 사용할 사용자 추가
```sql
GRANT ALL PRIVILEGES ON testdb.* TO 'ID'@localhost IDENTIFIED BY 'pwd';
EXIT;
mysql -u rlfdudwo -p
USE test;
```
- 3. 테이블성
```sql
CREATE TABLE professor ( _id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(32) NOT NULL, belong VARCHAR(12) DEFAULT 'FOO', phone VARCHAR(12) ) ENGINE=INNODB; DESCRIBE professor; #테이블 구조 확인
```
- 4. 데이터 삽입
```sql
INSERT INTO professor
(name, belong, phone)
VALUES('길영재','IDE','01033339999')
SELECT * FROM professor;
```
- 5. 쿼리
```sql
-- SELECT
SELECT column1, column2, column3 FROM DB WHERE column1 NOT LIKE 'man%' ORDER BY column1, column2 DESC LIMIT 1;
-- COUNT
SELECT COUNT(*) FROM DB;
SELECT COUNT(DISTINCT(column1)) FROM DB WHERE coulmn2 IS NOT NULL;
-- GOUP BY
SELECT JOB, COUNT(JOB) AS count FROM DB GOUP BY DB HAVING  count >= 3;
```
