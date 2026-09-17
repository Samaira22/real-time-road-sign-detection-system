import time

last_alert_time = 0


def check_alert(class_name, cooldown=3):
    global last_alert_time

    if class_name != "stop":
        return False

    current_time = time.time()

    if current_time - last_alert_time >= cooldown:
        print("ALERT: STOP SIGN DETECTED!")
        last_alert_time = current_time
        return True

    return False