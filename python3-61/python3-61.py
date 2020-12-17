#DateTime
#Working with dates, times, deltas and formats

#Imports
from datetime import datetime, timedelta
from time import strftime

def main():
    #Now
    #If the host machine is in the UTC timezone then there will be no difference between
    now = datetime.now()
    utc  = datetime.utcnow()
    print(f'Now: {now}')
    print(f'UTC: {utc}')
    print(f'Offset: {now.utcoffset()}')

    #Time
    print(f'Hour: {now.hour}')
    print(f'Minute: {now.minute}')
    print(f'Second: {now.second}')
    print(f'Micro: {now.microsecond}')

    #Date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')

    #Timedelta
    print(f'Next Month: {now + timedelta(days=30)}')
    print(f'Last Week: {now + timedelta(weeks=-1)}')
    print(f'5 Hours: {now + timedelta(hours=5)}')
    print(f'45 Seconds: {now + timedelta(seconds=45)}')
    print(f'200 Milliseconds: {now + timedelta(milliseconds=200)}')
    print(f'10 Microseconds: {now + timedelta(microseconds=10)}')

    #ISO Strings
    d = datetime.fromisoformat('2020-12-16')
    print(d)

    try:
        m = datetime.fromisoformat('20:26-06:00')
    except Exception as ex:
        print(ex.args)

    print(f'ISO: {now.isoformat()}')

    #Formatting 
    #https://www.w3schools.com/python/python_datetime.asp

    print(now.strftime('%y'))
    print(now.strftime('%Y'))
    print(now.strftime('%d'))
    print(now.strftime('%D'))
    print(now.strftime('%b'))
    print(now.strftime('Today is %B %d'))

if __name__ == "__main__":
    main()
