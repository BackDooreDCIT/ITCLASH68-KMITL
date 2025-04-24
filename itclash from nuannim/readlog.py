def main():
    log = input()

    loggedinlist = []

    logslicing0 = log.find('[')
    logslicing1 = log.find(']')

    logdatetime = log[logslicing0+1 : logslicing1]
    logstatus = log[logslicing1 + 2 :]
    
    logdatetime = logdatetime.split()

    logdayssplit = logdatetime[0].split('/')
    logtimesplit = logdatetime[1].split(':')

    logday = logtimesplit
    # logmonth
    # logyear

    # loghour
    # logminute
    # logsecond


    print(logdatetime)
    print(logstatus)

    print(logdayssplit)
    print(logtimesplit)

    if logstatus == 'Reception Opened.':
        while(True):
            log = input()



main()