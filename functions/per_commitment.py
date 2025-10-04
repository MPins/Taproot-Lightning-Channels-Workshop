from hashlib import sha256, hmac
from functions.test_framework.key import *
from functions.bip0327.reference import nonce_gen

# Flip the (bit_index % 8) bit of the (bit_index // 8) byte in value.
def flip_bit(value: bytearray, bit_index: int):
    byte_index = bit_index // 8  # Get the byte index
    bit_position = bit_index % 8  # Get the bit position within the byte
    value[byte_index] ^= (1 << bit_position)  # Flip the bit using XOR

# Generate a derived value P from a seed and an integer I
# param seed: 32-byte initial seed.
# param I: Index whose set bits determine which bits in P get flipped.
# return: 32-byte derived value P.
def generate_from_seed(seed: bytes, I: int) -> bytes:
    P = bytearray(seed)  # Convert to mutable bytearray

    for B in range(47, -1, -1):  # Iterate from 47 down to 0
        if (I & (1 << B)) != 0:  # Check if bit B is set in I
            flip_bit(P, B)  # Flip the corresponding bit in P
            P = bytearray(sha256(P).digest())  # Hash P and convert back to bytearray

    return bytes(P)  # Convert back to bytes before returning

class per_commitment:
    """
    Helper for generating per-commitment private/public keys
    from a per_commitment_seed and an index.
    """

    def __init__(self, seed: bytes, index: int):
        self.seed = seed
        self.index = 0xFFFFFFFFFFFF - index
        self._priv = None
        self._pub = None

    def get_priv(self) -> ECKey:
        """Return the per-commitment private key (ECKey)."""
        if self._priv is None:
            secret = generate_from_seed(self.seed, self.index)
            self._priv = ECKey().set(secret, compressed=True)
        return self._priv

    def get_pub(self) -> ECPubKey:
        """Return the per-commitment public key (ECPubKey)."""
        if self._pub is None:
            self._pub = self.get_priv().get_pubkey()
        return self._pub

    def get_compressed(self) -> bytes:
        """Return the per-commitment public key compressed (33 bytes)."""
        return self.get_pub().get_bytes(bip340=False)
    
    # Generate a nonce for signing a transaction using the per-commitment secret.
    def nonce_per_commitment(self, seed: bytes, index: int, sk: bytes, pk: bytes, agg_pubkey_tweaked: bytes, sighash: bytes):

        shachain_root_hash = sha256(seed).digest()
        nonce_seed = hmac.new(key=shachain_root_hash, msg=b"taproot-rev-root", digestmod=sha256).digest()
        k = generate_from_seed(nonce_seed, 0xFFFFFFFFFFFF - index)
        return nonce_gen(sk, pk, agg_pubkey_tweaked, sighash, k) 