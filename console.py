import pdb 
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

user_repository.delete_all()
task_repository.delete_all()

user1 = User("Bob", "Morane")
user2 = User("Rory", "Banterson")
user3 = User("Alfred", "Batman")

user_repository.save(user1)
user_repository.save(user2)
user_repository.save(user3)

task1 = Task("Be predictable", "Rory", 1, user2, False)
task2 = Task("Roast chicken", "Bob", 120, user1, False)
task3 = Task("Gym", "Alfred", 30, user3, False)
task4 = Task("Gym", "Rory", 30, user2, False)

task_repository.save(task1)
task_repository.save(task2)
task_repository.save(task3)
task_repository.save(task4)

task1.description = "Be very predictable"

task_repository.update(task1)

# task_repository.delete(35)

# print(task_repository.select(26).__dict__)

print(f"user tasks: {user_repository.tasks(user2)}")

result = task_repository.select_all()
for task in result:
    print(task.__dict__)

pdb.set_trace()