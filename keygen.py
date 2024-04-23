import secrets, string, sys

FLAGS = ('-r', '--refresh')
HELP = (
    """
    Usage:
      python keygen.py           : Generate & print secret key (Not assigned to project)
      python keygen.py -r        : Generate & reset to new secret-key (Assign to project & not printed)
      python keygen.py --refresh : Generate & reset to new secret-key(Assigned to project & not printed)
    """
).strip()


def main():
    args = sys.argv[1:]
    flag = args[0]

    if len(args) > 1:
        print(HELP)
        sys.exit()
    
    if flag.strip().lower() not in FLAGS:
        print(HELP)
        sys.exit()

    secret = generate_secret()
    print(secret)
    



def generate_secret(length=50):
    """Generate secret key for django project"""
    characters = string.ascii_letters + string.digits + string.punctuation
    secret = ''.join(secrets.choice(characters) for _ in range(length))
    return secret

if __name__ == '__main__':
    main()