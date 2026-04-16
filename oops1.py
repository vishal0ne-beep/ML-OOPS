class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    
    def travel(self, destinantion):
        print(f"Employee is now traveling to {destinantion}")

sam = employee()
print(sam.salary)
sam.travel("USA")