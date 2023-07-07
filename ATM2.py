''' 

 DB에 저장된 내용을 이용하여 ATM기 만들기
1. 회원 계좌번호 DB 입력 및 계좌번호 유무 확인
2. 회원 정보 확인 (계좌에 맞는 비번확인)
3. 거래 선택 
 3-1. 입금 – 현금 투입 -> 통장 입금
 3-2. 출금 – 출금액 입력 -> 비밀번호 확인 -> 잔액 확인 -> 통장 출금
 3-3. 이체 – 이체할 계좌 -> 이체할 금액 -> 사용자 계좌 비밀번호 확인 -> 잔액 확인 -> 이체 -> 본인 통장액 감원
 3-4. 거래 종료
기타 : 거래 오류 시


'''

import pymysql                          # DB 라이브러리

class ATM:
    def __init__(self):
        self.conn = pymysql.connect(        # mySQL 접속하기            
            host='127.0.0.1', 
            port=3306, 
            user='root', 
            passwd='k8339970!',
            db='atm', 
            charset='utf8'
        )    
        self.cursor = self.conn.cursor()


    def load_accounts(self):                        # DB에서 계좌정보 불러와 딕셔너리에 저장
        sql = "SELECT * FROM `user info`"
        self.cursor.execute(sql)
        accounts_data = self.cursor.fetchall()

        self.accounts = {}                             # 사용자 계좌 정보 관련 딕셔너리 생성
        for account_data in accounts_data:
            account_num, name, birth_date, initial_balance, password = account_data
        
            self.accounts[account_num] = {
                "name" : name,
                "birth_date" : birth_date,
                "balance" : float(initial_balance),
                "password" : password
            }
       

    '''def validate_password(self, account_num, password):        # 계좌정보 DB에서 입력받은 사용자의 계좌번호 유무 확인 및 비밀번호 확인
        sql = "SELECT password FROM `user info` WHERE account=%s"
        self.cursor.execute(sql, (account_num,))
        result = self.cursor.fetchone()
        if result is not None:
            stored_password = result[0]
            if stored_password == password:
                return True
        return False'''
    
    
    def transaction(self, account_num):                            
        sql = "SELECT * FROM `user info` WHERE account=%s"         # 사용자 계좌번호 확인 
        self.cursor.execute(sql, (account_num,))
        account_data = self.cursor.fetchone()
        if account_data is None:
            print("계좌번호가 유효하지 않습니다.")
            return
        
        balance = float(account_data[3])
        user_password = account_data[4]

        while True:                                          # 원하는 거래 선택
            print("1. 입금")
            print("2. 출금")
            print("3. 계좌 이체")
            print("4. 거래 종료")
            transaction_type = input("원하시는 거래 유형의 번호를 선택하세요: ")

            if transaction_type == "1":  # 입금
                deposit_amount = float(input("입금하실 금액을 투입하세요: "))
                balance += deposit_amount
                print(f"{deposit_amount}원이 입금되었습니다.")
                print(f"현재 잔고는 {balance}원 입니다.")


            elif transaction_type == "2":  # 출금
                withdraw_amount = float(input("출금하실 금액을 입력하세요: "))
                password = input("사용자의 계좌 비밀번호 4자리를 입력하세요: ")
                
                if password == user_password:             
                    print("비밀번호가 틀렸습니다.")
                    continue
              
                if withdraw_amount > balance:               # 현재 잔고에 원하는 출금액 유무 확인 및 출금
                    print("잔액이 부족합니다.")
                else:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount}원이 출금되었습니다.")
                    print(f"현재 잔고는 {balance}원 입니다.")


            elif transaction_type == "3":  # 계좌이체
                target_account_num = input("이체하실 계좌번호 8자리를 입력하세요: ")
                transfer_amount = float(input("이체하실 금액을 입력하세요: "))
                password = input("사용자의 계좌 비밀번호 4자리를 입력하세요: ")
                if password == user_password:             
                    print("비밀번호가 틀렸습니다.")
                    continue

                if transfer_amount > balance:
                    print("잔액이 부족하여 계좌이체가 불가능합니다.")
                    continue

                balance -= transfer_amount
                print(f"{transfer_amount}원이 {target_account_num}으로 이체되었습니다.")
                print(f"현재 잔고는 {balance}원 입니다.")


            elif transaction_type == "4":  # 거래 종료
                print("거래가 종료되었습니다. 감사합니다.")
                break

            else:
                print("올바른 거래 유형을 선택해주세요.")
                continue

    def run(self):
        print("\n=== Hyun Su ATM ===")
        account_num = input("안녕하세요.\n사용자의 계좌번호 8자리를 입력하세요: ")
        self.transaction(account_num)
        self.conn.close()


# ATM 객체 생성 및 실행
atm = ATM()

atm.run()