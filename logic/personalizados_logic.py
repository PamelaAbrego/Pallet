from core.pyba_logic import PybaLogic

class PersonalizadosLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertPersonalizado(self, fecha, nombre, correo, celular, descripcion):
        database = self.databaseObj
        sql = (
            "INSERT INTO `pallet`.`personalizados` (`id`,`Fecha`,`Nombre`,`Correo`,`Celular`,`Descripción`,`Enviado`)"
            + f"VALUES (0,'{fecha}', '{nombre}', '{correo}','{celular}','{descripcion}',0);"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllPersonalizados(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM pallet.personalizados;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def updateEnviado(self, id):
        database = self.databaseObj
        sql = (
            "UPDATE `pallet`.`personalizados` "
            + f"SET `Enviado` = 1 "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getIdPersonalizado(self, fecha, nombre, celular, correo, descripcion):
        database = self.databaseObj
        sql = f"SELECT id FROM pallet.personalizados where Fecha like '{fecha}' and Nombre like '{nombre}' and Celular like '{celular}' and Correo like '{correo}' and Descripción like '{descripcion}';"
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

    def getAllPersonalizadosSinEnviar(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM pallet.personalizados WHERE Enviado like '0';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def getAllPersonalizadosEnviados(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * "
            + f"FROM pallet.personalizados WHERE Enviado like '1';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def deleteUsuario(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `heroku_de080cfa793afc7`.`usuarios` WHERE id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def checkUser(self, user):
        database = self.databaseObj
        sql = f"SELECT user FROM `heroku_de080cfa793afc7`.`usuarios` WHERE user like '{user}';"
        result = database.executeQuery(sql)
        return result

    def getUserByName(self, userName):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user, password, salt, role "
            + f"FROM heroku_de080cfa793afc7.usuarios where user like '{userName}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getEmailByName(self, userName):
        database = self.createDatabaseObj()
        sql = (
            "SELECT email "
            + f"FROM heroku_de080cfa793afc7.usuarios where user like '{userName}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]["email"]
        else:
            return []



