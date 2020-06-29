from setuptools import setup

setup(
    name="passwords",
    version="0.1",
    py_modules=["passwords"],
    install_requires=["Click", "cryptography"],
    entry_points="""
        [console_scripts]
        passwords=scripts:cli
    """,
    python_requires=">=3.4",
)
