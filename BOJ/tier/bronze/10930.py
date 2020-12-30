import hashlib
print(hashlib.sha256(str(input()).encode()).hexdigest())