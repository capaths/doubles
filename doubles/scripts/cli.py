import os
import glob
import click

from doubles import Storage, StoragePassword
from typing import Dict, List, Optional, Union


__all__ = ['cli']

def compile(path: str = './codes') -> Storage:
    """
    Compile the storage.
    """
    codes: Dict[str, ] = {}
    for filepath in glob.glob(os.path.join(path, '*.txt')):
        filename, _ = os.path.splitext(os.path.basename(filepath))
        with open(filepath, 'r') as f:
            codes[filename] = [l.strip() for l in f.readlines()]
    click.echo(f"Found services: {', '.join(list(codes.keys()))}")
    return Storage(codes)

@click.command()
@click.option('--output', '-o', default='./2fa-rc2s.store', help='Output file')
@click.option('--path', '-p', default='./codes', help='Path to the storage directory.')
@click.option('--n_passwords', '-n', default=2, help='Number of passwords to generate.')
def store(path: str, n_passwords: int, output: str):
    """
    Store the recovery codes.
    """

    storage = compile(path)

    passwords = [StoragePassword.generate(idx) for idx in range(n_passwords)]
    encoded_passwords = [p.encoded for p in passwords]
    click.echo("While your codes are being encrypted. Store your master passwords:\n")
    click.echo('\n'.join(encoded_passwords))
    click.echo("\nStore them safely. Maybe each one in different places.")

    with open(output, 'wb') as f:
        f.write(storage.encrypt(encoded_passwords))
    click.echo(f"The store can be found at {output}")

@click.command()
@click.option('--path', '-p', default='./2fa-rc2s.store', type=str, help='Path to the storage file.')
@click.option('--service', '-s', default=None, type=str, help='Service which to retrieve the codes from.')
@click.option('--n_codes', '-n', default=42, type=int, help='Number of codes to retrieve.')
@click.option('--passwords', '-P', required=True, type=str, help='The passwords to use for deccryption separated by commas (,).')
def read(path: str, passwords: str, service: Optional[str], n_codes: str):
    """
    Read the recovery codes.

    The store must be encrypted with the given passwords.

    :param path: Path to the storage file.
    :param passwords: The passwords to use for deccryption separated by commas (,).
    """
    passwords: List[StoragePassword] = sorted([
        StoragePassword.from_encoded(p) for p in passwords.split(',')
    ], key=lambda p: p.index)
    encoded_passwords = [p.encoded for p in passwords]

    with open(path, 'rb') as f:
        click.echo(f"Decrypting store with {len(passwords)} passwords...")
        storage = Storage.decrypt(f.read(), encoded_passwords)
    if service is None:
        # Print available services
        click.echo(f"Available services: {', '.join(storage.services)}")
        return
    codes = storage.get_random_codes(service, n_codes)
    click.echo(f"Found {len(codes)} codes:")
    click.echo('\n'.join(codes))

@click.group()
def cli():
    pass

cli.add_command(store)
cli.add_command(read)
