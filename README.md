# Password Hash Script
For hashing password with python

## Prerequisites

* ### Setup environment with uv venv
  ```bash
  cd password_hash
  uv venv
  uv sync
  ```

* ### Setup environment with pip
  ```bash
  cd password_hash
  pip install -r requirements.txt
  ```

## How to use

* ### Options Description
  * -p --password: The password you want to hash
  * -s --strength: The password strength(float: 0.0 ~ 1.0)

* ### Get script help
  ```bash
  python hash_password.py --help
  ```

* ### Execture without options
  ```bash
  python hash_password.py
  ```

* ### Execture with password options
  ```bash
  python hash_password.py -p ${YOU_PASSWORD} -s ${PASSWORD_STRENGTH}
  ```

## Example

* ### Execture with password options via uv
  ```bash
  uv run python hash_password.py -p MySecurePassword123 -s 0.3
  ```

* ### Execture with password options via vanilla python
  ```bash
  python hash_password.py -p MySecurePassword123 -s 0.3
  ```

## References:
* [uv official website](https://docs.astral.sh/uv/)

## License
* MIT
