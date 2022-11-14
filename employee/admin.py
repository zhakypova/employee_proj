from django.contrib import admin
from employee.models import  Employee, Passport, WorkProject, \
    MemberShip, Client, VipClient

admin.site.register(Employee)
admin.site.register(Passport)
admin.site.register(WorkProject)
admin.site.register(Client)
admin.site.register(VipClient)
admin.site.register(MemberShip)
