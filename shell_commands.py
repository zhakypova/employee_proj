from employee.models import *
from django.db.models import Subquery

emp_1 = Employee.objects.create(
name = 'Zulaika Zhakypova', birth_date = '1998-04-14',
    position = 'manager', salary = 30000,
    work_experience = '2019-08-27'
)
emp_2 = Employee.objects.create(
name = 'Gabriel Solis', birth_date = '1985-01-06',
    position = 'model', salary = 50000,
    work_experience = '2000-06-25'
)

emp_3 = Employee.objects.create(
name = 'Mike Delfino', birth_date = '1986-02-04',
    position = 'artist', salary = 25000,
    work_experience = '2001-10-15'
)

emp_4 = Employee.objects.create(
name = 'Tom Scavo', birth_date = '1985-08-21',
    position = 'shef', salary = 90000,
    work_experience = '2000-03-29'
)

passp_1 = Passport.objects.create(inn='11404199812345', id_card='ID1234567', employee=emp_1)
passp_2 = Passport.objects.create(inn='10601198523456', id_card='ID9865321', employee=emp_2)
passp_3 = Passport.objects.create(inn='20402198645678', id_card='ID7412365', employee=emp_3)
passp_4 = Passport.objects.create(inn='22108198545612', id_card='ID8521479', employee=emp_4)

emp_4.delete()

premium_life = WorkProject.objects.create(project_name='Premium Life')

# e1 = MemberShip.objects.create(employee=emp_1, workproject=premium_life, date_joined = '2000-03-29')
# e2 = MemberShip.objects.create(employee=emp_2, workproject=premium_life, date_joined = '2000-03-29')
# e3 = MemberShip.objects.create(employee=emp_3, workproject=premium_life, date_joined = '2000-03-29')
# e4 = MemberShip.objects.create(employee=emp_4, workproject=premium_life, date_joined = '2000-03-29')

premium_life.employees.set([emp_1, emp_2, emp_3], through_defaults={'date_joined' : '2000-03-29'})

premium_life.employees.remove(emp_3)

premium_life.employees.create(name='Susan Delfino', birth_date='1987-01-05',
                              position='teacher', salary = 50000,
                              work_experience='2003-12-10',
                              through_defaults={'date_joined':'2000-03-29'})


client_1 = Client.objects.create(name='Linnet Scavo', birth_date='1987-05-09',
                                 address='Baykerstreet 14', phone_number='0551222333')

client_2 = Client.objects.create(
    name='Enola Holmes', birth_date = '1975-04-08',
    address='Baykerstreet 22b', phone_number='0705030201'
)

client_3 = Client.objects.create(
    name='Sherlok Holmes', birth_date = '1968-04-04',
    address='Baykerstreet 22b', phone_number='0705784512'
)

vip_1 = VipClient(vip_status_start = '2022-11-14', address='Usenbayeva12', phone_number='0222334455')
client_1.delete()

Employee.objects.all()

WorkProject.objects.all()

work_proj = WorkProject.objects.filter(
    employees__id__in=Subquery(Employee.objects.filter(name__icontains='Zhakypova').values('id'))
)

Client.objects.all()

VipClient.objects.all()
