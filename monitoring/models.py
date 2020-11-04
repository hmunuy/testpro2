from django.db import models


# Create your models here.
class Host(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    update_time = models.CharField(max_length=200)

class get_interface(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    update_time = models.CharField(max_length=200)

class get_cpu_ram(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    cpu_temp = models.IntegerField()
    ram_usage = models.IntegerField()
    update_time = models.CharField(max_length=200)

class get_uptime(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    uptime = models.CharField(max_length=200)
    update_time = models.CharField(max_length=200)

class get_traffic(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    interface = models.CharField(max_length=200)
    inbound = models.CharField(max_length=200)
    outbound = models.CharField(max_length=200)
    update_time = models.CharField(max_length=200)

class get_clients(models.Model):
    ip_hostname = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    clients = models.IntegerField()
    update_time = models.CharField(max_length=200)

class get_clients_detail(models.Model):
    ip_clients = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    update_time = models.CharField(max_length=200)

