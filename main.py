import sys
import os
import time
import censys.certificates
from censys.ipv4 import CensysIPv4
import censys
import csv


# Function finds subdomain related to domain
def subdomain_search(domain, api_id, api_secret, subdomain_fields):
    subdomain = censys.certificates.CensysCertificates(api_id, api_secret)
    results = subdomain.search(domain, fields=subdomain_fields)
    subdomain_list = list(results)

    res_list = []
    for i in range(len(subdomain_list)):  # Remove duplicate domains and append in new list
        if subdomain_list[i] not in subdomain_list[i + 1:]:
            res_list.append(subdomain_list[i])

    with open(domain + '.domains.csv', 'w', newline='') as f:  # Write results pulled via API to CSV file
        writer = csv.DictWriter(f, subdomain_fields)
        writer.writerows(res_list)
    print('[+] Results written to csv file: ' + domain + '.domains.csv')


# Function finds ipv4 information related to domain
def ipv4_search(domain, api_id, api_secret, ipv4_fields):
    ipv4 = CensysIPv4(api_id, api_secret)
    results = ipv4.search(domain, fields=ipv4_fields)
    ipv4_list = list(results)

    res_list = []
    for i in range(len(ipv4_list)):  # Remove duplicate domains and append in new list
        if ipv4_list[i] not in ipv4_list[i + 1:]:
            res_list.append(ipv4_list[i])

    with open(domain + '.ipv4.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, ipv4_fields)
        writer.writerows(res_list)
    print('[+] Results written to csv file: ' + domain + '.ipv4.csv')


# Function initialises values for searches and runs the search functions
def main(domain, api_id, api_secret):
    subdomain_fields = ['parsed.names']
    ipv4_fields = [
        "ip",
        "location.city",
        "location.country",
        "location.country_code",
        "location.postal_code",
        "autonomous_system.name",
        "autonomous_system.organization"
    ]
    print("[+] Finding subdomains of %s " % domain)
    subdomain_search(domain, api_id, api_secret, subdomain_fields)

    print("[+] Finding related ipv4 of %s " % domain)
    ipv4_search(domain, api_id, api_secret, ipv4_fields)


if __name__ == "__main__":
    api_id = input("Enter Censys API id: ")
    api_secret = input("Enter Censys secret: ")

    # api_id = 'a5d9d1dd-c9f7-4217-a342-f4f94c1993d2'
    # api_secret = 'BByXL2VEnCTulDoZyToNwrK3Nla0zo77'

    valid_domain = ['.com', '.net', '.org', '.co.uk']
    domain_input = input("Enter the domain: ")
    domain = domain_input.split()
    print("Checking %s is valid " % domain)

    for domain in domain:  # For domain present after user input,
        if domain.endswith(tuple(valid_domain)):  # check domain is valid before attempting to
            print("[+] %s is valid " % domain)  # query censys api
            main(domain, api_id, api_secret)
        else:
            print('[-] Invalid domain ')
            print('[-] exiting ....')
            exit(1)
