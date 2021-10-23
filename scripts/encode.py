import argparse


FILES = {
    'GITHUB': 'github-recovery-codes.txt',
}


def compile():
    encrypter = AESCipher('password')

    decrypted = []
    for key in FILES:
        with open(FILES[key], 'r') as source:
            content = [l.strip() for l in source.readlines()].join(' ').encode('utf-8')
            decrypted.append(base58.b58encode(content))
    print(decrypted)


def main():
    compiled = compile()
    print(compiled)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encode 2FA codes')
    parser.add_argument('-p', '--password', help='Password to use for encryption', required=True)
    args = parser.parse_args()
    password: str = args.password

    main()
