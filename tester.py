import sys
import whois

res = whois.query(sys.argv[1])
print(res.__dict__)
