from threading import Timer
from win32gui import GetWindowText, GetForegroundWindow
from win32process import GetWindowThreadProcessId
from psutil import Process
from datetime import datetime
from peewee import SqliteDatabase, Model, CharField, DateTimeField, SQL

SAMPLING_DELAY = 10 # Seconds

current_db_name: str | None = None

db = SqliteDatabase(None)

class Moment(Model):
    process = CharField(max_length=150)
    window_title = CharField(max_length=50)
    date =  DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db


def insert_moment():
    try:
        date = datetime.now().isoformat().split('.')[0]
        window = GetForegroundWindow()
        process_ids = GetWindowThreadProcessId(window)
        window_title = GetWindowText(window)[:150]
        process = Process(process_ids[-1]).name()[:50]

        print(str(date).ljust(20), process.ljust(25), window_title)

        moment = Moment(process=process, window_title=window_title, date=date)
        return moment.save()

    except Exception as e:
        print(e)
        return None


def insert_schedule():
    thread = Timer(SAMPLING_DELAY, insert_schedule)
    thread.start()
    init_database()
    insert_moment()


def current_month():
    date = datetime.now()
    return f"{date.year}{date.month:02}"


def init_database():
    global current_db_name
    db_name = f"data_{current_month()}.db"

    if db_name == current_db_name:
        return

    if current_db_name is None:
        print(f"Using database {db_name}")
    else:
        print(f"Change database to {db_name}")

    current_db_name = db_name

    db.init(current_db_name)
    db.connect()
    db.create_tables([Moment])


if __name__ == '__main__':
    insert_schedule()