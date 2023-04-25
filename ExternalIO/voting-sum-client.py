#!/usr/bin/python3

import sys
import threading
from client import *
from domains import *

def read_vote_vectors(filename, num_candidates):
    with open(filename, 'r') as f:
        vote_vectors = [list(map(int, line.strip().split())) for line in f]
        for vector in vote_vectors:
            if len(vector) != num_candidates:
                print("Error: Invalid vote vector size.")
                sys.exit(1)
    return vote_vectors

def create_client(client_id, n_parties, vote_vector, finish):
    client = Client(['localhost'] * n_parties, 14000, client_id)

    type = client.specification.get_int(4)

    if type == ord('R'):
        domain = Z2(client.specification.get_int(4))
    elif type == ord('p'):
        domain = Fp(client.specification.get_bigint())
    else:
        raise Exception('invalid type')

    for socket in client.sockets:
        os = octetStream()
        os.store(finish)
        os.Send(socket)

    # for x in vote_vector:
    client.send_private_inputs([domain(x) for x in vote_vector])

    # print('Winning client id is :',
    #           client.receive_outputs(domain, 1)[0].v)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script.py <n_parties> <vote_vectors_file> <num_candidates> <client_num>")
        sys.exit(1)

    n_parties = int(sys.argv[1])
    vote_vectors_file = sys.argv[2]
    num_candidates = int(sys.argv[3])
    client_num = int(sys.argv[4])

    vote_vectors = read_vote_vectors(vote_vectors_file, num_candidates)

    if len(vote_vectors) != client_num:
        print("Error: The number of vote vectors in the file does not match the number of clients.")
        sys.exit(1)

    threads = []

    for i in range(client_num):
        finish = 1 if i == client_num - 1 else 0
        t = threading.Thread(target=create_client, args=(i, n_parties, vote_vectors[i], finish))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
