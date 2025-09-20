from bip_utils import Bip32Slip10Secp256k1
from test_framework.key import ECKey, ECPubKey
from hashlib import sha256

SECP256K1_N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

class derivated_key:
    """
    delayed_priv = (base_priv + H(pc || basepoint)) mod n
    delayed_pub  = Pub(delayed_priv)
    """

    def __init__(self, seed: bytes, family: int):
        # Derive delayed_payment_basepoint: m/1017'/1'/4'/0/0
        base_ctx = Bip32Slip10Secp256k1.FromSeed(seed).DerivePath(f"m/1017'/1'/{family}'/0/0")
        self._base_secret_bytes  = base_ctx.PrivateKey().Raw().ToBytes()
        self._base_secret_int = base_ctx.PrivateKey().Raw().ToInt()
        self._base_bytes = base_ctx.PublicKey().RawCompressed().ToBytes()


    def get_delayed_pubkey(self, pc: bytes) -> ECPubKey:
        """Return delayed publey key as ECPubKey object."""
        priv = self.get_delayed_privkey(pc)
        pub = priv.get_pubkey()
        
        return pub
    

    def get_delayed_privkey(self, pc: bytes) -> ECKey:
        """Return delayed private key as ECKey object."""

        sha = sha256(pc + self._base_bytes).digest()
        sha_int = int.from_bytes(sha, 'big') % SECP256K1_N   
        pk = (self._base_secret_int + sha_int) % SECP256K1_N
        priv = ECKey()
        priv.set(pk.to_bytes(32, "big"), compressed=True)
        
        return priv
    
    def get_basepoint_compressed(self) -> bytes:
        """Return the basepoint bytes compressed (33 Bytes)"""
        return self._base_bytes