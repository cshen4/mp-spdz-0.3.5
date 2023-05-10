import subprocess
import time

# Define a function to run a pair of commands with a 1 second delay between them


def run_command_pair(num_parties, num_candidates, num_clients, protocol):
    print(f"Running {protocol} with {num_parties} parties {num_candidates} candidates and {num_clients} voters")

    output_file = f"{protocol}:{num_parties}:{num_candidates}:{num_clients}.txt"
    gen_votes_file = subprocess.Popen(f"python3 /home/shared/mp-spdz-0.3.5/Player-Data/gen_votes2.py {num_clients} {num_candidates} > /home/shared/mp-spdz-0.3.5/Player-Data/votes.txt", shell=True)
    gen_votes_file.wait()

    comp = subprocess.Popen(f"./compile.py voting_sum_v2 1 {num_candidates} {num_clients}", shell=True)
    comp.wait()

    command1 = f"python3 ExternalIO/voting-sum-client.py {num_parties} ./Player-Data/votes.txt {num_candidates} {num_clients}"
    command2 = f"PLAYERS={num_parties} Scripts/{protocol}.sh voting_sum_v2-1 {num_candidates} {num_clients}  > {output_file}"


    print(command1)
    print(command2)

    # Run the first command
    process1 = subprocess.Popen(command1, shell=True)
    
    # Wait 1 second
    time.sleep(1)
    
    # Run the second command
    process2 = subprocess.Popen(command2, shell=True)
    
    # Wait for both commands to finish
    process1.wait()
    process2.wait()

list_of_protocols = ["atlas", "shamir", "mal-shamir", "sy-shamir"]
num_parties = [3,4,5,6]
num_candidates = [3,6,8,10]

for c in num_candidates:
    for p in list_of_protocols:
        run_command_pair(4,c,100,p)

