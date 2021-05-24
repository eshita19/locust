from locust import TaskSet, User, between, task

class UserBehaviour(TaskSet):
    wait_time = between(1, 2)
    @task(1)
    def task1(self):
        print("This is task1")

    @task(2)
    def task2(self):
        print("This is task2")


class TestUser(User):
    tasks = [UserBehaviour];
