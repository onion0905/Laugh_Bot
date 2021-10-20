import datetime

today = datetime.date.today()
with open("dialogue_log.txt", "a") as log:
    log.write(str(today))
    log.write("\n")

print("Running")

while True:
    if today != datetime.date.today():
        today = datetime.date.today()
        with open("dialogue_log.txt", "a") as log:
            log.write(str(today))
            log.write("\n")

print(today)