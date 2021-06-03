from system.models import Apply
from django.core import serializers
import json



class SerializerClass:
    
   
    def __init__(self):
        #global suppliers
        self.dic_suppliers_list = dict()
        self.dic_suppliers = []
        self.dic_clients = []
        self.clients = []
        self.suppliers_list = []
        self.transactions = []

    def get_serializer_data(self):
        data = serializers.serialize("json", Apply.objects.all(), fields=('jobs', 'applied', 'zimra_date', 'praz_date', 'doc_validity', 'suppliers'), use_natural_foreign_keys=True, use_natural_primary_keys=True)
        json_data = json.loads(data)
        print(self.transactions)
        return json_data

    def create_dic(self, serialized_data):
        for item in range(0, len(serialized_data)):
            key = serialized_data[item]['fields']['jobs']['Product Id']
            suppliers_dictionary = {
                                f"{key}".format(key): [{"name": serialized_data[item]['fields']['suppliers'],
                                                    "zimra_date": serialized_data[item]['fields']['zimra_date'],
                                                    "praz_date": serialized_data[item]['fields']['praz_date'],
                                                    "Documents": serialized_data[item]['fields']['doc_validity'],

                                                    }
                                                ],
                                
                                }
            self.dic_suppliers.append(suppliers_dictionary)

            client_dictionary = {
                            key: [{"name": serialized_data[item]['fields']['jobs']['Client'],
                            "Product Type": serialized_data[item]['fields']['jobs']['Group product'],
                            "Product": serialized_data[item]['fields']['jobs']['Product name'],
                            "Requirements": serialized_data[item]['fields']['jobs']['Requirements'],
                            "Created date": serialized_data[item]['fields']['jobs']['Created data'],
                            "Delivery period": serialized_data[item]['fields']['jobs']['Delivery period'],
                            }]                        
                            }
            self.dic_clients.append(client_dictionary)

        #print(self.dic_clients)

    def cleaned_client_list(self):
        """
        method removes duplicate keys in clients[] using naive()
        """
        clients_list = self.dic_clients

        for client in range(len(clients_list)):
            if clients_list[client] not in clients_list[client + 1: ]:
                self.clients.append(clients_list[client])
        #print(self.clients)

    def cleaned_supplier_list(self):
        
        """
        merge duplicate keys of all suppliers with the same key and add to supplier[]
        """
        for dict in self.dic_suppliers:
            for list in dict:
                if list in self.dic_suppliers_list:
                    self.dic_suppliers_list[list] += (dict[list])
                else:
                    self.dic_suppliers_list[list] = dict[list]
        
        for item in self.dic_suppliers_list.items():
            self.suppliers_list.append(item)
        

    def dic_transactions(self):
        """
        checks key for suppliers_list[] and clients[] and merge if are equal
        """
        for client in range(len(self.clients)):
            for supplier in range(len(self.suppliers_list)):
                if [*self.clients[client]][0] == int(self.suppliers_list[supplier][0]): # grab key from client{} and compare with supplie()
                    self.clients[client]["suppliers"] = self.suppliers_list[supplier][1] # add key 'supplier' with values of suppliers
                    self.transactions.append(self.clients[client])
    