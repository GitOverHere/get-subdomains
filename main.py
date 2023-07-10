import socket

def find_subdomains(domain):
    subdomains = []
    try:
        # Resolve the domain to an IP address
        ip_address = socket.gethostbyname(domain)
        
        # Iterate over a range of possible subdomains
        for i in range(256):
            subdomain = f"{i}.{domain}"
            try:
                socket.gethostbyname(f"{subdomain}")
                subdomains.append(subdomain)
            except socket.error:
                pass
    except socket.error:
        pass

    return subdomains

# Usage example
domain = input("Enter a domain: ")
subdomains = find_subdomains(domain)
print("Subdomains:")
for subdomain in subdomains:
    print(subdomain)

