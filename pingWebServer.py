import platform  # For getting the operating system name
import subprocess  # For executing a shell command
import time  # for sleep

host = "<WebServer IP>"
host2 = "<WOLServer>"
token = "https://api.telegram.org/<TOKEN>/sendMessage"
chatid = "chat_id=<ID>"
WebDown = "text= Hey! The webserver is down!"
WOLDown = "text= Hey! The wolserver is down!"


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = "-c"

    # if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ["ping", param, "1", host]

    return subprocess.call(command) == 0


try:
    while True:
        if ping(host) and ping(host2):
            #            print("true")
            time.sleep(600)
        elif ping(host2) is False:
            time.sleep(60)  # try again in 60 seconds
            if ping(host2) is False:
                # subprocess.call(["curl", "-X", "POST" ,"-d", "\"\"", message2])
                subprocess.call(
                    ["curl", "-X", "POST", token, "-d", chatid, "-d", WOLDown]
                )
                time.sleep(600)
        else:
            #            print("false")
            time.sleep(60)  # try again in 60 seconds
            if ping(host) is False:
                # subprocess.call(["curl", "-X", "POST" ,"-d", "\"\"", message])
                subprocess.call(
                    ["curl", "-X", "POST", token, "-d", chatid, "-d", WebDown]
                )
                time.sleep(600)
except KeyboardInterrupt:
    print("Exiting")
