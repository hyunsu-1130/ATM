''' 

ATM기 만들기
1. 회원 계좌번호 생성 (이름, 생년월일, 초기잔액, 계좌번호, 계좌비번)
2. 회원 정보 확인 (계좌에 맞는 비번확인)
3. 거래 선택 
 3-1. 입금 – 현금 투입 -> 통장 입금
 3-2. 출금 – 출금액 입력 -> 비밀번호 확인 -> 잔액 확인 -> 통장 출금
 3-3. 이체 – 이체할 계좌 -> 이체할 금액 -> 사용자 계좌 비밀번호 확인 -> 잔액 확인 -> 이체 -> 본인 통장액 감원
 3-4. 거래 종료
기타 : 거래 오류 시

'''

import string
import random

class ATM:
    def __init__(self):
        self.accounts = {}    # 계좌번호 및 통장 잔고를 저장할 딕셔너리

 
    def assign_account_num(self):       # 8자리 숫자로 구성된 계좌번호를 랜덤하게 생성
        account_num = ''.join(random.choices(string.digits, k=8))
        return account_num


    def create_account(self):       # 사용자의 이름, 생년월일, 초기 잔액, 비밀번호를 입력 받은 후, 랜덤하게 생성된 계좌번호 할당
        name = input("이름을 입력하세요 : ")
        birth_date = input("생년월일을 입력하세요 (YYYYMMDD) : ")
        account_num = self.assign_account_num()
        initial_balance = input("초기 잔액을 입력하세요 : ")
        password = input("계좌 비밀번호 4자리를 입력하세요 : ")
        self.accounts[account_num] = {          # 사용자의 계좌정보 딕셔너리에 저장
            "name" : name,
            "birth_date" : birth_date,
            "balance" : initial_balance,
            "password" : password
        }
        print(f"{name}님의 계좌가 생성되었습니다. 계좌번호는 {account_num} 입니다.")        # 사용자에게 할당된 계좌번호


    def validate_password(self, account_num, password):
        account = self.accounts.get(account_num)            # 계좌정보 딕셔너리에서 입력받은 계좌번호 유무 확인
        if account is None:
            return False
        if account["password"] == password:
            return True
        return False


    def update_balance(self, account_num, new_balance):         # 잔액 변경 시 update
        self.accounts[account_num]["balance"] = new_balance


    def transaction(self, account_num):                             # 원하는 거래 선택
        while True:
            print("1. 입금")
            print("2. 출금")
            print("3. 계좌 이체")
            print("4. 거래 종료")
            transaction_type = input("원하시는 거래 유형의 번호를 선택하세요: ")

            balance = float(self.accounts[account_num]["balance"])         

            if transaction_type == "1":  # 입금
                deposit_amount = input("입금하실 금액을 투입하세요: ")
                deposit_amount = float(deposit_amount)
                balance += deposit_amount                               # 현재 잔액에 입금
                print(f"{deposit_amount}원이 입금되었습니다.")
                print(f"현재 잔고는 {balance}원 입니다.")
                self.update_balance(account_num, balance)               # 잔액 update


            elif transaction_type == "2":  # 출금
                withdraw_amount = input("출금하실 금액을 입력하세요: ")
                withdraw_amount = float(withdraw_amount)
                password = input("사용자의 계좌 비밀번호 4자리를 입력하세요: ")
                if not self.validate_password(account_num, password):               # 계좌 비밀번호 확인
                    print("비밀번호가 틀렸습니다.")
                    continue

                if withdraw_amount > balance:  # 현재 잔고에 원하는 출금액 유무 확인 및 출금
                    print("잔액이 부족합니다.")
                else:
                    balance -= withdraw_amount                                      # 현재 잔액에서 출금
                    print(f"{withdraw_amount}원이 출금되었습니다.")
                    print(f"현재 잔고는 {balance}원 입니다.")
                    self.update_balance(account_num, balance)                       # 잔액 update


            elif transaction_type == "3":  # 계좌이체
                target_account_num = input("이체하실 계좌번호 8자리를 입력하세요: ")
                transfer_amount = input("이체하실 금액을 입력하세요: ")
                transfer_amount = float(transfer_amount)
                password = input("사용자의 계좌 비밀번호 4자리를 입력하세요: ")         # 계좌 비밀번호 확인
                if not self.validate_password(account_num, password):
                    print("비밀번호가 틀렸습니다.")
                    continue

                if transfer_amount > balance:                                          # 잔액 확인 및 출금
                    print("잔액이 부족하여 계좌이체가 불가능합니다.")
                    continue

                balance -= transfer_amount
                print(f"{transfer_amount}원이 {target_account_num}으로 이체되었습니다.")
                print(f"현재 잔고는 {balance}원 입니다.")
                self.update_balance(account_num, balance)                               # 잔액 update

            elif transaction_type == "4":  # 거래 종료                                  # 거래 종료
                break

            else:
                print("올바른 거래 유형을 선택해주세요.")
                continue


    def run(self):
        print("\n=== Hyun Su ATM ===")
        print("계좌번호 생성을 위해 기본 정보를 입력해주세요.")
        self.create_account()  # 회원 계좌번호 생성
        print("======================")
        account_num = input("사용자의 계좌번호 8자리를 입력하세요: ")
        self.transaction(account_num)

        
# ATM 객체 생성 및 실행
atm = ATM()

atm.run()