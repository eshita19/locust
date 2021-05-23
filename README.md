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
