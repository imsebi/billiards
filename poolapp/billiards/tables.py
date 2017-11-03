import django_tables2 as tables

class UserTable(tables.Table):
    class Meta:
        model = Profile