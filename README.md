# Reverse_CryptoChecker
Attempt on reversing the database of CC by Aleph for both preservation and reuse purposes on Linux.

[![Download](https://img.shields.io/badge/download-success?style=for-the-badge&logo=windows95&logoColor=black)](http://gazlan.narod.ru/pe/cc/cc.rar)  [![Download GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=windows95&logoColor=white)](https://github.com/TAbdiukov/Reverse_CryptoChecker/raw/main/bin/cc.rar)


## What is CC by Aleph ?

CC aka CryptoChecker, produced by Aleph

This is an amazing old tool to detecting (crypto) signatures in files. Unfortunately, its database never became available for the public to reuse or port (to Linux). 

The tool is last updated in 2016 and made with MZ-architecture in mind (.com file format, from MS-DOS/Win9x days), and it is unlikely that the tool is to work in the future systems (let alone on the systems outside the realm of M$)

```
-*-   CC 1.3 alpha 12  *  Copyright (c)  Aleph 2000-2016   -*-

Crypto Checker

Usage: cc.com [!command][{[+]/-}AlgoGroupName] ... [{[+]/-}AlgoGroupName] wildcards

* NOTE: use optional [+/-]AlgoGroup for include/exclude AlgoGroup search
	AlgoGroupName '*' or 'NULL' if used should be first in the method list

Commands are:
	noscript - suppress IDA IDC-script tags generation
	quiet    - naked mode: no header, no footer... stuff only

Examples:
> cc filename.ext  // single file / QUICK mode - recomended
> cc *.*           // some, but entire directory scan
> cc *.DLL         // some, but for specified file type
> cc !noscript filename.ext
> cc * -TINY_PRIMES -SMALL_PRIMES -LOCKBOX filename.ext

complains_n_suggestions direct to alephz@yahoo.com


   DB Timestamp    :  Fri Nov 25 11:10:38 2016
   DB Entries total:  4245

 * Built to find everything
```

## Discovered way to dump off CC database

### Step 1 - generate "busy" file (dummy to keep the tool running)

This is to later keep the CC tool running. The generated file is best to contain nulls (NULL-bytes), so CC doesn't detect. 

It's set to generate a 600 MB file which appears to work well. It makes the program last for about 5-10 minutes, and that's despite the claims of high optimisation of CC

Use `step1_generate_busyfile.py` (The generated file itself is NOT included, as it is easy to regenerate it)

* *Tip*: Best to generate on the modern host system to avoid old Python compatibility issues, and then send over the file to wherever necessary

### Step 2 - initialise a virtualised Windows instance

Any pre-2010 Windows 32-bit should do fine. However, it's been discovered that on Windows NT onwards, the tool allocates too much memory for temporary use - which it doesn't appear to do on Windows 98SE.  

Additionally, newer OSs utilise HyperThreading and multicore optimisations which appear to mess up the binary.

It's recommended that you initialise a virtualised Windows 98SE and install it.

### Step 3 - Drop in software

Once the VM is ready to go, drop in,

* The dummy file generated in step 1  
	*Notice*: Older FAT32 supports up to 4GB, but for some reason takes a REALLY long time to drop in big files (the lack of optimisation?)

* LordPE - for future dumping.  
	*Notice*: You'll need to drop in the update files to use the latest version

* CC - The executable itself.  
	Best to unpack first as it is packed with RAR5

### Step 4 - Dump the unpacked binary

perform,  
```
cc.com busy.bin
```

and wait for some time to ensure that the software unpacked itself. 30 seconds should be more than enough.

Then launch LordPE and select `cc.bin`. Right-click -> Dump full

*Tip*: Pre-dumped copy available in [bin/dump9x.exe](bin/dump9x.exe)

### Step 5 - Generate a listing

**Warning**: Section is incomplete, further work needed

It's been discovered that (apparently) all in-binary strings are encapsulated into 2 NULL-bytes of length 1 or more on both sides.

With this knowledge in mind, a simple getlist tool was created. Use,
```
python step5_getlist.py (target binary)
```

The current output listing is available as *dump9x.exe_list.txt*

### Old versions

* CryptoChecker (CC) 1.1 (beta 8) and CryptoChecker (CC) 1.2 (alpha) – [old](./old/CC_1.1_(beta_8)_and_CC_1.2_(alpha)) / [IA](https://archive.org/details/cc12a_and_cc11b8)  
* CryptoChecker (CC) 1.3 alpha – [old](./old/CC_1.3_alpha) / [IA](https://archive.org/details/cc1.13a)  
* CryptoChecker (CC) 1.3 alpha 9 – [GitHub](https://github.com/nihilus/IDA-CC) / [old](./old/CC_1.3_alpha_9) / [IA](https://archive.org/details/CC1.3A9)  
* CryptoChecker (CC) 1.3 alpha 10 - [old](./old/CC_1.3_alpha_10) / <ins>IA</ins> / [52PoJie](https://www.52pojie.cn/thread-310517-1-1.html)  
* CryptoChecker (CC) 1.3 alpha 11 – [old](./old/CC_1.3_alpha_11) / [IA](https://archive.org/details/cc1.3a11)  

### Further steps?

* Remove rubbish.
* Link the signatures with their descriptions (find patterns?)
* Create an open-source implementation of CC!

---------------------------------

***[Tim Abdiukov](https://github.com/TAbdiukov)***
