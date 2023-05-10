import sys
from pathlib import Path

# Define a function to parse the piped input
def parse_input(file):
    input_str = Path(file).read_text()

    time_str = input_str.split("Time = ")[1].split(" seconds")[0]
    data_sent_str = input_str.split("Data sent = ")[1].split(" in ")[0]
    rounds_str = input_str.split("~")[1].split(" rounds")[0]
    global_data_sent_str = input_str.split("Global data sent = ")[1].split(" (all parties)")[0]
    
    return time_str, data_sent_str, rounds_str, global_data_sent_str



if __name__ == "__main__":
    # Parse the input using the function we defined earlier
    time, data_sent, rounds, global_data_sent = parse_input(sys.argv[1])

    # Print the results
    print("Time:", time)
    print("Data sent:", data_sent)
    print("Rounds:", rounds)
    print("Global data sent:", global_data_sent)
