from first_user_interface import UserInterface
from user_data import UserData

def main():    
    userData = UserData()
    userInterface = UserInterface(userData)
    

if __name__ == "__main__":
    main()
else:
    print("You cannot import this as a module.")