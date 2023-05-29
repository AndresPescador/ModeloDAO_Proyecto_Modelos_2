from UsuarioDAO import UsuarioDAO
from RolDAO import RolDAO
from PermisoDAO import PermisoDAO

def PruebasUsuario():
    usuarioDao = UsuarioDAO()
    usuarioDao.AñadirUsuario("Andres","Pescador","1020")
    usuarioDao.ObtenerUsuarios()
    usuarioDao.ActualizarContrasenaUsuario(1,"2021")
    usuarioDao.EliminarUsuario(10)
    print("\nDespúes de modificar: \n")
    usuarioDao.ObtenerUsuarios()


def PruebasRol():
    rolDao = RolDAO()
    rolDao.AñadirRol("Empleado","Descripcion")
    rolDao.ObtenerRoles()
    rolDao.ActualizarAtributosRol(1,"Descripcion Atributos")
    rolDao.EliminarRol(2)
    print("\nDespúes de modificar: \n")
    rolDao.ObtenerRoles()

def PruebasPermiso():
    permisoDao = PermisoDAO()
    permisoDao.AñadirPermiso("Descripción #3")
    permisoDao.ObtenerPermisos()
    permisoDao.ActualizarDescripcion(3,"Descripción Actualizada")
    permisoDao.EliminarPermiso(2)
    print("\nDespúes de modificar: \n")
    permisoDao.ObtenerPermisos()

#PruebasUsuario()
#PruebasRol()
#PruebasPermiso() 