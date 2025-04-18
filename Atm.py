import time

print("Please Insert Your Card")

time.sleep(5)
password=2222
pin=int(input("Enter your ATM Pin"))
Balance = 5000
if pin == password:
	while True:

		print("""
			1 == Balance
			2 == Withdraw Balance
			3 == Deposit Balance
			4 == Exit"""
			)
		try:
			option = int(input("Please enter your choice"))
		except:
			print("Please enter valid option")
		if option == 1:
			print(f"Your Current Balance is {Balance}")
			print("=========================================================")
			print("=========================================================")
		if option == 2:
			withdraw_amount = int(input("Please enter withdraw_amount"))
			print("=========================================================")
			print("=========================================================")
			Balance=Balance-withdraw_amount
			print(f"{withdraw_amount} is debited from your account")
			print("*********************************************************")
			print("*********************************************************")
			print(f"your current balance is {Balance}")
			print("*********************************************************")
			print("*********************************************************")
		if option == 3:
			deposit_amount = int(input("Please enter deposit_amount"))
			Balance=Balance+deposit_amount
			print("*********************************************************")
			print("*********************************************************")
			print(f"{deposit_amount} is credited to your account")
			print("*********************************************************")
			print("*********************************************************")
			print(f"your updated balancs is {Balance}")	
		if option == 4:
			break
else:
	print("Wrong pin Please try again")	