from django.db import models


from django.db import models
class PuestoManager(models.Manager):
    def asignar_permiso(self, permiso):
        self.permisos.add(permiso)

    def quitar_permiso(self, permiso):
        self.permisos.remove(permiso)