import subprocess
import time

import pandas as pd
from parser import parse_input
# Define a function to run a pair of commands with a 1 second delay between them


def run_parser(num_parties, num_candidates, num_clients, protocol):
    output_file = f"{protocol}:{num_parties}:{num_candidates}:{num_clients}.txt"

    try:
        time_str, data_sent_str, rounds_str, global_data_sent_str = parse_input(output_file)
        return float(time_str), float(data_sent_str.split(" ")[0]), int(rounds_str), float(global_data_sent_str.split(" ")[0]),
    except:
        return None, None, None, None

list_of_protocols = ["atlas", "shamir", "mal-shamir", "sy-shamir"]
num_parties = [3,4,5,6]
num_candidates = [3,6,8,10]


num_candidates = 4
num_voters = 100


data = []
columns = ["protocol", "parties", "candidates", "voters", "time", "data sent", "rounds", "global data sent"]

for n in num_parties:
    for p in list_of_protocols:
        time, data_sent, rounds, global_data_sent = run_parser(n,num_candidates,num_voters,p)
        data.append([p,n, num_candidates, num_voters, time, data_sent, rounds, global_data_sent])

df = pd.DataFrame(data, columns=columns)
df = df.sort_values("protocol")

df.to_csv("first_exp.csv")



