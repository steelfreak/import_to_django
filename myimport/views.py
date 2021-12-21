from django.shortcuts import render
from .resources import EmployeeResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .models import Employee


def simple_upload(request):
	if request.method == 'POST':
		employee_resource = EmployeeResource()
		dataset = Dataset()
		new_employee = request.FILES['myfile']

		if not new_employee.name.endswith('xlsx'):
			messages.info(request, 'wrong format')
			return render(request, 'upload.html')

		imported_data = dataset.load(new_employee.read(),format='xlsx')
		for data in imported_data:
			value = Employee(
				data[0],
				data[1],
				data[2],
				)
			value.save()
	return render(request, 'upload.html')