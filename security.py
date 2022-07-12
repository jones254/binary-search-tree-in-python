def view():
     with open('new.txt','r') as f:
          user=input("enter user name-- ")
          passw=input("enter your password-- ")
          for line in f.readlines():
               data=line.rstrip()
               entry=(f'{user}|{passw}' )
               raw= data.split("|")
 
               if entry in data:
                    print(f'welcome in {user}')
               elif user not in raw:
                    print(f'sorry {user} you are not registered!')    
               elif user in raw:
                    print(f"you have entered a wrong password {user}!")
                     
def add():
     name=input("Enter user name: ")
     password=input("Enter password: ")
     with open('new.txt','a') as f:
          f.write(name + "|" + password + "\n") 
          
while True:
     mode=input("Enter A for logging or B for signup or Q to quit==>").lower()
     if mode == 'q':
          break
     if mode == 'a':
          
          view()
     elif mode == "b":
          
          add()  
     else:
          print('invalid input')
          continue