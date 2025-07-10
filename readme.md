# 🧪 Passkeys Vulnerability Lab

A deliberately vulnerable Flask web app to demonstrate real-world **passkey (WebAuthn)** implementation flaws. Built for security researchers, students, and conference demos like **BSides Bangalore 2025**.

---

## 🚩 Vulnerabilities Demonstrated

| Endpoint           | Description                                          | Flag                               |
|-------------------|------------------------------------------------------|------------------------------------|
| `/register`       | Passkey registration without attestation check       | `FLAG{attestation_not_verified}`   |
| `/login`          | Login without user presence/verification              | `FLAG{no_biometric_verification}`  |
| `/fallback`       | MFA fallback attack to bypass passkey enforcement    | `FLAG{mfa_downgrade_success}`      |
| `/phish`          | Simulated CSRF registration without user intent      | `FLAG{csrf_token_missing}`         |
| `/remove_key`     | Credential removal via spoofed injection request     | `FLAG{credential_injected}`        |
| `/flags`          | Displays a summary of all captured flags             | *(UI page)*                        |

---

## ⚙️ Quick Setup (Local)

### 🧰 Requirements
- Python 3.8+
- Git
- Chrome browser (for passkey simulation)

### 🐍 Python Install
```bash
# Clone the repository
$ git clone https://github.com/your-username/passkeys-vuln-lab.git
$ cd passkeys-vuln-lab

# Set up Python environment
$ pip install flask

# Run the app
$ cd app
$ python main.py
```

Open your browser at [http://localhost:5000](http://localhost:5000)

---

## 🐳 Run with Docker

### Option 1: Docker CLI
```bash
docker build -t passkeys-vuln-lab .

# Run the Flask app container
docker run -p 5000:5000 passkeys-vuln-lab

# In another terminal, run the evil server container (using Python image)
docker run -p 1337:1337 -v $(pwd)/evil:/evil python:3.10-slim python -m http.server 1337 -w /evil
```

### Option 2: Docker Compose
```bash
docker-compose up --build
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Testing in Chrome
Enable Chrome’s built-in WebAuthn support for testing passkey flows:

1. Open DevTools → More Tools → **WebAuthn**.
2. Enable **Virtual Authenticator Environment**.
3. Add a platform authenticator (Resident Key, User Verified).

No real hardware passkey needed — Chrome simulates one!

---

## 🗂️ Folder Structure
```
passkeys-vuln-lab/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── register.py
│   │   ├── login.py
│   │   ├── fallback.py
│   │   ├── phish.py
│   │   ├── remove.py
│   │   ├── register_real.py
│   │   └── summary.py
│   └── flags.py
├── templates/
│   ├── flag.html
│   └── flag_summary.html
├── evil/
│   └── index.html
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits
Developed by **Mayank Dhawan** for BSides Bangalore 2025.

> "Passkeys Are Lying to You: Real-World Exploits in WebAuthn Implementations"