# Write your solution here:

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
        return temp_list
    
    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.finished = True
                return
        raise ValueError

    def finished_orders(self):
        return [order for order in self.orders if order.finished == True]
    
    def unfinished_orders(self):
        return [order for order in self.orders if order.finished == False]
    
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
            raise ValueError
        return tuple(status_tuple)

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
