# censys.io Project
 This project contains a script to query the censys.io API, returning domain and ipv4 information for a given domain.

## Installation
 The program requires the open source Censys Python library.

 Use the package manager [pip]((https://pip.pypa.io/en/stable/) to install the library using the following:

 ```bash
pip install censys
```

More information on the censys library can be found at: (https://github.com/censys/censys-python/blob/master/README.md)

## Usage
The program is run using the following command:

```bash
python main.py
```
You will then be prompted to enter a valid censys 'api id' and 'api secret' which can be obtained by creating a free account at: (https://censys.io/register)
and accessing your account details here: (https://censys.io/account/api)

Results from the API queries are ouput in csv format for further consuption.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
