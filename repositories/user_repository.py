from db.run_sql import run_sql

from models.user import User
import repositories.task_repository as task_repository


  
def select_all():  
    users= [] 

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row['last_name'])
        users.append(user)
    return users


# SAVE
def save(user):
    
    sql = "INSERT INTO users(first_name, last_name) VALUES (%s, %s) RETURNING *"

    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    user.id = id
    return user

# DELETE ALL
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

# SELECT
def select(id):
    task = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # Checking if the list return by `run_sql(sql, values` is empty. Empty lists are 'falsy'.
    # Could alternatively have: if len(results) > 0
    if results:
        result = results[0]
        task = User(result['first_name'], result['last_name'])
    return task

# DELETE
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE
def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name]
    run_sql(sql, values)

def tasks(user):
    sql = "SELECT * FROM tasks WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)
    
    return results
