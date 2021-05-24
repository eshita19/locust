## https://developer.todoist.com/rest/v1/#overview

from locust import HttpUser, task, between,  events, SequentialTaskSet
import uuid

class ProjectBehaviour(SequentialTaskSet):
    def on_start(self):
        self.token = '89a91426a4ff1c04fa9240e8b8fd6d47b8355dd7'
        self.randomid = uuid.uuid4()

    @task
    def GetProject(self):
        resp = self.client.get('',
                                headers={
                                    "Accept": "application/json",
                                    "Authorization": "Bearer " + self.token
                                })
        print('Response Code: ' + str(resp.status_code))
        print('Response Headers: ' + str(resp.headers))
        print('Response Body json: '+ str(resp.json()))
        print('Response text: ' + str(resp.text))
        resp.raise_for_status() #Raise error if in 4XX or 5XX status code.

    @task
    def postProject(self):
        resp = self.client.post('',
                               headers = {
                                   "content-type": "application/json",
                                   "Authorization": "Bearer " + self.token
                               },
                               json = {
                                "id": 2203306141,
                                "name": "Shopping List2",
                                "comment_count": 0,
                                "color": 47,
                                "shared": False,
                                "sync_id": 0,
                                "order": 1,
                                "favorite": False,
                                "url": "https://todoist.com/showProject?id=2203306141"
                            })
        print('Response Code: ' + str(resp.status_code))
        print('Response Headers: ' + str(resp.headers))
        print('Response Body json: ' + str(resp.json()))
        print('Response text: ' + str(resp.text))
        resp.raise_for_status()  # Raise error if in 4XX or 5XX status code.


class HttpClient(HttpUser):
    host = "https://api.todoist.com/rest/v1/projects"
    tasks = [ProjectBehaviour]





