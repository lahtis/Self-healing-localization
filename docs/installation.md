# Installation

The Self‑Healing Localization Layer (SHL) can be installed using pip.  
The package is currently available on TestPyPI for early testing.

---

## Installing from TestPyPI

To install the latest test release:

```bash
pip install -i https://test.pypi.org/simple/ self-healing-localization
```

To install a specific version:
```bash
pip install -i https://test.pypi.org/simple/ self-healing-localization==0.1.1
```

# Installing from PyPI (coming soon)
Once the first stable release is published, installation will be as simple as:
```bash
pip install self-healing-localization
```

Requirements
* Python 3.10 or newer
* No external dependencies
* Works on Windows, Linux, and macOS

Verifying the installation
After installation, you can verify that SHL works by importing the engine:
```bash
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
print("SHL is installed and working.")
```
---

# Upgrading to the latest version
```bash
pip install --upgrade self-healing-localization
```
---

# Uninstalling
```bash
pip uninstall self-healing-localization
```
If you encounter any issues during installation, feel free to open an issue on GitHub

