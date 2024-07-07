import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

start_date = date.today()
end_date = start_date + relativedelta(months=-6)

print(start_date.strftime("%Y-%-m-%-d"))
print(end_date.strftime("%Y-%-m-%-d"))

# Specify start, end, and periods; the frequency is generated automatically (linearly spaced).
df = pd.date_range(start=start_date, end=end_date, periods = 12)

#for splunk the exact date/time format is %m/%d/%Y:%H:%M:%S
# https://docs.splunk.com/Documentation/SCS/current/Search/Specifyingtimeranges
for i in df:
    print(i.strftime("%m/%d/%Y:%H:%M:%S"))
