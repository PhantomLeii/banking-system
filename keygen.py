import secrets, string, sys, os 

def main():
    dot_env_path = os.path.join('config', '.env')

    write_secret(dot_env_path, generate_secret(50))

    print('.env created successfully!')
    print('SECRET propulated successfully')
    
    return None

def generate_secret(length=50):
    """Generate secret key for django project"""
    characters = string.ascii_letters + string.digits + string.punctuation
    secret = ''.join(secrets.choice(characters) for _ in range(length))
    return secret

def write_secret(path, secret):
    """Write secret to the file specified in path"""
    with open(path, 'w') as env:
        env.write(f'SECRET="{secret}"')

if __name__ == '__main__':
    main()