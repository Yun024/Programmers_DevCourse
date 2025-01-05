-- Snowflake 실습을 위한 초기 환경 설정
CREATE DATABASE dev;

-- 먼저 3개의 스키마를 생성
CREATE SCHEMA dev.raw_data;
CREATE SCHEMA dev.analytics;
CREATE SCHEMA dev.adhoc;

-- 3개의 테이블을 raw_data 밑에 생성
CREATE OR REPLACE TABLE dev.raw_data.session_transaction(
    sessionid varchar(32) primary key,
    refunded boolean,
    amount int
);

CREATE TABLE dev.raw_data.user_session_channel(
    userid integer,
    sessionid varchar(32) primary key,
    channel varchar(32)
);

CREATE TABLE dev.raw_data.session_timestamp(
    sessionid varchar(32) primary key,
    ts timestamp
);

-- COPY를 사용해 벌크 업데이트를 수행
COPY INTO dev.raw_data.session_timestamp
FROM 's3://yeojun-test-bucket/test_data/session_timestamp.csv'
credentials = (AWS_KEY_ID='[]' AWS_SECRET_KEY='[]')
FILE_FORMAT = (type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

COPY INTO dev.raw_data.session_transaction
FROM 's3://yeojun-test-bucket/test_data/session_transaction.csv'
credentials = (AWS_KEY_ID='[]' AWS_SECRET_KEY='[]')
FILE_FORMAT = (type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

COPY INTO dev.raw_data.user_session_channel
FROM 's3://yeojun-test-bucket/test_data/user_session_channel'
credentials = (AWS_KEY_ID='[]' AWS_SECRET_KEY='[]')
FILE_FORMAT = (type='CSV' skip_header=1 FIELD_OPTIONALLY_ENCLOSED_BY='"');

-- analytics 스키마 밑에 테이블을 CTAS로 생성
CREATE TABLE dev.analytics.mau_summary AS
SELECT
    TO_CHAR(A.ts,'YYYY-MM') AS month,
    COUNT(DISTINCT B.userid) AS mau
FROM raw_data.session_timestamp A
JOIN raw_data.user_session_channel B ON A.sessionid = B.sessionid
GROUP BY 1
ORDER BY 1 DESC;

SELECT * FROM dev.analytics.mau_summary LIMIT 10;

-- Role과 User생성
CREATE ROLE analytics_users;
CREATE ROLE analytics_authors;

-- 사용자 생성
CREATE USER yeojun PASSWORD='Yeojun15'

-- set up analytics_users
GRANT USAGE on schema dev.raw_data to ROLE analytics_users;
GRANT SELECT on all tables in schema dev.raw_data to ROLE analytics_users;
GRANT USAGE on schema dev.analytics to ROLE analytics_users;
GRANT SELECT on all tables in schema dev.analytics to ROLE analytics_users;
GRANT ALL on schema dev.adhoc to ROLE analytics_users;
GRANT ALL on all tables in schema dev.adhoc to ROLE analytics_users;

-- set up analytics_authors
GRANT ROLE analytics_users TO ROLE analytics_authors;
GRANT ALL on schema dev.analytics to ROLE analytics_authors;
GRANT ALL on all tables in schema dev.analytics to ROLE analytics_authors;

-- 사용자에게 analytics_users 권한 지정
GRANT ROLE analytics_users TO USER yeojun;

-- 역할에 부여된 권한 조회
SHOW GRANTS TO ROLE analytics_users;
SHOW GRANTS TO ROLE analytics_authors;

-- 특정 사용자가 가지 권한 직접 조회
SHOW GRANTS TO USER yeojun;

-- 역할 해제
REVOKE ROLE analytics_users FROM USER yeojun;

-- 사용자 삭제
DROP USER yeojun;

-- 추가 확인
SHOW USERS;