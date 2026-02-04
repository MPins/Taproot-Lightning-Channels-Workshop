# Taproot Lightning Channels from Scratch Workshop

This workshop is designed for developers interested in the details of Taproot transactions required to create and operate [simple taproot channels](https://github.com/lightning/bolts/pull/995). This repo contains a series of python jupyter-notebooks to explain how lightning transactions are created.

The notebooks will start up an instance of bitcoind in regtest mode so that transactions can be validated and broadcasted on regtest.

Participants will build the following transactions from scratch during the session:
- lightning node keys derivation
- channel funding transaction
- initial commitment transaction
- in-flight htlc commitment transaction
- collaborative closing transaction
- htlc-timeout transaction

Each chapter notebook includes a comprehensive summary at the end, covering key concepts, transaction structures, and takeaways.

## Background

Some prior understanding of Schnorr signatures and Taproot is recommended for this workshop.

### Schnorr

- [bip-0340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki): This technical document proposes a standard for 64-byte Schnorr signatures over the elliptic curve secp256k1.
-  [Taproot, and Schnorr, and SIGHASH_NOINPUT, oh my!](https://www.youtube.com/watch?v=YSUVRj8iznU): video about Taproot, Schnorr, and SIGHASH_NOINPUT by Pieter Wuille, author of the Schnorr/Taproot proposal. (Note: since the video SIGHASH_NOINPUT is no longer grouped with the taproot/schnorr soft fork proposal) ([transcript](https://diyhpl.us/wiki/transcripts/sf-bitcoin-meetup/2018-07-09-taproot-schnorr-signatures-and-sighash-noinput-oh-my/))
- [Optech Executive Briefing The Next Softfork](https://www.youtube.com/watch?v=fDJRy6K_3yo): Optech's video presentation of the next proposed soft fork.

### Taproot

- [Taproot Channel Transactions](https://ellemouton.com/posts/taproot-chan-txs/)
- [bip-0341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki): This technical document proposes a new SegWit version 1 output type, with spending rules based on Taproot, Schnorr signatures, and Merkle branches.
- [bip-0342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki): This technical document specifies the semantics of the initial scripting system under bip-0341.
- [Bitcoin Optech’s Overview of the Taproot & Tapscript proposed BIPs](https://bitcoinops.org/en/newsletters/2019/05/14/#overview-of-the-taproot--tapscript-proposed-bips): Summary of bip-341 and bip-342.

### Bolt

This is still a work-in-progress specification, but it’s worth understanding its current state and keeping track of changes.

- [extension-bolt: simple taproot channels (feature 80/81)](https://github.com/lightning/bolts/pull/995)

### Musig2

- [bip-327](https://github.com/bitcoin/bips/blob/master/bip-0327.mediawiki): This document proposes a standard for the [MuSig2](https://eprint.iacr.org/2020/1261.pdf) multi-signature scheme. The standard is compatible with [BIP340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) public keys and signatures. It supports tweaking, which allows deriving [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) child keys from aggregate public keys and creating [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) Taproot outputs with key and script paths. 

## Local Setup

The Taproot Lightning Channels from Scratch Workshop can be setup and run locally. This section lists the necessary steps and requirements.

### Clone this repository

```
$ git clone https://github.com/MPins/Taproot-Lightning-Channels-Workshop
```

### Build Bitcoin Core Locally

Build bitcoind locally. See the build documentation in the Bitcoin Core repository [docs](https://github.com/bitcoin/bitcoin/tree/master/doc#building).

Note that these notebooks will make use of the bitcoind wallet and so when following the build instructions above, do not use the --disable-wallet flag.

No need to run bitcoind or download the mainchain or testnet blockchain. We will run in regtest mode and spawn node instances via scripts.

### Python 3

Verify you have python3 installed:

```
$ python3 --version
```

If not, you should install Python 3.

Linux:

```
$ sudo apt-get install python3
```

MacOS (using [homebrew](https://brew.sh/)):

```
$ brew install python3
```

Windows:

* Install using [binary from python.org](https://www.python.org/downloads/windows/) as appropriate for your system.

### Python Dependencies

This workshop uses some Python dependencies, particularly jupyter-notebook. To keep dependencies local to the project, you should create and activate a virtual environment. You can skip this step if you're happy to install the dependencies globally.

Make sure you are in your Taproot-Lightning-Channels-Workshop repository folder.

The command below creates a Python virtual environment inside the .venv folder. This environment is isolated, meaning that everything you install with pip will be restricted to it and won’t affect the system-wide Python installation.

```
$ python3 -m venv .venv
```

The command below activates the virtual environment you just created.

```
$ source .venv/bin/activate
```

(if you're using the csh or fish shells, replace .venv/bin/activate with .venv/bin/activate.csh or .venv/bin/activate.fish)

Install dependencies:

```
$ python3 -m pip install -r requirements.txt
```

Ensure jupyter notebook is installed:

```
$ jupyter notebook --version
```

Jupyter notebook is a handy tool which allow us to run python code directly in an interactive document like this one. The workshop materials are built directly with jupyter .ipynb files, which you can open once you have jupyter installed.

Start jupyter notebook to see exercises:

```
$ jupyter notebook
```

Jupyter will start a notebook server in your terminal, and provide a link for your browser from which you can interact with notebook files. If your browser doesn't automatically open the notebook file explorer, click on the link provided by jupyter notebook server in the terminal.

## About the Speaker
Pins is a  [Vinteum](https://vinteum.org/)  grantee currently contributing to LND. He began his career as a software developer but later transitioned into commercial and sales roles in cybersecurity within big tech companies. As he progressed in his career, he found himself distanced from hands-on programming. However, his passion for Bitcoin and open-source software reignited his motivation to return to development. Over the past two years, he has focused on relearning programming and began contributing to LND in the past year.

### Social Links
Github https://github.com/MPins
Twitter https://x.com/pins_btc

### Length of workshop: 90 min
