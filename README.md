# Doubles (Secure Storage)

**Doubles** (Double-S, 2S or Secure Storage) is a small Python application that allows you to store the recovery codes of multiple services in a file encrypted using a smaller set of recovery codes that can be safely stored easier than saving all the recovery codes from all the services.

It heavily relies on the [aes_cipher](https://github.com/ebellocchia/aes_cipher) package for its encryption/decryption purposes.

**Note:** This is a small hobby project to practice some encryption, so don't expect some enterprise-level encryption (or not yet). Nonetheless, if you want to use it, I'll gladly read you if you have some issue to report on this repository.

## Requirements

- Python 3.8.x
- pip
- Some codes on .txt files where each code is in a different line. i.e.:

```txt
ABCD-EFGH
Q1W2-E3R4
FOOO-BAAR
...
```

## First steps

Run the command to install all dependencies through `pip`:

```shell
pip install -r requirements.txt
```

## Storing steps

1. Put your .txt files into the ``input`` directory and make sure each .txt contains an identifiable name (ideally, only identifiable by you) for the service it belongs to (e.g. ``github.txt``).
2. Execute the encode script using the following command:
```shell
python doubles store [-p <PATH-TO-CODES>] [-n <NUMBER-OF-CODES-TO-GENERATE>]
```
3. Get your encrypted storage file and save it safely and store the passwords printed by the program. You can write those passwords down, print them or whatever you think it's a safe way to store them.

## Get your codes

Whenever you need a sub-set of codes for a service, you can grab them using the following command:

```
python doubles read -p <PASSWORD> -s <SERVICE-NAME> [-n <NUMBER-OF-CODES-TO-GET>]
```

If you don't know what is your service name, you can execute the same script without the service name, and that will return you the services available on the encrypted file:

```
python doubles read -p <PASSWORD>
```

## Contribution

If you want to contribute or expand this project, you can create some pull requests so that I can review them or submit some issues and I'll try to solve them when I can.
