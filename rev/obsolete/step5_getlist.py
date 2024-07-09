#!/usr/bin/env python
# -*- coding: utf8 -*-

import re # for regex matching
import sys #for args

def main(filename):
	pattern = rb"\0([\x20-\x7F]{3,}?)\0"

	print("Stage 1 - reading")
	fp = open(filename, "rb")
	full_raw = fp.read()
	fp.close()

	print("Stage 2 - Generate new string")
	new_raw = full_raw.replace(b'\x00', b'\x00\x00')

	print("Stage 3 - matching & saving")
	fp2 = open(filename+"_list.txt", "w+")

	for m in re.finditer(pattern, new_raw):
		buf = m.group(1).decode("ASCII")
		fp2.write("* {0:08X}\t{1:d}\t{2:s}\n".format(m.start(), len(buf), buf))

	fp2.close()

	print("Completed")

if __name__ == '__main__':
	try:
		arg = sys.argv[1].lower()
		main(arg)
	except:
		print("Step 5 data retriever for Reverse CryptoChecker project")
		print(sys.argv[0]+" (filename)")

