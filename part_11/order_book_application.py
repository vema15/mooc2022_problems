# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    unique_id = 1
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.unique_id
        Task.unique_id += 1

    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"FINISHED" if self.finished == True else "NOT FINISHED"}'

    def is_finished(self):
        return False if self.finished == False else True
    
    def mark_finished(self):
        self.finished = True

class OrderBook():
    def __init__(self):
        self.orders = []
    
    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return [order for order in self.orders]

    def programmers(self):
        temp_list = []
        for order in self.orders:
            if order.programmer not in temp_list:
                temp_list.append(order.programmer)
        for programmer in temp_list:
            print(programmer)
    
    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.finished = True
                print("marked as finished")
                return
        print("erroneous input")
    def finished_orders(self):
        finished_list = [order for order in self.orders if order.finished == True]
        if finished_list == []:
            print("no finished tasks")
        else:
            for order in finished_list:
                print(order)

    def unfinished_orders(self):
        unfinished_list = [order for order in self.orders if order.finished == False]
        if unfinished_list == []:
            print("no unfinished tasks")
        else:
            for order in unfinished_list:
                print(order)
    
    def status_of_programmer(self, programmer: str):
        status_tuple = [0, 0, 0, 0]
        for order in self.orders:
            if order.programmer == programmer:
                if order.finished == True:
                    status_tuple[0] += 1
                    status_tuple[2] += order.workload
                elif order.finished == False:
                    status_tuple[1] += 1
                    status_tuple[3] += order.workload
        if status_tuple == [0,0,0,0]:
            print("erroneous input")
            return
        print(f'tasks: finished {status_tuple[0]} not finished {status_tuple[1]}, hours: done {status_tuple[2]} scheduled {status_tuple[3]}')
    
class OrderBookApplication:
    def __init__(self):
        self.order_book = OrderBook()

    def execute(self):
        print("commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")
        while True:
            user_input = int(input("command: "))
            if user_input == 0:
                break
            elif user_input == 1:
                temp_input = input("description: ")
                person_and_workload = input("programmer and workload estimate: ")
                p_and_w = person_and_workload.split(" ")
                if len(p_and_w) == 1:
                    print("erroneous input")
                    continue
                try:
                    int(p_and_w[1])
                except:
                    print("erroneous input")
                    continue
                else:
                    self.order_book.add_order(temp_input, p_and_w[0], int(p_and_w[1]))
                    print("added!")
            elif user_input == 2:
                self.order_book.finished_orders()
            elif user_input == 3:
                self.order_book.unfinished_orders()
            elif user_input == 4:
                try:
                    user_id = int(input("id: "))
                    self.order_book.mark_finished(user_id)
                except:
                    print("erroneous input")
            elif user_input == 5:
                self.order_book.programmers()
            elif user_input == 6:
                programmer_input = input("programmer: ")
                self.order_book.status_of_programmer(programmer_input)
            else:
                print("erroneous input")


app_run = OrderBookApplication()
app_run.execute()