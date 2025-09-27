# witnessScaleFactor determines the level of "discount" witness data
# receives compared to "base" data. A scale factor of 4, denotes that
# witness data is 1/4 as cheap as regular non-witness data.
witness_scale_factor = 4

# InputSize 41 bytes
#	- PreviousOutPoint:
#		- Hash: 32 bytes
#		- Index: 4 bytes
#	- OP_DATA: 1 byte (ScriptSigLength)
#	- ScriptSig: 0 bytes
#	- Witness <----	we use "Witness" instead of "ScriptSig" for
# 			transaction validation, but "Witness" is stored
# 			separately and weight for it size is smaller. So
# 			we separate the calculation of ordinary data
# 			from witness data.
#	- Sequence: 4 bytes
funding_input_size = 32 + 4 + 1 + 4

# P2TRSize 34 bytes
# 	- OP_0: 1 byte
#	- OP_DATA: 1 byte (x-only public key length)
#	- x-only public key length: 32 bytes
p2tr_size = 34

# TaprootCommitmentOutput 43 bytes
#	- Value: 8 bytes
#	- VarInt: 1 byte (PkScript length)
#	- PkScript (P2TR)
taproot_commitment_output = 8 + 1 + p2tr_size

# TaprootCommitmentAnchorOutput 43 bytes
#	- Value: 8 bytes
#	- VarInt: 1 byte (PkScript length)
#	- PkScript (P2TR)
taproot_commitment_anchor_output = 8 + 1 + p2tr_size

# BaseTaprootCommitmentTxWeight 225 + 43 * num-htlc-outputs bytes
#	- Version: 4 bytes
#	- WitnessHeader <---- part of the witness data
#	- CountTxIn: 1 byte
#	- TxIn: 41 bytes
#		FundingInput
#	- CountTxOut: 3 byte
#	- TxOut: 172 + 43 * num-htlc-outputs bytes
#		OutputPayingToThem,
#		OutputPayingToUs,
#		....HTLCOutputs...
#	- LockTime: 4 bytes
def base_taproot_commitment_tx_weight(num_tap_out: int, num_anchor_out: int) -> int:
        base_taproot_commitment_tx_weight = (4 + 1 + funding_input_size + 3 + num_tap_out*taproot_commitment_output + 
                                         num_anchor_out*taproot_commitment_anchor_output + 4) * witness_scale_factor
        
        return base_taproot_commitment_tx_weight

# TaprootSignatureWitnessSize 65 bytes
#	- sigLength: 1 byte
#	- sig: 64 bytes
taproot_signature_witness_size = 1 + 64

# TaprootKeyPathWitnessSize 66 bytes
#	- NumberOfWitnessElements: 1 byte
#	- sigLength: 1 byte
#	- sig: 64 bytes
taproot_key_path_witness_size = 1 + taproot_signature_witness_size

# WitnessHeaderSize 2 bytes
#	- Flag: 1 byte
#	- Marker: 1 byte
witness_header_size = 1 + 1

# Taproot Commitment Weight
def taproot_commit_weight(NumTapOut: int, NumAnchorOut: int) -> int:
    taproot_commit_weight = (base_taproot_commitment_tx_weight(NumTapOut, NumAnchorOut) + witness_header_size + taproot_key_path_witness_size)

    return taproot_commit_weight