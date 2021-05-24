from locust import User, task, between,  events

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")


def performtask1(self):
    print("task1")

def performtask2(self):
    print("task2")

class MyUser(User):
    wait_time = between(1, 2)
    host = "www.google.com"
    tasks = {performtask1:3, performtask2:6}

    #Executed per user before starting task
    def on_start(self):
        print("Logging in")

    # Executed per user after task is complete
    def on_stop(self):
        print("Logging off")
