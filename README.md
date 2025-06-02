
# 🔐 Kubernetes OIDC Vault Authentication (Python)

This repository demonstrates how a Python application running inside a Kubernetes or OpenShift 4.x cluster can authenticate to **HashiCorp Vault** using a Kubernetes-issued **OIDC JWT token**, and retrieve secrets securely with no hardcoded credentials.

---

## 📦 What This Project Does

- Reads the OIDC service account token from the pod (`/var/run/secrets/kubernetes.io/serviceaccount/token`)
- Authenticates with Vault using the JWT/OIDC method
- Fetches secrets securely from a specified Vault path
- Designed to work seamlessly in zero-trust environments using service accounts

---

## 📁 Project Structure

```

KubernetesOIDCVaultPython/
├── main.py               # Python script that authenticates and fetches secret
├── requirements.txt      # Python dependencies
├── vault-role-example.hcl  # Example Vault role & policy (for reference)
└── README.md             # You're here!

````

---

## 🛠️ Requirements

- Python 3.8+
- HashiCorp Vault (v1.9+)
- Kubernetes or OpenShift 4.x
- Vault configured for JWT authentication
- Service account with projected token
- Secret already stored in Vault

---

## 🔐 Vault Configuration

### Enable JWT auth method:

```bash
vault auth enable jwt
````

### Configure Vault to accept Kubernetes-issued OIDC tokens:

```bash
vault write auth/jwt/config \
  oidc_discovery_url="https://kubernetes.default.svc" \
  bound_issuer="https://kubernetes.default.svc"
```

### Create a Vault role:

```bash
vault write auth/jwt/role/my-role \
  role_type="jwt" \
  bound_audiences="https://kubernetes.default.svc" \
  bound_subject="system:serviceaccount:default:my-service-account" \
  user_claim="sub" \
  policies="default"
```

---

## 💾 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

Make sure your pod is running with a service account and projected token.

Then run:

```bash
export VAULT_ADDR=https://vault.default.svc:8200
export VAULT_ROLE=my-role
export VAULT_PATH=secret/data/myapp/config
python main.py
```

---

## 🔑 Environment Variables

| Variable     | Description                                            |
| ------------ | ------------------------------------------------------ |
| `VAULT_ADDR` | Vault endpoint (e.g. `https://vault.default.svc:8200`) |
| `VAULT_ROLE` | Vault role to authenticate with                        |
| `VAULT_PATH` | Full path of secret to retrieve (KV v2 format)         |

---

## 📦 Example Output

```bash
🔐 Successfully authenticated with Vault.
✅ Retrieved secret: {'username': 'admin', 'password': 's3cr3t'}
```

---

## 📚 References

* [Vault JWT Auth Method](https://developer.hashicorp.com/vault/docs/auth/jwt)
* [Python HVAC (Vault Client)](https://github.com/hvac/hvac)
* [Kubernetes Projected Service Account Tokens](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#token-projection)

---

## 🧠 Author

Maintained by [@mpwusr](https://github.com/mpwusr)
Contributions welcome! Please open an issue or submit a PR.

```

---

Would you like me to also provide:
- A `Dockerfile` for containerizing this app?
- A Kubernetes `Deployment.yaml` that includes projected token setup?
```
