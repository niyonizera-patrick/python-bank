# main balance 
# initial balance 
# entered or withdrawn money 
# current balance 

current_balance = 0

def deposit():
      global current_balance
      money = int(input('enter the money to deposit '))
      if money > 0:
            current_balance += money

            print(f'successifully deposited {money} : new balance is :{current_balance}')

def withdraw():
      global current_balance

      money = int(input('enter money to withdraw'))

      if current_balance >=money:
            current_balance -= money
            print(f'you have withdrawn {money } : the remaining balance is : {current_balance}')   

def balance():
      global current_balance

      print(f' this is your current balance {current_balance}')
  
      
    

def menu():
    while True:
            print('\n menu ')
            print('1. check balance ')
            print('2. withdraw money')
            print('3. deposit the money ')
            print('4. exiting ...')


            choice = input('enter your choice:_ ')

            if (choice =='1'):
                  balance()
            elif(choice == '2'):
                  withdraw()
            elif (choice == '3'):
                  deposit()
            elif(choice == '4'):
                  print('exiting ...')      
            else:
                  print('invalid input')     
def main():
      global current_balance

     
      initial = 100000
      current_balance = initial
      pin = 2022
      ussd = '*123#'
      inussd = input('enter the ussd code')
      
      if inussd == ussd:
            inpin = int(input('enter the pin '))
            if inpin == pin:
                  menu()
                           
main()
