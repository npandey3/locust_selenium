from locust import TaskSet, task
from realbrowserlocusts import HeadlessChromeLocust


class LocustUserBehavior(TaskSet):

    def open_lipitor_page(self):
        self.client.get("https://www-staging.goodrx.com/lipitor")

    def click_on_1st_coupon(self):
        self.client.find_element_by_xpath('//*[@id="uat-expanded-row-action-button-coupon-0"]').click()

    @task(1)
    def get_coupon(self):
        self.client.timed_event_for_locust("Go to", "lipitor_price_page", self.open_lipitor_page)
        self.client.timed_event_for_locust("Get Lipitor Coupon", "lipitor_coupon", self.click_on_1st_coupon)


class LocustUser(HeadlessChromeLocust):
    host = "not really used"
    timeout = 30  # in seconds in waitUntil thingies
    min_wait = 50
    max_wait = 100
    screen_width = 1200
    screen_height = 600
    task_set = LocustUserBehavior
