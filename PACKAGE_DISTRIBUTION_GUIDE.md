# Rosetta-Field Package Distribution Guide

## 📦 **Package Distribution Process**

This guide explains how to distribute your Rosetta-Field package and use it locally during development.

## 🏠 **Local Development Usage**

### **Option 1: Editable Install (Recommended for Development)**

```bash
# From your project root directory
pip install -e .

# Or with all optional dependencies
pip install -e ".[all,dev]"
```

**Benefits:**
- Changes to source code are immediately available
- No need to reinstall after code changes
- Perfect for development and testing

**What happens:**
- Creates a link to your source code
- Installs dependencies from `pyproject.toml`
- Package becomes importable from anywhere

### **Option 2: Development Mode with pip**

```bash
# Install in development mode with dev tools
pip install -e ".[dev]"

# This installs:
# - Your package (editable)
# - Development dependencies (pytest, black, flake8, mypy)
```

### **Option 3: Using PYTHONPATH (Alternative)**

```bash
# Add your project root to Python path
export PYTHONPATH="/path/to/your/rosetta-field:$PYTHONPATH"

# Or temporarily
PYTHONPATH="/path/to/your/rosetta-field" python your_script.py
```

## 🧪 **Testing Your Local Installation**

### **Test Import from Anywhere**

```bash
# Test that package is available globally
python -c "from rosetta_field import RosettaAPI; print('✅ Success!')"

# Test from different directory
cd /some/other/directory
python -c "from rosetta_field import RosettaAPI; print('✅ Success!')"
```

### **Run Example Script**

```bash
# From project root
python example_usage.py

# From anywhere (after editable install)
python /path/to/rosetta-field/example_usage.py
```

### **Test in Python REPL**

```python
# Start Python REPL
python

# Test imports
>>> from rosetta_field import RosettaAPI, RosettaConfig
>>> from rosetta_field.core import SessionType
>>> api = RosettaAPI()
>>> print("✅ All imports working!")
```

## 🔨 **Building Distribution Packages**

### **Install Build Tools**

```bash
pip install build twine
```

### **Build Packages**

```bash
# Build both source and wheel distributions
python -m build

# This creates:
# - dist/rosetta_field-0.1.0.tar.gz (source distribution)
# - dist/rosetta_field-0.1.0-py3-none-any.whl (wheel distribution)
```

### **What Gets Built**

The build process:
1. **Source Distribution** (`.tar.gz`): Contains source code and metadata
2. **Wheel Distribution** (`.whl`): Pre-built package for specific Python versions
3. **Metadata**: Package information, dependencies, and classifiers

### **Build Output**

```
dist/
├── rosetta_field-0.1.0.tar.gz          # Source distribution
└── rosetta_field-0.1.0-py3-none-any.whl  # Wheel distribution
```

## 📤 **Publishing to PyPI**

### **1. Test PyPI (Recommended First)**

```bash
# Upload to Test PyPI first
twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ rosetta-field
```

### **2. Real PyPI**

```bash
# Upload to real PyPI
twine upload dist/*

# Install from PyPI
pip install rosetta-field
```

### **PyPI Account Setup**

1. **Create Account**: Visit [pypi.org](https://pypi.org) and [test.pypi.org](https://test.pypi.org)
2. **Enable 2FA**: Required for security
3. **API Tokens**: Generate tokens for automated uploads
4. **Configure twine**: Set up credentials

```bash
# Configure twine (stores credentials securely)
twine configure

# Or use environment variables
export TWINE_USERNAME=your_username
export TWINE_PASSWORD=your_api_token
```

## 🔄 **Development Workflow**

### **Daily Development Cycle**

```bash
# 1. Make code changes
# 2. Test locally (editable install)
python example_usage.py

# 3. When ready for release:
#    - Update version in pyproject.toml
#    - Commit changes
#    - Build packages
python -m build

# 4. Test packages locally
pip install dist/rosetta_field-0.1.0-py3-none-any.whl

# 5. Upload to PyPI
twine upload dist/*
```

### **Version Management**

```toml
# In pyproject.toml
[project]
version = "0.1.0"  # Update this for each release
```

**Versioning Strategy:**
- `0.1.0` - Initial release
- `0.1.1` - Bug fixes
- `0.2.0` - New features
- `1.0.0` - Stable API

## 🧹 **Cleaning Up**

### **Remove Editable Installation**

```bash
# Remove the editable installation
pip uninstall rosetta-field

# Clean build artifacts
rm -rf build/ dist/ *.egg-info/
```

### **Clean Build Directories**

```bash
# Remove build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/
rm -rf __pycache__/
```

## 📋 **Distribution Checklist**

### **Before Building**

- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md` (if you have one)
- [ ] Test with editable install: `pip install -e .`
- [ ] Run tests: `pytest`
- [ ] Check code quality: `black .`, `flake8 .`, `mypy .`

### **Before Publishing**

- [ ] Build packages: `python -m build`
- [ ] Test wheel installation: `pip install dist/*.whl`
- [ ] Test source installation: `pip install dist/*.tar.gz`
- [ ] Verify package contents
- [ ] Check metadata and dependencies

### **After Publishing**

- [ ] Test installation from PyPI: `pip install rosetta-field`
- [ ] Verify all functionality works
- [ ] Update documentation if needed
- [ ] Announce release to community

## 🚀 **Advanced Distribution Features**

### **Multiple Python Versions**

```bash
# Build for multiple Python versions
python -m build --wheel

# Or use tox for multi-version testing
pip install tox
tox --build
```

### **Platform-Specific Wheels**

```bash
# Build platform-specific wheels
python -m build --wheel

# This creates wheels optimized for your platform
```

### **Source Distribution Only**

```bash
# Build only source distribution
python -m build --sdist
```

## 🔍 **Troubleshooting**

### **Common Issues**

1. **Import Errors After Installation**
   ```bash
   # Check if package is installed
   pip list | grep rosetta-field
   
   # Reinstall in editable mode
   pip uninstall rosetta-field
   pip install -e .
   ```

2. **Build Failures**
   ```bash
   # Clean and rebuild
   rm -rf build/ dist/ *.egg-info/
   python -m build
   ```

3. **Upload Failures**
   ```bash
   # Check credentials
   twine check dist/*
   
   # Test with Test PyPI first
   twine upload --repository testpypi dist/*
   ```

### **Debugging Tips**

- Use `pip show rosetta-field` to see installation details
- Check `pip list` for installed packages
- Use `python -c "import rosetta_field; print(rosetta_field.__file__)"` to see where package is loaded from
- Check build logs for detailed error information

## 📚 **Resources**

- **Official Python Packaging Guide**: [packaging.python.org](https://packaging.python.org/)
- **PyPI**: [pypi.org](https://pypi.org)
- **Test PyPI**: [test.pypi.org](https://test.pypi.org)
- **Build Tool**: [pypa-build.readthedocs.io](https://pypa-build.readthedocs.io/)
- **Twine**: [twine.readthedocs.io](https://twine.readthedocs.io/)

## 🎯 **Quick Start Commands**

```bash
# Development setup
pip install -e ".[dev]"
python example_usage.py

# Build for distribution
python -m build

# Test packages locally
pip install dist/rosetta_field-0.1.0-py3-none-any.whl

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

---

This guide covers the complete process from local development to PyPI distribution. Start with editable installation for development, then use the build and upload process when you're ready to share your package with the world!
