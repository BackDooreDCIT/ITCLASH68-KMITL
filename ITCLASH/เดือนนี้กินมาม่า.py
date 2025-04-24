class EmployeeNode:
    def __init__(self, name, emp_id, money):
        self.name = name
        self.id = emp_id
        self.money = money
        self.next = None

class EmployeeLinkedList:
    def __init__(self):
        self.head = None
    
    def is_id_exists(self, emp_id):
        current = self.head
        while current:
            if current.id == emp_id:
                return True
            current = current.next
        return False
    
    def get_next_available_id(self, emp_id):
        while self.is_id_exists(emp_id):
            emp_id += 1
        return emp_id
    
    def insert_employee(self, name, emp_id, money):
        if money < 0:
            return
        
        emp_id = self.get_next_available_id(emp_id)
        new_node = EmployeeNode(name, emp_id, money)
        
        if not self.head or (self.head.money > money) or (self.head.money == money and self.head.id > emp_id):
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and ((current.next.money < money) or (current.next.money == money and current.next.id < emp_id)):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def display(self):
        if not self.head:
            print("LinkedList is Empty.")
            return
        
        current = self.head
        while current:
            print(f"Name : {current.name}")
            print(f"ID : {current.id}")
            print(f"Money : {current.money:.2f}")
            print("---------------")
            current = current.next

# รับข้อมูลเข้า
employee_list = EmployeeLinkedList()

while True:
    data = input().strip()
    if data.lower() == "end":
        break
    try:
        name, emp_id, money = data.split()
        employee_list.insert_employee(name, int(emp_id), float(money))
    except ValueError:
        continue

employee_list.display()
