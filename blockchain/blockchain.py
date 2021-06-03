import time
import json
from hashlib import sha256

class Block:

    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        hashed = sha256(block_string.encode()).hexdigest()
        return hashed

class Blockchain:

    difficult = 2

    def __init__(self):
        self.uniconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        hashed_gen_block = genesis_block.compute_hash()

        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):

        block.nonce = 0
        computed_hash = block.compute_hash()

        while not computed_hash.startswith("0" * Blockchain.difficult):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.compute_hash()

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
         check if block_hash is valid hash of block and satifies the difficulty criteria
        """

        return (block_hash.startswith("0" * Blockchain.difficulty) and block_hash == block.compute_hash())
    
    def add_new_transaction(self, transaction):
        self.uniconfirmed_transactions.append(transaction)

    def mine(self):

        if not self.uniconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index = last_block.index + 1,
                          transactions = self.uniconfirmed_transactions,
                          timestamp = time.time(),
                          previous_hash = last_block.compute_hash()
                         )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.uniconfirmed_transactions = []

        return new_block.index




    

