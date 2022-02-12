import random
import time


bcolors = {
    'HEADER': '\033[95m',
    'OKBLUE': '\033[94m',
    'OKCYAN': '\033[96m',
    'OKGREEN': '\033[92m',
    'WARNING': '\033[93m',
    'FAIL': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m'
}


def colors(color, message):
    return f'{bcolors[color]}{message}{bcolors["ENDC"]}'


def turn_off(battery_life, start_time):
    return not (battery_life < (time.time() - start_time))


def dirty_room(location, state_A, state_B):
    if location == 'B':
        state_A = random.choice(['DIRTY', 'CLEAN'])
    else:
        state_B = random.choice(['DIRTY', 'CLEAN'])

    return [state_A, state_B]


def reflex_agent(location, state):
    if state == 'DIRTY':
        return 'CLEAN UP'

    if location == 'A':
        return 'MOVE TO B'
    elif location == 'B':
        return 'MOVE TO A'


def start(params):
    start_time = time.time()

    location = params['room']
    state_A = params['state_A']
    state_B = params['state_B']
    battery_life = params['battery_life']

    print(colors(
        'OKGREEN',
        f'The vacuum cleaner has been turned on in room {location}.'
    ))

    while turn_off(battery_life, start_time):
        state = state_A if location == 'A' else state_B
        action = reflex_agent(location, state)

        print(colors(
            'ENDC',
            f'Location: {location} | State: {state} | Action: {action}'
        ))

        if action == 'CLEAN UP':
            if location == 'A':
                state_A = 'CLEAN'
            elif location == 'B':
                state_B = 'CLEAN'
        elif action == 'MOVE TO B':
            location = 'B'
        elif action == 'MOVE TO A':
            location = 'A'

        [state_A, state_B] = dirty_room(location, state_A, state_B)
        time.sleep(1)

    print(colors('FAIL', 'The vacuum cleaner has turned off.'))


if __name__ == '__main__':
    start({
        'room': 'B',
        'state_A': '',
        'state_B': 'CLEAN',
        'battery_life': 10
    })
