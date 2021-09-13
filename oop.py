class Employee(object):
    def __init__(self, name, emp_id, payrate):
        self._name = name
        self._emp_id = emp_id
        self._payrate = payrate

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getId(self):
        return self._emp_id

    def pay(self):
        return self._payrate


class HourlyEmployee(Employee):
    def __init__(self, name, emp_id, payrate, hours):
        super().__init__(name, emp_id, payrate)
        self._hours = hours

    def pay(self):
        return Employee.pay(self) * self._hours

    def getHours(self):
        return self._hours

    def setHours(self, hours):
        self._hours = hours
