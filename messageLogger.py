import datetime

def log(author, message):
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
    
    f = open("logs/messages.log", "a+")
    f.write("{} - {}: {}\n".format(timestamp, author, message))
    f.close()