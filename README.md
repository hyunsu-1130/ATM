# ATM
1. 목적
  : 자동화된 금융 거래 처리 기능을 통해 사용자에게 편의성 제공

2. 배경 기술
   - 개발 환경 :
• 개발 tool : VS Code
• 프로그래밍 언어 : Python
• 사용 라이브러리 : random, pymysql

   - 데이터베이스 :
• 데이터베이스 시스템: MySQL
• 데이터베이스 테이블: user info 2 (계좌 관련 정보를 저장하는 테이블)

3. 실제 구현
 - 시나리오
  : DB에 저장된 내용을 이용한 ATM기로 프로그램을 실행한 뒤 계좌번호를 입력하고 원하는 거래 유형을 선택하여 입금, 출금, 계좌 이체를 수행함. 이때, DB에 저장된 계좌 정보와 잔액이 실시간으로 업데이트되어 사용자의 거래를 반영함.

  1. 회원 계좌번호 DB 입력 및 계좌번호 유무 확인
  2. 회원 정보 확인 (계좌에 맞는 비밀번호 확인)
  3. 거래 선택 
 	3-1. 입금 – 현금 투입 -> 통장 입금
 	3-2. 출금 – 출금액 입력 -> 비밀번호 확인 -> 잔액 확인 -> 통장 출금
 	3-3. 계좌 이체 – 이체할 계좌 -> 이체할 금액 -> 사용자 계좌 비밀번호 확인 -> 잔
	     액 확인 -> 이체 -> 본인 통장액 감원
 	3-4. 거래 종료
  기타 : 거래 오류 시

  - 코드 설명
     ATM 클래스 : ATM 기능을 구현한 클래스 생성
     DB 사용을 위해 라이브러리를 이용하여 mySQL에 접속
     load_accounts : DB에서 사용자 정보를 불러와서 딕셔너리에 저장 (계좌번호, 이름, 생
      년월일, 초기 잔액, 계좌 비밀번호) 
     transaction : 사용자의 거래 선택에 따라 입금, 출금, 계좌 이체 기능 수행	ㄱ. 사용자의 계좌번호 확인
        ㄴ. 거래 선택 (입금, 출금, 계좌 이체, 거래 종료) 
           각 단계에서 입력받은 비밀번호 확인과 잔액 변경 시, DB update
