from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        # Adding a User-Agent header to mimic a browser request
        self.client.get("/login", headers={"User-Agent": "Mozilla/5.0"})
        self.client.get("/in/LoginHelp", headers={"User-Agent": "Mozilla/5.0"})