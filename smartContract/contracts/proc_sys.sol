pragma solidity >=0.7.0 <0.9.0;



contract procurement {
    
    struct Supplier_details {
        string name;
        string zimraITF263;
        string praz;
        string validity;
    }
    
    
    struct Client {
        string name;
        string product_type;
        string product;
        string requirements;
        string date;
        string delivery_period;
        uint8 job;
        mapping(uint8 => Supplier_details) suppliers;
    }
    
    mapping(address => Client) public transaction;
    
    event Jobs (
        string indexed name,
        string indexed product_type,
        string product,
        string requirements,
        string date,
        string delivery_period,
        uint8 indexed job
    );
    
    event Bidders (
        uint256 indexed job_id,
        string indexed name,
        string zimraITF263,
        string praz,
        string validity
    );

    function addTransaction(string memory _name, string memory _productType, string memory _product, string memory _req, string memory _date, string memory _del, uint8 _job) public {
       
        Client storage client = transaction[msg.sender];
        client.name = _name;
        client.product_type = _productType;
        client.product = _product;
        client.requirements = _req;
        client.date = _date;                
        client.delivery_period = _del;
        client.job = _job;

        emit Jobs(
            _name,
            _productType,
            _product,
            _req,
            _date,
            _del,
            _job
        );
    }
    
    function addSuppliers(uint8 _job,string memory _supNm, string memory _zimraITF263, string memory _praz, string memory _validity) public {
        Client storage client = transaction[msg.sender];
        client.suppliers[_job] = Supplier_details({name: _supNm, zimraITF263: _zimraITF263, praz: _praz, validity: _validity});
        
        emit Bidders(
            _job,
            _supNm,
            _zimraITF263,
            _praz,
            _validity
            
        );
    }
    
    function getTransactions(address _address) view public returns(string memory, string memory, string memory, string memory, string memory, string memory,uint8) {
        Client storage client = transaction[_address];
        return (client.name, client.product_type, client.product, client.requirements, client.date, client.delivery_period, client.job);
    }
    
    function getSuppliers(address _address, uint8 _job) view public returns(string memory, string memory, string memory, string memory) {
        Client storage client = transaction[_address];
        
        return (client.suppliers[_job].name, client.suppliers[_job].zimraITF263, client.suppliers[_job].praz, client.suppliers[_job].validity);
    }
    
    
    
    
    
}
