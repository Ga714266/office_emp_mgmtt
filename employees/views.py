from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required, user_passes_test

# View to list all employees
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

# View to list all employees with optional filtering
@login_required
@user_passes_test(lambda u: u.is_superuser)
def employee_list(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(position__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# View to delete an employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')

def home(request):
    return render(request, 'home.html')

