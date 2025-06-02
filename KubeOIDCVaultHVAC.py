import hvac
import os

# Vault connection details
VAULT_ADDR = os.environ.get('VAULT_ADDR', 'https://vault.example.com')
VAULT_ROLE = os.environ.get('VAULT_ROLE', 'my-role')
JWT_PATH = '/var/run/secrets/kubernetes.io/serviceaccount/token'

# Read the JWT from the service account token file
with open(JWT_PATH, 'r') as f:
    jwt = f.read()

# Initialize the Vault client
client = hvac.Client(url=VAULT_ADDR)

# Authenticate to Vault using the JWT
login_response = client.auth.jwt.jwt_login(role=VAULT_ROLE, jwt=jwt)

# Extract the client token
client_token = login_response['auth']['client_token']

# Set the token for subsequent requests
client.token = client_token

# Example: Read a secret from Vault
secret_path = 'secret/data/myapp/config'
read_response = client.secrets.kv.v2.read_secret_version(path=secret_path)

# Access the secret data
secret_data = read_response['data']['data']
print(f"Retrieved secret: {secret_data}")
