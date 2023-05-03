from crypt import crypt
from crypt import mksalt
from crypt import METHOD_SHA512
from getpass import getpass

from optparse import OptionParser

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

    print("Weak Password" if policy.test(pwd) else f"Hashed value: {crypt(pwd, mksalt(METHOD_SHA512))}")


if __name__ == "__main__":
    main()
