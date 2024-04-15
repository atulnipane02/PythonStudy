from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta

utcnow = timezone('utc').localize(datetime.utcnow())

xt = utcnow.astimezone(timezone('US/Eastern')).replace(tzinfo=None)

yt = utcnow.astimezone(timezone('Asia/Ho_Chi_Minh')).replace(tzinfo=None)

diff = relativedelta(xt, yt)
print(diff)
