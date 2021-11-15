import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Your Upcoming CA Is Next Week",
            timeout=10,
            message='START PREPARING For Your CA',
            toast=False
        )
        time.sleep(1200)
