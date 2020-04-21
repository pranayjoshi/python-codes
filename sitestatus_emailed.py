from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import smtplib 
s = []
result = []
with open("a.txt", "r") as fd:
    for line in fd:
        line = line.replace("\r", "").replace("\n", "")
        s.append(line)
def site_status(site):
    try:
        response = urlopen(site)
    except HTTPError as e:
        ret = ('The server couldn\'t fulfill the request.\nError code: ', e.code)
    except URLError as e:
        ret= ('We failed to reach a server.\nReason: ', e.reason)
    else:
        ret = 'Website is working fine'
    return ret
def sent_mail(result):
    resipiant = "name"
    content = result

    # init gmail SMTP
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    # identify to server
    mail.ehlo()

        # encrypt session
    mail.starttls()

        # login
    mail.login('email@gmail.com', 'pass')

        # send message
    mail.sendmail('recipient', 'recipient@gmail.com', content)

        # end mail connection
    mail.close()

    print('Email sent.')
for i in range(len(s)):
    a = site_status(s[i])
    res = (f"{i+1}. the status of {s[i]} is {a}")
    result.append(res)
print(result)
sent_mail(result)
