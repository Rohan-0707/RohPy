import os
os.system("cls")
import time

def divider():
    print("\n---------------------------------------------------------------\n")

def menu():
    print("\nThis Program is developed by Mr. Rohan Kumar Bhoi")
    print("\n\n-------------------- Instuctions and Menu --------------------\n")
    print("\n\t1. Beginner\n\t2. Intermediate\n\t3. Advanced\n\n\tPress any other key to exit the program...\n\tPlease do not press power key !!!\n\n")
    print("---------------------------------------------------------------\n")
    choice = input("Please choose your level of Python Skills : ")
    return choice

def install_pkg(choice):
    count = 1
    if choice == "1" or choice == "beginner" or choice == "Beginner":
        os.system("cls")
        print("\nOkay we are installing libraries for Beginners Level !")
        
        print(f"\n\t{count}. Installing NumPy Library...\n")
        os.system("pip install numpy")
        print("\n\tNumPy Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing Pandas Library...\n")
        os.system("pip install pandas")
        print("\n\tPandas Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing MatplotLib Library...\n")
        os.system("pip install matplotlib")
        print("\n\tMatplotLib Successfully Installed !\n")
        divider()
        count += 1
    
    elif choice == "2" or choice == "Intermediate" or choice == "intermediate":
        os.system("cls")
        print("\nOkay we are installing libraries for Intermediate Level !")
        
        print(f"\n\t{count}. Installing Scikit-Learn Library...\n")
        os.system("pip install scikit-learn")
        print("\n\tScikit-Learn Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing Seaborn Library...\n")
        print("\n\tDescription: NumPy is the fundamental package for scientific computing with Python. It provides support for arrays and matrices, along with mathematical functions to operate on these arrays.\n\n")
        os.system("pip install seaborn")
        print("\n\tSeaborn Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing Requests Library...\n")
        os.system("pip install requests")
        print("\n\tRequests Successfully Installed !\n")
        divider()
        count += 1
        
    elif choice == "3" or choice == "Advanced" or choice == "advanced":
        os.system("cls")
        print("\nOkay we are installing libraries for Advanced Level !")
        
        print(f"\n\t{count}. Installing TensorFlow or PyTorch Library...\n")
        os.system("pip install scikit-learn")
        os.system("pip install pytorch")
        print("\n\tTensorFlow and PyTorch Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing Django Library...\n")
        os.system("pip install django")
        print("\n\tDjango Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing Flask Library...\n")
        os.system("pip install Flask")
        print("\n\tFlask Successfully Installed !\n")
        divider()
        count += 1
        
        print(f"\n\t{count}. Installing SQLAlchemy Library...\n")
        os.system("pip install SQLAlchemy")
        print("\n\tSQLAlchemy Successfully Installed !\n")
        divider()
        count += 1
    
    else:
        divider()
        print("\n\tWrong Choice ! Please Enter Valid Choice\n")
        divider()
        time.sleep(5)
        ch=input("\n\nDo you want to continue (Yes / No) : ")
        if ch == "no" or ch == "No":
            os.system("exit")
            print()
        else:
            time.sleep(5)
            os.system("cls")
            execute()
        
        
def execute():
    choice = menu()
    install_pkg(choice)
    user_choice()
    
def user_choice():
    choice = input("\nWould you like to Run this Program again : ")
    if choice == "yes" or choice=="Yes":
        execute()
        
    else:
        os.system("cls")
        print("\n\n\tThanks for using RohPy Package...\n")
        print("\n\tPlease don't forget to follow Developer on Social media !\n")
        print("\n\tInstagram    :   ceorohan")
        print("\tTwitter        :   ceorohan1")
        print("\tFacebook       :   ceorohan")
        print("\tThreads        :   ceorohan")
        print("\tSnapChat       :   ceo_rohan")
        divider()
    
execute()