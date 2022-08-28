class Math:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_sum(self, requestor):
        value = 0
        for i in self.data:
            value += i
        print(f"Hey {requestor}! {self.name} calculated sum to be {value}")

    def get_avg(self, requestor):
        total = 0
        for i in self.data:
            total += i
        average = total / len(self.data)
        print(f"Hey {requestor}! {self.name} calculated average to be {average}")


m = Math("Noman", [2,4,6,8,10])
m.get_sum("Sohaib")
m.get_avg("Sohaib")
