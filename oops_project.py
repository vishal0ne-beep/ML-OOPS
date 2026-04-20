class chatbook:

    __user_id = 1  #static variable wwith encapsulation.


    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Defaul User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value

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
            self.my_post()
        elif user_input == "4":
            self.send_msg()
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

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your post here -> ")
            print(f"Your post: {txt} ")
        else:
            print("Signedin first")
        print("\n")
        self.menu()
    
    def send_msg(self):
        if self.loggedin == True:
            txt = input("Enter your message -> ")
            frnd = input("Enter your friend name -> ")
            print("Message sent!")
        else:
             print("Signedin first")
        print("\n")
        self.menu()


abc = chatbook()