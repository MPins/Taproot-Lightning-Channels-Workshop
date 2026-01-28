from bip_utils import Bip32Slip10Secp256k1
from functions.test_framework.key import *
from hashlib import sha256

SECP256K1_N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

class derivate_key:
    """
    priv = (base_priv + H(pc || basepoint)) mod n
    pub  = Pub(priv)
    """

    def __init__(self, seed: bytes, family: int, channel_index: int = 0):
        # Derive basepoints: m/1017'/1'/family'/0/channel_index
        base_ctx = Bip32Slip10Secp256k1.FromSeed(seed).DerivePath(f"m/1017'/1'/{family}'/0/{channel_index}")
        self._base_secret_bytes  = base_ctx.PrivateKey().Raw().ToBytes()
        self._base_secret_int = base_ctx.PrivateKey().Raw().ToInt()
        self._base_bytes = base_ctx.PublicKey().RawCompressed().ToBytes()

    def get_pubkey(self, pc: ECPubKey) -> ECPubKey:
        """Return pubkey key as ECPubKey object."""
        priv = self.get_privkey(pc)
        pub = priv.get_pubkey()
        
        return pub

    def get_privkey(self, pc: ECPubKey) -> ECKey:
        """Return private key as ECKey object."""

        sha = sha256(pc.get_bytes(bip340=False) + self._base_bytes).digest()
        sha_int = int.from_bytes(sha, 'big') % SECP256K1_N   
        pk = (self._base_secret_int + sha_int) % SECP256K1_N
        priv = ECKey()
        priv.set(pk.to_bytes(32, "big"), compressed=True)
        
        return priv
    
    def get_basepoint_compressed(self) -> bytes:
        """Return the basepoint bytes compressed (33 Bytes)"""
        return self._base_bytes
    
class derivate_revocation_key:
    """
    pub = (base * H(base || pc) + pc * H(pc || base)) mod n
    priv = (base_secret * H(base || pc) + pcs * H(pc || base)) mod n
    """

    def __init__(self, seed: bytes, channel_index: int):
        # Derive revocation basepoints: m/1017'/1'/1'/0/channel_index
        base_ctx = Bip32Slip10Secp256k1.FromSeed(seed).DerivePath(f"m/1017'/1'/1'/0/{channel_index}")
        self._base_secret_int = base_ctx.PrivateKey().Raw().ToInt()
        self._base_bytes = base_ctx.PublicKey().RawCompressed().ToBytes()

    def get_pubkey(self, pc: ECPubKey) -> ECPubKey:
        # s1 = H(base || pc), s2 = H(pc || base)
        s1 =  int.from_bytes(sha256(self._base_bytes + pc.get_bytes(bip340=False)).digest(), 'big') % SECP256K1_N
        s2 = int.from_bytes(sha256(pc.get_bytes(bip340=False) + self._base_bytes).digest(), 'big') % SECP256K1_N
        pub =  ECPubKey().set(self._base_bytes).mul(s1) + pc.mul(s2)
        
        return pub

    def get_privkey(self, pcs: ECKey) -> ECKey:
        # s1 = H(base || pc), s2 = H(pc || base) com pc = Pub(pcs)
        pc_bytes = pcs.get_pubkey().get_bytes(bip340=False)
        s1 = int.from_bytes(sha256(self._base_bytes + pc_bytes).digest(), 'big') % SECP256K1_N
        s2 = int.from_bytes(sha256(pc_bytes + self._base_bytes).digest(), 'big') % SECP256K1_N

        pcs_int = int.from_bytes(pcs.get_bytes(), 'big')
        sk = (self._base_secret_int * s1 + pcs_int * s2) % SECP256K1_N

        priv = ECKey()
        priv.set(sk.to_bytes(32, "big"), compressed=True)
        return priv
