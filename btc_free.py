import curses
import time
import datetime
import random

def draw_logo(stdscr):
    logo = """▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█▄▄░▄▄██░▄▄▀████░▄▄▄██░▄▄▀██░▄▄▄██░▄▄▄
██░▄▄▀███░████░███████░▄▄███░▀▀▄██░▄▄▄██░▄▄▄
██░▀▀░███░████░▀▀▄████░█████░██░██░▀▀▀██░▀▀▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

    """
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(2, 2, logo)
    stdscr.attroff(curses.color_pair(1))

def draw_datetime(stdscr):
    now = datetime.datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    stdscr.addstr(curses.LINES - 2, curses.COLS - len(dt_string) - 2, dt_string)

def display_user_info(stdscr, email, balance):
    color = random.randint(1, 6)
    stdscr.attron(curses.color_pair(color))
    stdscr.addstr(18, 2, f"User: {email}")
    stdscr.addstr(20, 2, f"BTC Balance: {balance:.8f}")
    stdscr.attroff(curses.color_pair(color))

def display_history(stdscr, history):
    stdscr.addstr(22, 2, "BTC MULTIPLY history:")
    for entry in history:
        stdscr.addstr(24 + history.index(entry), 2, entry)

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_BLUE, -1)
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)
    curses.init_pair(6, curses.COLOR_CYAN, -1)
    curses.init_pair(7, curses.COLOR_RED, -1)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    stdscr.addstr(10, 2, "BTC FREE BOT")
    stdscr.addstr(14, 2, "stratégie")
    stdscr.refresh()

    stdscr.addstr(16, 2, "Enter your email: ")
    email = stdscr.getstr().decode('utf-8')
    stdscr.addstr(17, 2, "Enter your password: ")
    password = stdscr.getstr().decode('utf-8')

    user_balance = 0.12345678
    time.sleep(1)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    display_user_info(stdscr, email, user_balance)
    stdscr.refresh()
    time.sleep(2)

    stdscr.clear()
    stdscr.border()
    draw_logo(stdscr)
    display_user_info(stdscr, email, user_balance)
    stdscr.addstr(22, 2, "Enter 'Run bot' to start the bot.")
    stdscr.refresh()

    history = []

    while True:
        draw_datetime(stdscr)
        key = stdscr.getstr().decode('utf-8')

        if key == 'q':
            break
        elif key == 'Run bot':
            stdscr.clear()
            stdscr.border()
            draw_logo(stdscr)
            display_user_info(stdscr, email, user_balance)
            stdscr.addstr(22, 2, "Bot is running...")
            stdscr.refresh()
            time.sleep(2)

            stdscr.clear()
            stdscr.border()
            draw_logo(stdscr)
            display_user_info(stdscr, email, user_balance)
            entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: You won 0.00000092 BTC!"
            history.append(entry)
            display_history(stdscr, history)
            stdscr.refresh()
            time.sleep(2)

curses.wrapper(main)
