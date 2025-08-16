# Taproot Lightning Channels from Scratch Workshop

This workshop is designed for developers interested in the details of Taproot transactions required to create and operate [simple taproot channels](https://github.com/lightning/bolts/pull/995). This repo contains a series of python jupyter-notebooks to explain how lightning transactions are created.

The notebooks will start up an instance of bitcoind in regtest mode so that transactions can be validated and broadcasted on regtest.

Participants will build the following transactions from scratch during the session:
- channel funding transaction
- initial commitment transaction
- pending htlc commitment transaction
- htlc timeout and successful transactions
- collaborative closing transaction
- unilateral closing transaction

## Background

Some prior understanding of Schnorr signatures and Taproot is recommended for this workshop.

### Schnorr

- [bip-0340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki): This technical document proposes a standard for 64-byte Schnorr signatures over the elliptic curve secp256k1.
-  [Taproot, and Schnorr, and SIGHASH_NOINPUT, oh my!](https://www.youtube.com/watch?v=YSUVRj8iznU): video about Taproot, Schnorr, and SIGHASH_NOINPUT by Pieter Wuille, author of the Schnorr/Taproot proposal. (Note: since the video SIGHASH_NOINPUT is no longer grouped with the taproot/schnorr soft fork proposal) ([transcript](https://diyhpl.us/wiki/transcripts/sf-bitcoin-meetup/2018-07-09-taproot-schnorr-signatures-and-sighash-noinput-oh-my/))
- [Optech Executive Briefing The Next Softfork](https://www.youtube.com/watch?v=fDJRy6K_3yo): Optech's video presentation of the next proposed soft fork.

### Taproot

- [bip-0341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki): This technical document proposes a new SegWit version 1 output type, with spending rules based on Taproot, Schnorr signatures, and Merkle branches.
- [bip-0342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki): This technical document specifies the semantics of the initial scripting system under bip-0341.
- [Bitcoin Optech’s Overview of the Taproot & Tapscript proposed BIPs](https://bitcoinops.org/en/newsletters/2019/05/14/#overview-of-the-taproot--tapscript-proposed-bips): Summary of bip-341 and bip-342.

### Bolt

This is still a work-in-progress specification, but it’s worth understanding its current state and keeping track of changes.

- [extension-bolt: simple taproot channels (feature 80/81)](https://github.com/lightning/bolts/pull/995)

## About the Speaker
Pins is a  [Vinteum](https://vinteum.org/)  grantee currently contributing to LND. He began his career as a software developer but later transitioned into commercial and sales roles in cybersecurity within big tech companies. As he progressed in his career, he found himself distanced from hands-on programming. However, his passion for Bitcoin and open-source software reignited his motivation to return to development. Over the past two years, he has focused on relearning programming and began contributing to LND in the past year.

### Social Links
Github https://github.com/MPins
Twitter https://x.com/pins_btc

### Length of workshop: 90 min
