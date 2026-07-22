class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        padded = binary.zfill(32)
        rev_padded = padded[::-1]
        return int(rev_padded,2)