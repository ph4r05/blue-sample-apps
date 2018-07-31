# Sample Signature App for Ledger Blue & Ledger Nano S

This application demonstrates a more complex user interface, the Secure Element
proxy logic, cryptographic APIs and flash storage.

Run `make load` to build and load the application onto the device. After
installing and running the application, you can run `demo.py` to test a
signature over USB.

Note that in order to run `demo.py`, you must install the `secp256k1` Python
package:

```
pip install secp256k1
```

See [Ledger's documentation](http://ledger.readthedocs.io) to get started.

## Ubuntu 18:

```
# BOLOS_ENV - just GCC is needed to setup
# Download GCC to ~/bolos_env/
export GCCPATH=~/bolos_env/gcc-arm-none-eabi-5_3-2016q1/bin

# Download SDK for 1.4.2 https://github.com/LedgerHQ/nanos-secure-sdk/archive/nanos-1421.tar.gz
export BOLOS_SDK=~/bolos_sdk/nanos-secure-sdk-nanos-1421/

sudo apt install libusb-1.0.0-dev libudev-dev
sudo apt install python3 python3-dev python3-pip python3-venv
sudo apt install clang-4.0
sudo apt install gcc-multilib g++-multilib
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-4.0 100
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-4.0 100

# Fill /etc/udev/rules.d/80-ledger.rules:
# SUBSYSTEMS=="usb", ATTRS{idVendor}=="2c97", ATTRS{idProduct}=="0000", MODE="0660", TAG+="uaccess", TAG+="udev-acl" OWNER="<UNIX username>”
# SUBSYSTEMS=="usb", ATTRS{idVendor}=="2c97", ATTRS{idProduct}=="0001", MODE="0660", TAG+="uaccess", TAG+="udev-acl" OWNER="<UNIX username>”

# reconnect USB device, enter PIN

# Setup dev from loader repo
python3 -v venv venv
./venv/pip install ledgerblue
PATH=./venv/bin:$PATH make load
```
