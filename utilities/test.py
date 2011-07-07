from ConfigConstants import *
statFile = open("C:/Users/singhulariti/workspace/CapstonePy/src/resources/configFile.txt", 'r')
delayList = []
line = statFile.readline().replace('\n', '')
while line:    
    if line == DISK_DELAY_TOKEN:                            
        delayList.append(int(statFile.readline().replace('\n', '')))            
    elif line == CLIENT_DELAY_TOKEN:
        delayList.append(int(statFile.readline().replace('\n', '')))
    elif line == MANAGER_DELAY_TOKEN:
        delayList.append(int(statFile.readline().replace('\n', '')))
    elif line == LOCAL_CACHE_DELAY_TOKEN:
        delayList.append(int(statFile.readline().replace('\n', '')))
    elif line == LOG_MESSAGES_TOKEN:
        delayList.append(int(statFile.readline().replace('\n', '')))
    elif line == ADD_DELAY_TOKEN:
        delayList.append(int(statFile.readline().replace('\n', '')))
    else:
        line = statFile.readline().replace('\n', '')
    line = statFile.readline().replace('\n', '')
print delayList                       
getStats(delayList)