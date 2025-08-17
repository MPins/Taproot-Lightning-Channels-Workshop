from bip_utils import Bip32Slip10Secp256k1, Bip39SeedGenerator, Bip39MnemonicGenerator, Bip86, Bip86Coins, Bip44Changes

def generate_taproot_ctx():
    # Generate a 24-word mnemonic
    mnemo = Bip39MnemonicGenerator().FromWordsNumber(24)
    
    # Generate a seed from the mnemonic
    seed = Bip39SeedGenerator(mnemo).Generate()
    
    # Generate a BIP86 context from the seed, 
    ctx = Bip86.FromSeed(seed, Bip86Coins.BITCOIN_REGTEST)
    
    # Return the context
    return ctx

def generate_taproot_address(ctx, index=0, change=False):
    ch = Bip44Changes.CHAIN_INT if change else Bip44Changes.CHAIN_EXT
    node = (ctx.Purpose()
              .Coin()
              .Account(0)
              .Change(ch)
              .AddressIndex(index))
    return node.PublicKey().ToAddress()