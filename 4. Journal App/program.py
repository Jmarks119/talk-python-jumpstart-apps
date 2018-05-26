import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('---------------------------')
    print('       JOURNAL APP')
    print('---------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'X' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.upper().strip()

        if cmd == 'L':
            list_entries(journal_data)
        elif cmd == 'A':
            add_entry(journal_data)
        elif cmd != 'X' and cmd:
            print("Sorry, the command '{}' is not understood.".format(cmd))

    print('Goodbye!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print("[{}] {}".format(index + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':
    main()
