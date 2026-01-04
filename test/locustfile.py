from locust import HttpUser, task, between


class GetRoot(HttpUser):
    wait_time = between(1, 5)

    @task
    def root_route(self):
        self.client.get("/health")

    # @task
    # def post_route(self):
    #     self.client.post(
    #         "/api/v1/ask", json={"question": "What true happiness", "author": "Plato"}
    #     )
