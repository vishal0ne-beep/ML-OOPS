class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""How would you like to proceed ?
                           1. Pres 1 to signup
                           2. Press 2 to signn
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email  = input("Enter your email -> ")
        pwd = input("Setup your pasword -> ") 
        self.username = email
        self.password = pwd
        print("You have signed up succesfully")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username =='' and self.password=='':
            print("Please signup")
        else:
            uname = input("Enter your email -> ")
            pwd = input("Enter your pasword -> ") 
            if self.username == uname and self.password == pwd:
                print("Signedin succesfully")
                self.loggedin = True
            else:
                print("Pleae input correct credentials..")
        print("\n")
        self.menu()

abc = chatbook()