from flask_app.config.mysqlconnection import connectToMySQL

class User():
    def __init__(self, data):
        self.id = data['iduser']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.handle = data['handle']
        self.birthday = data['birthday']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        connection = connectToMySQL('user_db_demo')
        users = connection.query_db('SELECT * FROM user;')

        # WHY DO WE DO THIS?! 

        # results = []
        # for user in users:
        #     results.append(cls(user))
        return users

    @classmethod
    def create_user(cls, data):
        connection = connectToMySQL('user_db_demo')
        query = "INSERT INTO user (first_name, last_name, handle, birthday, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(handle)s, %(birthday)s, NOW(), NOW());"
        # The query_db method returns the id number after running so we can save that for later
        new_user_id = connection.query_db(query, data)
        
        return new_user_id

    @classmethod
    def destroy(cls, data):
        connection = connectToMySQL('user_db_demo')
        # The ID must match the key in our data dictionary
        query = "DELETE FROM user WHERE iduser = %(id)s"
    # Delete method does NOT return anything therefore we put the query in the return

    # WHY IS THIS IN THE RETURN STATEMENT | WHY EVEN HAVE IT RETURN AT ALL?
        connection.query_db(query, data) 

    @classmethod
    def get_user(cls, data):
        connection = connectToMySQL('user_db_demo')

        query = "SELECT * FROM user WHERE iduser = %(id)s"
        # This comes back as a list
        results = connection.query_db(query, data)
        return results[0]
        
    @classmethod 
    def update_user(cls, data):
        connection = connectToMySQL('user_db_demo')
        query = "UPDATE user SET first_name=%(first_name)s, last_name=%(last_name)s,handle=%(handle)s,birthday=%(birthday)s, updated_at=NOW() WHERE iduser = %(id)s;"
        return connection.query_db(query, data)