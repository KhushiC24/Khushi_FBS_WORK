basic = int(input('Enter Basic Salary'))

Da = ((10/100) * basic)
Ta = ((12/100) * basic)
hra = ((15/100) * basic)

Total_Salary = basic + Da + Ta + hra

print(f'Total Salary of employee is {Total_Salary}')