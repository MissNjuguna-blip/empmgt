from rest_framework import serializers

from employees.models import Department,Employee

# department serializers
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Department
        fields='__all__'
        # include all fields from the department model 

class EmployeeSerializer(serializers.ModelSerializer):
    # read only shows full nested department on get request

    department=DepartmentSerializer(read_only=True)
    # write only accepts a department id integer during POST/PUT
    department_id=serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True
    )

    class Meta:
        model = Employee
        fields = "__all__"