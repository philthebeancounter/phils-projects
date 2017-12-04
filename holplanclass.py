class Employee(object):

    def __init__(self,name,hol_allowance):
        self.name = name
        self.hol_allowance = hol_allowance


    def add_hol(self,days):
        self.hol_allowance = self.hol_allowance - days

data=open('data.txt','a')
name_input = raw_input("name> ")
hol_allowance_input = input ("annual allowance days> ")
hours_per_week = input ("Hours per week >")
days_per_week = input ("Days worked per week")
company_entitlement = input ("Annual entitlement >")
employee_entitlement = days_per_week / 5 * company_entitlement
print "employe entitlement" employee_entitlement







employee = Employee(name_input,hol_allowance_input)
employee.add_hol(1)


#print employee.name
data.write(employee.name)
data.write(str(employee.hol_allowance))
print employee.hol_allowance
