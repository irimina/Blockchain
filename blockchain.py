# Task: Instantiate the blockchain object, create three transactions, add them to the chain and display the chain after each one. 


import hashlib
import json
from time import time

#Blockhain Class
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(previous_hash="The Times 03/Jan/2009/Chancellor on brink of second bailout for banks", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
             # true hash of the genesis block: 
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

#Search the blockchain for the most recent block.
    @property
    def last_block(self):
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash
 
# this line is outside the class to generate a proof ID
proofID= random.randrange(100, 100000)

#. Add your code below here #

# STEP 1 instantiate the blockchain object

# STEP 2 print the empty chain

# STEP 3 initiate the first transation by calling the new_transaction() on the object with the arguments of your choice

# STEP 4 add the new block to the chain using the new_block() by passing the proofID numberbk_

# STEP 5 print the entire chain 

# Repeat the steps 3-5 twice to add two more transactions

# NOTE: you can add some print() statements among transactions for easier reading









