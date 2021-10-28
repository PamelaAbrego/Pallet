from core.pyba_logic import PybaLogic

class CatalogoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertCatalogo(self, fecha, nombre, correo, celular, categoria, articulo, cantidad):
        database = self.databaseObj
        sql = (
            "INSERT INTO `heroku_de080cfa793afc7`.`catalogo`(`id`, `Fecha`, `Nombre`, `Correo`, `Celular`, `Categoría`, `Producto`, `Cantidad`, `Enviado`)"
            + f"VALUES (0,'{fecha}', '{nombre}', '{correo}','{celular}','{categoria}' , '{articulo}',{cantidad},0);"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllCatalogo(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM heroku_de080cfa793afc7.catalogo;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def updateEnviado(self, id):
        database = self.databaseObj
        sql = (
            "UPDATE `heroku_de080cfa793afc7`.`catalogo`"
            + f"SET `Enviado` = 1 "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getIdCatalogo(self, fecha, nombre, celular, correo, categoria, producto, cantidad):
        database = self.databaseObj
        sql = f"SELECT id FROM heroku_de080cfa793afc7.catalogo where Fecha like '{fecha}' and Nombre like '{nombre}' and Celular like '{celular}' and Correo like '{correo}' and Categoría like '{categoria}' and Producto like '{producto}' and Cantidad = {cantidad};"
        result = database.executeQuery(sql)
        return result

    def updateUsuario(self, id, usuario):
        database = self.databaseObj
        sql = (
            "UPDATE `heroku_de080cfa793afc7`.`usuarios` "
            + f"SET `user` = '{usuario['user']}', `email` = '{usuario['email']}',`role` = '{usuario['role']}', `password` = '{usuario['password']}', `salt` = '{usuario['salt']}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllCatalogoSinEnviar(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM heroku_de080cfa793afc7.catalogo WHERE Enviado like '0';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def getAllCatalogoEnviados(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM heroku_de080cfa793afc7.catalogo WHERE Enviado like '1';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []




