from django.db import models
import datetime

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_age(self):
        birth = self.birth_date.year
        now = datetime.datetime.now()
        now1 = now.year
        age =  now1 - birth

        return f'возраст - {age} лет(года)'


class Employee(AbstractPerson):
    position = models.CharField(max_length=30)
    salary = models.IntegerField()
    work_experience = models.DateField()




class Passport(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=9)

    def get_gender(self):
        if self.inn.startswith('1'):
            return 'female'
        else:
            return 'male'

    def __str__(self):
        return f'{self.employee} - {self.inn} - {self.id_card}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Поле Passport с данными ИНН - {self.inn} №{self.id_card} сохранено')


class WorkProject(models.Model):
    project_name = models.CharField(max_length=30)
    employees = models.ManyToManyField(Employee, through='MemberShip')

    def __str__(self):
        return self.project_name


class MemberShip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workproject = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.employee.name} - {self.workproject.project_name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'поле Membership с данными сотрудник - {self.employee}, '
              f'проект {self.workproject} дата вступления {self.date_joined} '
              f'сохранено')


class Client(AbstractPerson):
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.address} - {self.phone_number}'


class VipClient(Client):
    vip_status_start = models.CharField(max_length=20)
    donation_amount = models.IntegerField(default=0)

