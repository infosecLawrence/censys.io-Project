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
and accessing your account details here: (https://censys.io/account/api).

For testing purposes a key and secret are provided within the script but commented out in case of issues with censys account details.

Results from the API queries are output in csv format for further consumption.

## Improvements
Future improvements would include:

- Error handling specific to API responses such as 'incorrect account details', 'API search volume reached' and others.
- Incorporation of active scanning elements based on the data returned from the API by incorporating unix tools such as:
  nmap, harvester etc.
- incorporation of python libraries such as the nmap module to interpret nmap results for example.
- Usage of the shodan.io API in conjunction with the Censys API data to gather further intelligence.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
