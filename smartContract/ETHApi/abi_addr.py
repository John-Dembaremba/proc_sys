import json


def get_addr():
  contract_addr = '0x1716A74ad4c23bb5107aFC72cb69F71BD5a63d28'
  return contract_addr

def get_abi():
    json_data = """
      [{
      "inputs": [
        {
          "indexed": true,
          "internalType": "uint256",
          "name": "job_id",
          "type": "uint256"
        },
        {
          "indexed": true,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "zimraITF263",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "praz",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "validity",
          "type": "string"
        }
      ],
      "name": "Bidders",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "indexed": true,
          "internalType": "string",
          "name": "product_type",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "product",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "requirements",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "date",
          "type": "string"
        },
        {
          "indexed": false,
          "internalType": "string",
          "name": "delivery_period",
          "type": "string"
        },
        {
          "indexed": true,
          "internalType": "uint8",
          "name": "job",
          "type": "uint8"
        }
      ],
      "name": "Jobs",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "transaction",
      "outputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "product_type",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "product",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "requirements",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "date",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "delivery_period",
          "type": "string"
        },
        {
          "internalType": "uint8",
          "name": "job",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "_name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_productType",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_product",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_req",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_date",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_del",
          "type": "string"
        },
        {
          "internalType": "uint8",
          "name": "_job",
          "type": "uint8"
        }
      ],
      "name": "addTransaction",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint8",
          "name": "_job",
          "type": "uint8"
        },
        {
          "internalType": "string",
          "name": "_supNm",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_zimraITF263",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_praz",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "_validity",
          "type": "string"
        }
      ],
      "name": "addSuppliers",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_address",
          "type": "address"
        }
      ],
      "name": "getTransactions",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_address",
          "type": "address"
        },
        {
          "internalType": "uint8",
          "name": "_job",
          "type": "uint8"
        }
      ],
      "name": "getSuppliers",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }]
  """
    abi = json.loads(json_data)
    return abi




































