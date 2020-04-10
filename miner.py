import hashlib
import requests

import sys
import json


def proof_of_work(block):
    """
    Simple Proof of Work Algorithm
    Stringify the block and look for a proof.
    Loop through possibilities, checking each one against `valid_proof`
    in an effort to find a number that is a valid proof

    :return: A valid proof for the provided block
    """
    block_string = json.dumps(block, sort_keys=True)

    new_proof = 0
    while valid_proof(block_string, new_proof) is False:
        new_proof += 1

    return new_proof


def valid_proof(block_string, new_proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?  Return true if the proof is valid

    :parameter block_string: <string> The stringified block to use to
    check in combination with `proof`

    :parameter proof: <int?> The value that when combined with the
    stringified previous block results in a hash that has the
    correct number of leading zeroes.

    :return: True if the resulting hash is a valid proof, False otherwise
    """
    # sh256 needs encoded input

    guess = f'{block_string}{new_proof}'.encode()
    # hexidigest makes easier to read
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:3] == "000"


if __name__ == '__main__':
    # What is the server address? IE `python3 miner.py https://server.com/api/`
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    # Load ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    # Run forever until interrupted
    coins = 0
    print("Starting mining")
    while True:
        r = requests.get(url=node + "/last_block")
        # Handle non-json response
        try:
            data = r.json()
            #print("data from get", data)
        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(r)
            break

        # breakpoint()
        # need to always grab the last block to build the chain
        block = data['last_block']
        #old_proof= block['proof']

        # TODO: Get the block from `data` and use it to look for a new proof
        # new_proof = ???
        # block data here
        # When found, POST it to the server {"proof": new_proof, "id": id}

        # use proof_of_work method on incoming data from last_block endpoint
        # new proof is block['last block'] info ran through proof of work algo (which increments proof if valid_proof is true)
        new_proof = proof_of_work(block)
        print(f"Proof found: {new_proof}")

        # post then data in correct format required for post body
        post_data = {"proof": new_proof, "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        try:
            data = r.json()
            print("data", data)

        except ValueError:
            print("Error:  Non-json response")
            print("Response returned:")
            print(r)
            break

        if data['message'] == 'New Block Forged':
            coins += 1
            print(f"1 coin added. New coin total: {coins}")
        # TODO: If the server responds with a 'message' 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
