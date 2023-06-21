# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the user table from our database


class Users:
    DB = "users_schema"  

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = """
        
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        
        """
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod  # <----- EDIT VALUES
    def get_one(cls, data):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s ;
                """
        results = connectToMySQL('users_schema').query_db(query, data)

        return cls(results[0])
    
    @classmethod   #<------- UPDATE
    def update(cls, data):
        query = """
            UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s, email=%(email)s
            WHERE id = %(id)s
                """
        results = connectToMySQL('users_schema').query_db(query, data)
        return results
    
    @classmethod  # <------- DELETE
    def delete(cls, data):
        query = """
        DELETE FROM users 
        WHERE ID = %(id)s ;
        """

        results = connectToMySQL('users_schema').query_db(query, data)

        return results
    
    @classmethod    #<---- SHOW USERS
    def show(cls, data):
        query = """ 
        SELECT * FROM users
        """
