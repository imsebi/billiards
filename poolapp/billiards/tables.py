import django_tables2 as tables
from .models import Profile
class UserTable(tables.Table):
    class Meta:
        model = Profile