import hashlib

hashHandler = hashlib.sha256()
nonce = 0

while True:
    block_header = str(nonce) + "last block hash" + "Merkle root"
    hashHandler.update(block_header.encode("utf-8"))
    hashValue = hashHandler.hexdigest()
    print('nonce:{0}, hash:{1}'.format(nonce, hashValue))
    nounceFound = True
    for i in range(4):
        if hashValue[i] != '0':
            nounceFound = False
    if nounceFound:
        break
    else:
        nonce = nonce + 1