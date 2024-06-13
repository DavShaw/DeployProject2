from locust import HttpUser, task

class CodeWizardNotes(HttpUser):
    @task
    def noteTaks(self):
        self.client.get("/")
        self.client.get("/login")
        self.client.get("/sign-up")
        self.client.get("/delete-note")
        self.client.get("/logout")

if __name__ == "__main__":
    import os
    currentDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(currentDir)
    os.system("locust -f locustfile.py")
