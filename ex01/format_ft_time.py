import datetime

past_dt = datetime.datetime(1970, 1, 1)
current_dt = datetime.datetime.now()
delta = (current_dt - past_dt)
# print(past_dt)
# print(current_dt)
print("Total Seconds: ", "{:.1e}".format(delta.total_seconds()))
