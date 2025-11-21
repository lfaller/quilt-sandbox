# quilt-sandbox

## Setup

### Create Virtual Environment

To set up a Python virtual environment for this project:

```bash
python3 -m venv venv
```

### Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### Deactivate Virtual Environment

When you're done working, deactivate the virtual environment:

```bash
deactivate
```

### Install Dependencies

After activating the virtual environment, install the required packages:

```bash
pip install pandas==2.3.3 pyarrow==20.0.0 quilt3
```

**Note on package versions:** These specific versions are tested and compatible with Python 3.13. The combination of pandas 2.3.3 and pyarrow 20.0.0 avoids known extension type registration issues that occur with newer pyarrow versions.
