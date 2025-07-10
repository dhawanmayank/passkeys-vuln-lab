# Passkeys Vulnerability Lab

A vulnerable web app built using Flask to demonstrate real-world implementation flaws in passkey authentication systems.

## 🔧 Features & Test Cases

| Route              | Description                                          | Flag                               |
|-------------------|------------------------------------------------------|------------------------------------|
| `/register`       | Passkey registration without attestation check       | `FLAG{attestation_not_verified}`   |
| `/login`          | Login without user presence (no biometric check)     | `FLAG{no_biometric_verification}`  |
| `/fallback`       | MFA downgrade via alternative auth route             | `FLAG{mfa_downgrade_success}`      |
| `/phish`          | Simulated CSRF to steal credentials                  | `FLAG{csrf_token_missing}`         |
| `/remove_key`     | Credential removal attack using spoofed request      | `FLAG{credential_injected}`        |
| `/flags`          | View all discovered flags                            | *(Summary UI)*                     |

---

## 🏁 Getting Started

### Requirements
- Python 3.8+
- Flask

### Installation

```bash
# Clone the repo
$ git clone https://github.com/your-username/passkeys-vuln-lab.git
$ cd passkeys-vuln-lab

# Set up environment
$ pip install -r requirements.txt

# Run the app
$ cd app
$ python main.py
```

Visit `http://localhost:5000` in Chrome.

---

## 🧪 Testing in Chrome
This lab is designed for testing using **Chrome**'s built-in passkey simulator. When registering/login with passkeys, Chrome will prompt you to use:

- Local device authentication
- Virtual authenticator (if enabled via DevTools > More Tools > WebAuthn)

---

## 📁 Folder Structure
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
└── README.md
```

---

## 📜 License
MIT License

---

## 🙌 Credits
Developed by Mayank for **BSides Bangalore 2025**

> "Passkeys are lying to you... until you exploit them right."
