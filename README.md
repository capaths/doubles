# 2FA recovery codes secure storage (2FA-RC2S)

2FA recovery codes storage (or 2FA-RC2S) is a simple Python application that allows you to store the recovery codes of multiple services in a file encrypted using a smaller set of recovery codes that can be safely stored easier than saving all the recovery codes from all the services.

It heavily relies on the [aes_cipher](https://github.com/ebellocchia/aes_cipher) package for its encryption/decryption purposes.

## Requirements

- Python 3.8.x
- pip
- Some 2FA codes .txt files where each code is in a different line. i.e.:

```txt
ABCD-EFGH
Q1W2-E3R4
FOOO-BAAR
...
```

## Storing steps

1. Put your 2FA .txt files into the ``input`` directory and make sure each .txt contains an identifiable name (ideally, only identifiable by you) for the service it belongs to.
2. Execute the encode script using the following command:
```shell
python ./src/scripts/store.py [-n NUMBER-OF-CODES-TO-GENERATE]
```
3. Get your encrypted storage file and save it safely and store the passwords printed by the program. You can write those passwords down, print them or whatever you think it's a safe way to store them.

## Get your recovery codes

Whenever you need a sub-set of recovery codes for a service, you can grab them using the following command:

```
python ./src/scripts/read.py -p <PASSWORD> -s <SERVICE-NAME> [-n <NUMBER-OF-CODES-TO-GET>]
```

If you don't know what is your service name, you can execute the same script without the service name, and that will return you the services available on the encrypted file:

```
python ./scripts/read.py -p <PASSWORD>
```
