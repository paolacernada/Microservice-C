import zmq
import time

# Initialize ZeroMQ context and REP socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")


def calculate_probability(num_dice, target):
    if target < 1 or target > 6:
        return 0  # Invalid target number for a standard 6-sided die

    probability_of_not_getting_target = (5/6) ** num_dice
    probability_of_getting_target_at_least_once = 1 - probability_of_not_getting_target

    return probability_of_getting_target_at_least_once


print("Microservice C is running...")
time.sleep(0.5)


while True:
    print("Waiting for requests...")
    message = socket.recv_json()
    print("Received request.")
    time.sleep(0.5)

    command = message['command']

    if command == 'calculate_probability':
        num_dice = message['num_dice']
        target = message['target']
        print(f"Calculating probability for rolling {target} with {num_dice} dice...")
        time.sleep(1)  # Pause for 1 second during the calculation
        probability = calculate_probability(num_dice, target)
        print("Calculation completed. Sending probability result...")
        time.sleep(0.5)
        socket.send_json({"probability": probability})
        print("Probability result sent.")
        time.sleep(0.5)

    elif command == 'compare_probabilities':
        num_dice = message['num_dice']
        targets = message['targets']
        print(f"Calculating probabilities for targets {targets} with {num_dice} dice...")
        time.sleep(1)
        probabilities = {
            target: calculate_probability(num_dice, target)
            for target in targets
        }
        print("Calculations completed. Sending probability results...")
        time.sleep(0.5)
        socket.send_json(probabilities)
        print("Probability results sent.")
        time.sleep(0.5)

    else:
        print("Invalid command received. Sending error response...")
        time.sleep(0.5)
        socket.send_string("Invalid command.")
        print("Error response sent.")
        time.sleep(0.5)
