# CryptoChecker_Research
Researching CryptoChecker data by Aleph 🇮🇱.

[![Download](https://img.shields.io/badge/download-success?style=for-the-badge&logo=windows95&logoColor=black)](http://gazlan.narod.ru/pe/cc/cc.rar)  [![Download GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=windows95&logoColor=white)](https://github.com/TAbdiukov/CryptoChecker_Research/raw/main/bin/cc.rar)

## Browse

* [./bin (Binaries)](./bin)
* [./rev (Reversing)](./rev)
* [./txt (Strings)](./txt)

## Binary

* CryptoChecker (CC) 1.3 alpha 12 - [bin](./bin/CC_1.3_alpha_12)
* CryptoChecker (CC) 1.3 alpha 11 (Oct 14, 2015) – [bin](./bin/CC_1.3_alpha_11_20151410) / [IA](https://archive.org/details/cc1.3a11)  
* CryptoChecker (CC) 1.3 alpha 11 (Mar 31, 2015) – [bin](./bin/CC_1.3_alpha_11_20150331) / [IA](https://archive.org/details/cryptochecker-1.3-alpha-11-mar-31-2015)  
* CryptoChecker (CC) 1.3 alpha 10 – [bin](./bin/CC_1.3_alpha_10) / [IA](https://archive.org/details/cc13a10) / [52PoJie](https://www.52pojie.cn/thread-310517-1-1.html)  
* CryptoChecker (CC) 1.3 alpha 9 – [bin](./bin/CC_1.3_alpha_9) / [IA](https://archive.org/details/CC1.3A9) / [GitHub](https://github.com/nihilus/IDA-CC)  
* CryptoChecker (CC) 1.3 alpha – [bin](./bin/CC_1.3_alpha) / [IA](https://archive.org/details/cc1.13a)  
* CryptoChecker (CC) 1.1 (beta 8) and CryptoChecker (CC) 1.2 (alpha) – [bin](./bin/CC_1.1_(beta_8)_and_CC_1.2_(alpha)) / [IA](https://archive.org/details/cc12a_and_cc11b8)

## What is CC by Aleph?

CC aka CryptoChecker by Aleph

This is an amazing old tool for detecting (crypto) signatures in files. Unfortunately, no source code is available.

The tool is last updated in 2016 and made with MZ-architecture in mind (.com file format, from MS-DOS/Win9x days), and given how capable the utility is, it would be great to be able to use this utility in the future.

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

## Guide: extract CC strings

### Step 1 - Generate a "busy" file (dummy to keep the tool running)

This is to later keep the CC tool running. The generated file is best to contain nulls (NULL-bytes), so CC minimally loads detection information. 

A generated 600 MB file makes the program run for about 5-10 minutes.

Use `step1_generate_busyfile.py` (The generated file itself is NOT included, as it is easy to regenerate it)

* *Tip*: To keep it simple, it is best to generate a 'busy' file on the modern host system.

### Step 2 - Create a virtualized Windows instance

For some reason, `cc.com` operates most optimally in Win9x environment. There, the utility uses least RAM. Hence, a (virtualized) Win9x environment is needed.

### Step 3 - Transfer files

Once the VM is ready to go, transfer,

* The dummy file generated in step 1  
	*Note*: Older FAT32 supports up to 4GB, but it takes a long time to transfer big files

* LordPE - for future dumping.  
	*Note*: The update files are also needed to use the latest version

* CC - The executable itself.  
	Best to unpack first as it is packed with RAR5

### Step 4 - Dump the unpacked binary

execute,  
```
cc.com busy.bin
```

and wait for some time to ensure that the software unpacks itself. 30 seconds should be more than enough.

Then launch LordPE and select `cc.bin`. Right-click → Dump full

* Pre-dumped copy available in [rev/dump9x.exe](rev/dump9x.exe)

### Step 5 - Generate a listing

Use [strings2](https://github.com/glmcdona/strings2) or other tools to extract strings.

Extracted strings are available in [./txt/](./txt)

---------------------------------

***[Tim Abdiukov](https://github.com/TAbdiukov)***
