from django.contrib import admin
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

# No registrar el modelo User aquí ya que está registrado por defecto

# Si deseas mantener la función para referencia futura, puedes comentarla
# def create_groups(apps, schema_editor):
#     # Crear grupos
#     admin_group, created = Group.objects.get_or_create(name='Admin')
#     supervisor_group, created = Group.objects.get_or_create(name='Supervisor')
#     dentist_group, created = Group.objects.get_or_create(name='Dentist')
#
#     # Asignar permisos a los grupos
#     content_type = ContentType.objects.get_for_model(User)
#     permissions = Permission.objects.filter(content_type=content_type)
#
#     admin_group.permissions.set(permissions)
#     supervisor_group.permissions.set(permissions.filter(codename__in=['add_user', 'change_user']))
#     dentist_group.permissions.set(permissions.filter(codename__in=['view_user']))
#
# class Migration(migrations.Migration):
#     dependencies = [
#         ('auth', '0012_alter_user_first_name_max_length'),
#     ]
#
#     operations = [
#         migrations.RunPython(create_groups),
#     ]