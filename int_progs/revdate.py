#! /usr/bin/python

"""
Need to find previous n days date without using any date related inbuilt function.  
Just use date command and get current day/month/yr and take input in days for previous n days 
and return new date.
"""
import subprocess
import sys

# [seconds_in_a_day, seconds_in_month, seconds_in_year]
ss = [86400, 2629743, 31556926]

# reference time hsould be considered as jan 1st of 1970
ref_date = [01, 01, 1970]


def main(days):
    today = subprocess.check_output('date +%d:%m:%Y', shell=True).strip()
    today = [int(i) for i in today.split(':')]
    #print(today, ref_date)
    delta = [j-i for i, j  in zip(ref_date, today)]
    curr_sec = sum([cur * val for cur, val in zip(delta, ss)])
    #print("Curr_diff : ", curr_sec)
    days  = int(days)
    daysinsec = days * 86400
    #print("Days in sec : ", daysinsec)
    #print("sec delta : ", curr_sec - daysinsec)
    tim = curr_sec - daysinsec

    i = 2
    final = []
    while tim and i >= 0:
        if i == 2:
            final.append(tim/ss[i] + 1970)
        elif i == 1:
            final.append(tim/ss[i] + 1)
        else:
            final.append(tim/ss[i])
        tim = tim % ss[i]
        #print tim
        i -= 1
        #print (i)
    final.reverse()
    print(final)


if __name__ == "__main__":
    main(sys.argv[1])
