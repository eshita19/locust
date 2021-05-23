# Locust

## Basic Script
Screenshot 2021-05-23 at 4.09.26 PM![image](https://user-images.githubusercontent.com/33754197/119257061-4388b300-bbe1-11eb-8bcc-4f2983aa7923.png)
`locust -f m1.py`
- This defines a user thread instance. The class need to extend user/httpuser class from Locust. Define a method with @task annotation.
