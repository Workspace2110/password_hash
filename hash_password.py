import string
import random
from getpass import getpass
from optparse import OptionParser

from passlib.hash import sha512_crypt
from password_strength import PasswordPolicy


def _get_parameters() -> OptionParser:
    parser = OptionParser()
    parser.add_option("-p",
                      "--password",
                      help="The password you want to hash",
                      default=None,
                      type="string",
                      dest="pwd")
    parser.add_option("-s",
                      "--strength",
                      help="The password strength",
                      default=0.66,
                      type="float",
                      dest="strength")

    return parser


def gen_salt(length: int = 16) -> str:
    character_list = string.ascii_letters
    character_list += string.digits
    salt = []
    for _ in range(length):
        random_char = random.choice(character_list)
        salt.append(random_char)
    
    return "".join(salt)


def main():
    # Load parameters
    parser = _get_parameters()
    (options, args) = parser.parse_args()
    pwd = options.pwd
    strength = options.strength

    # Setup password strength level
    policy = PasswordPolicy.from_names(strength=strength)

    if pwd is None:
        print("Please input password")
        pwd = getpass()
    salt = gen_salt()
    print("Weak Password" if policy.test(pwd) else f"Hashed value: {sha512_crypt.using(salt=salt, rounds=5000).hash(pwd)}")


if __name__ == "__main__":
    main()
