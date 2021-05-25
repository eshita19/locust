# Locust

## Basic Script
Screenshot 2021-05-23 at 4.09.26 PM![image](https://user-images.githubusercontent.com/33754197/119257061-4388b300-bbe1-11eb-8bcc-4f2983aa7923.png)
`locust -f m1.py`

### Locust terminologies - 
https://docs.locust.io/en/stable/writing-a-locustfile.html#user-class
1. **User Class**: A user class represents one user (or a swarming locust if you will). Locust will spawn one instance of the User class for each user that is being simulated.  
2. **wait_time attribute**: A User’s wait_time method is an optional attribute used to determine how long a simulated user should wait between executing tasks.
   - _constant_ for a fixed amount of time
   - _between_ for a random time between a min and max value
   - _constant_pacing_ for an adaptive time that ensures the task runs (at most) once every X seconds
3. **weight attribute**: If more than one user class exists in the file, If you wish to simulate more users of a certain type you can set a weight attribute on those classes.
4. **host attribute(--host)**: The host attribute is a URL prefix (i.e. “http://google.com”) to the host that is to be loaded.
5. **Task**: Add a task for a user using @task over a method. @task takes optional arg weight, used to specify the task’s execution ratio.
6. **on_start() and on_stop()**: Methods called per user, before and after completion of task. 
7. **test_start() and test_stop()**: Methods called during start and end of load.
8. **HTTPClient**: self.client.get(), self.client.post()
9. **Running locust through command line options**:
   1. _-f(--locustfile)_: Specify the file name to be run as locust file.
   2. _-H(--host)_: Specify the host against which load test will run.
   3. _-u(--users)_: Number of concurrent locust users.
   4. _-r(--spawn-rate)_:  Users added per second
   5. _-t(--run-time)_: Stop after the specified amount of time( e.g. 300s, 20m, 3h ).  Defaults to run forever.
   6. _--logfile_: Specify to which logs should be logged. 
   7. **Step load**: 
       - Increment the number of users not linearly but n users in duration of t time.
       - Define a class inheriting the LoadTestShape class in your locust file. In this class you define a tick() method that returns a tuple with the desired user count and spawn rate (or None to stop the test). Locust will call the tick() method approximately once per second.
       - https://docs.locust.io/en/stable/generating-custom-load-shape.html
   9.  
   
