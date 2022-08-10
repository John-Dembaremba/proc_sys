from web3 import Web3, contract
import json
import abi_addr

ganache_url = 'http://127.0.0.1:7545'
#web3 = Web3(Web3.HTTPProvider(ganache_url))
#print(web3.isConnected())
#print(web3.eth.accounts)


class WebAPI(object):

    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(ganache_url))
        self.Accounts = self.web3.eth.accounts

    def checkConnection(self):
        return self.web3.isConnected()
    
    def contract_interact(self):
        contract = self.web3.eth.contract(address=abi_addr.get_addr(), abi=abi_addr.get_abi())
        return contract

    def post_jobs(self, user, name, product_type, product, requiments, date, delivery_period, job_id):
        self.web3.eth.defaultAccount = user

        contract = self.contract_interact()

        txt_hash = contract.functions.addTransaction(
            name, 
            product_type, 
            product, 
            requiments,
            date, 
            delivery_period, 
            job_id,
        ).transact()
        
        txt_receipt = self.web3.eth.wait_for_transaction_receipt(txt_hash)

        txt_logs = contract.events.Jobs().processReceipt(txt_receipt)
        print(type(txt_logs[0]['args']))

        return txt_logs[0]['args']

    def apply_jobs(self, user, job_id, name, zimra, praz, doc_validity):
        self.web3.eth.defaultAccount = user

        contract = self.contract_interact()

        txt_hash = contract.functions.addTransaction(
            job_id, 
            name, 
            zimra, 
            praz, 
            doc_validity,

        ).transact()
        
        txt_receipt = self.web3.eth.wait_for_transaction_receipt(txt_hash)
        
        txt_logs = contract.events.Bidders().processReceipt(txt_receipt)
        

        return txt_logs[0]['args']


    def get_transactions_logs(self, receipt):
        pass

      
