def persons(user):

    first_input = input("for logging enter 1, for signup enter 2-->")
    
    if first_input == "1" or  first_input == "2":
        
        while first_input == "2":
            user_name = input('enter your name-->')
           
            if user_name in user:
                return ('the user name is already taken') 
        
            user_password = input("enter your password-->")  
            user_password_verification = input("enter your password again-->")
            
            if user_password == user_password_verification:
                user[user_name] = user_password
                return user
           
            else:
                return "the passwords do not match"    
       
        while first_input == "1":
            user_name = input('enter your name-->')
            
            if user_name in user:
                user_password = input("enter your password-->")
               
                if user_password == user.get(user_name):
                    return(f"welcome  {user_name} ")
               
                else:
                    return "sorry! wrong password"     
            
            else:
                return ("sorry! user name does not exist")
    
    else:
        return ("sorry you have entered un invalid key")


user = {"jones":"123","jane":"234","peter":"345","steve":"456","chris":"567"}  
n = persons(user)
print(n)
