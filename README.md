# Linux + Ifttt + Email + Google Assistant = Google Control Linux Box
[![N|Python](https://www.python.org/static/community_logos/python-powered-w-100x40.png)](https://www.python.org)

# Requirement
 - Python2
    - imaplib
    - email
 - Android Smartphone
    - Compatible with Google Assistant
 - Gmail Email Adress
 - Any Linux Device
 - Ifttt account
    - Connect Gmail
    - Connect Google Assistant
 - VIM *optional
    - Vim is necessary because of line-folding is done. 

## Ifttt Template
```
Event:
 Google Assistant
  - What do you want to say?
    - Open Firefox in Laptop
  - What do you want the Assistant to say in response?
    - Opening Firefox in Laptop
Actions
  Gmail
   - To address
     - You Gmail Address
   - Subject
     - {Actual Command} <-- remove '{}'
   - Body
     - *Optional
```

## Python Configuring Template
```
 - Actions
  - actions["Laptop_Lock"] = ["laptop locking", "subprocess.call(['i3lock', '-c', '000000'])"]
   - actions["Laptop_Lock"] <= it is command that is passed by Ifttt Template {Actual Command}
   - "laptop locking" <= This will be printed in terminal.
   - "subprocess.call(['i3lock', '-c', '000000'])" <= it will command that will run.
```

## Python add command / functionality
```
 - Actions
  *Create a new line beneath actions{}
   - actions["Testing"] = ["this is test", "subprocess.call(['touch', '/tmp/testing_file'])"]
 - Ifttt
   - Follow the ifttt template
```

## How to Run Code.
```
./ifttt_email.py "email_id" "password"
  - or you can replace the variable of userName and passWord with your gmail user + password
```

## Sidenote
```
 - Can use any OS
 - Can replace the print in terminal to speak or notification
 - Use any email
   - You have to configure that.
 - Doesn't need Google Assistant, you can control by just emailing it.
```

## Things You Can
```
 - Everything that python + OS can do; even shutdown the system.
 - ^^^ Everythings.
 - Configure this in Raspberry Pi; and control any GPIO module.
```


```
       _                  _                 _          _ _____
 _ __ (_)_ __ __ _ _ __  (_) __ _ _ __  ___| |__  _ __/ |___ /
| '_ \| | '__/ _` | '_ \ | |/ _` | '_ \/ __| '_ \| '__| | |_ \
| | | | | | | (_| | | | || | (_| | | | \__ \ | | | |  | |___) |
|_| |_|_|_|  \__,_|_| |_|/ |\__,_|_| |_|___/_| |_|_|  |_|____/
                       |__/
```
- https://keybase.io/niranjanshr13
- https://github.com/niranjanshr13
- https://twitter.com/niranjanshr13
- https://www.linkedin.com/in/niranjanshr13

