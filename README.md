# Reverse_CryptoChecker
Attempt on reversing the database of CC by Aleph for both preservation and reuse purposes on Linux

## What is CC by Aleph ?

CC aka CryptoChecker, produced by Aleph

This is an amazing old tool to detecting (crypto) signatures in files. Unfortunately its database never became available for the public to reuse or port (to Linux). 

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
