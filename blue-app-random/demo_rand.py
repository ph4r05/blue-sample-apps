#!/usr/bin/env python
#*******************************************************************************
#*   Ledger Blue
#*   (c) 2016 Ledger
#*
#*  Licensed under the Apache License, Version 2.0 (the "License");
#*  you may not use this file except in compliance with the License.
#*  You may obtain a copy of the License at
#*
#*      http://www.apache.org/licenses/LICENSE-2.0
#*
#*  Unless required by applicable law or agreed to in writing, software
#*  distributed under the License is distributed on an "AS IS" BASIS,
#*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#*  See the License for the specific language governing permissions and
#*  limitations under the License.
#********************************************************************************
import sys
import binascii
from ledgerblue.comm import getDongle
from ledgerblue.commException import CommException

dongle = getDongle(True)

# CLS | INS | P1 | P2 | LC
cur = 0
while True:
	try:
		entropy = dongle.exchange(binascii.unhexlify(b'8005000000'))
		sys.stderr.buffer.write(entropy)

	except CommException as comm:
		if comm.sw == 0x6985:
			print("Aborted by user")
		else:
			print("Invalid status " + comm.sw)
