# Repl for fun
from datetime import date

# Constants
HEADER = "Welcome to REPL, type 'help' for command list, 'exit' for exit from REPL"
FOOTER = "Thanks for using REPL!"
PROMPT_COMMAND = ": "
PROMPT_ECHO = ">> "

# Message strings
MSG_ECHO_ON = 'Echo mode is on'
MSG_ECHO_OFF = 'Echo mode is off'

# Error string
ERR_WRONG_COMMAND = 'Wrong command: {0}'

# System Commands
CMD_EXIT = 'exit'
CMD_ECHO_ON = 'echo_on'
CMD_ECHO_OFF = 'echo_off'
CMD_HELP = 'help'

# Commands
CMD = ['hello_world', 'current_date']


# Building commands
def cmd_hello_world():
    print("HELLO WORLD")


def cmd_current_date():
    print('{0}{1}'.format(PROMPT_ECHO, date.today()))


# Main block
def main():
    # System Variables
    var_echo = False

    # Header for REPL
    print(HEADER)

    # Infinite loop
    while True:
        # Get command from console
        rep = input(PROMPT_COMMAND)

        # echo mode
        if var_echo: print('{0}{1}'.format(PROMPT_ECHO, rep))

        # exit command
        if rep == CMD_EXIT:
            break
        else:
            # Command Processor
            # System Command
            # echo_on command
            if rep == CMD_ECHO_ON:
                var_echo = True
                print(MSG_ECHO_ON)

            # echo_off command
            elif rep == CMD_ECHO_OFF:
                var_echo = False
                print(MSG_ECHO_OFF)

            # help command
            elif rep == CMD_HELP:
                for c in CMD:
                    print(c)

            # Building commands
            elif rep in CMD: eval('cmd_' + rep + '()')

            # Command not found
            else: print(ERR_WRONG_COMMAND.format(rep))

    # Footer for repl
    print(FOOTER)


if __name__ == '__main__':
    main()




