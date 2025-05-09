class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = self.set_health_rate(healthRate)

    def set_health_rate(self, rate):
        return max(0, min(100, rate))

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
        else:
            print(f"{self.name} doesn't have enough money to buy {items} item(s).")

    def __str__(self):
        return f"Person(name={self.name}, money={self.money}, mood={self.mood}, healthRate={self.healthRate})"


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.email = email
        self.salary = self.set_salary(salary)
        self.distanceToWork = distanceToWork
        self.car = car if isinstance(car, Car) else Car(car["model"], car["fuel"], 100)

    def set_salary(self, salary):
        return max(1000, salary)

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        print(f"{self.name} is driving to work...")
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount):
        self.car.fuelRate = min(self.car.fuelRate + gasAmount, 100)
        print(f"{self.name} refueled {gasAmount}%. New fuel level: {self.car.fuelRate:.2f}%")

    def send_mail(self, to, subject, body):
        print(f"Sending email from {self.email} to {to}")
        print(f"Subject: {subject}")
        print(f"Body:\n{body}")

    def __str__(self):
        return (f"Employee(id={self.id}, name={self.name}, email={self.email}, "
                f"salary={self.salary}, mood={self.mood}, healthRate={self.healthRate}, "
                f"money={self.money}, distanceToWork={self.distanceToWork}, "
                f"car={self.car})")


class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_employeesNum(cls, num):
        cls.employeesNum = num
        print(f"Employee limit for all offices set to {cls.employeesNum}")

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        if self.get_employee(employee.id) is None:
            self.employees.append(employee)
            print(f"{employee.name} has been hired.")
        else:
            print(f"Employee with ID {employee.id} already exists.")

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            print(f"{emp.name} has been fired.")
        else:
            print(f"No employee found with ID {emp_id}.")

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary = max(0, emp.salary - deduction)
            print(f"Deducted {deduction} from {emp.name}'s salary.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward
            print(f"Rewarded {emp.name} with {reward}.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def check_lateness(self, emp_id, moveHour):
        lateness = self.calculate_lateness(moveHour, 9) 
        if lateness > 0:
            self.deduct(emp_id, 10)
        else:
            self.reward(emp_id, 10)

    def calculate_lateness(self, arrival_time, start_time):
        return max(0, arrival_time - start_time)

    def __str__(self):
        emp_names = [emp.name for emp in self.employees]
        return f"Office(name={self.name}, employees={emp_names})"


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = self.set_fuel_rate(fuelRate)
        self.velocity = self.set_velocity(velocity)

    def set_fuel_rate(self, rate):
        return max(0, min(100, rate))

    def set_velocity(self, velocity):
        return max(0, min(200, velocity))

    def run(self, velocity, distance):
        self.velocity = self.set_velocity(velocity)
        print(f"{self.name} starts running at {self.velocity} km/h.")

        fuel_per_km = 0.2
        max_distance = self.fuelRate / fuel_per_km

        if max_distance >= distance:
            self.fuelRate -= distance * fuel_per_km
            print(f"{self.name} reached destination after {distance} km.")
        else:
            self.fuelRate = 0
            print(f"{self.name} ran out of fuel after {max_distance:.2f} km. Couldn't finish {distance} km.")
            self.stop()

    def stop(self):
        self.velocity = 0
        print(f"{self.name} has stopped.")

    def __str__(self):
        return f"Car(name={self.name}, fuelRate={self.fuelRate:.2f}%, velocity={self.velocity} km/h)"



per = Person("Samy", 6000, "neutral", 80)
per.sleep(6)
per.eat(3)
per.buy(6)
print(per)

emp = Employee("Samy", 6000, "neutral", 80, 1, {"model": "Fiat 128", "fuel": 30}, "samy@yahoo.com", 1200, 20)
emp.work(8)
emp.send_mail("Ali@yahoo.com", "Meeting", "Let's meet at 3 PM.")
print(emp)

office = Office("ITI")
emp1 = Employee("Alaa", 9000, "neutral", 90, 2, {"model": "BMW", "fuel": 50}, "Alaa@yahoo.com", 1500, 10)
emp2 = Employee("Ali", 7000, "neutral", 85, 3, {"model": "Ford", "fuel": 90}, "Ali@gmail.com", 1400, 11)
office.hire(emp)
office.hire(emp1)
office.hire(emp2)
office.reward(1, 100)
office.deduct(2, 50)

print(office.get_employee(1))
print(office)

car = Car("Fiat 128", 30, 100)
print(car)
car.run(100, 20)
car.stop()
print(car)
