class ArithmeticEncoder:
    def __init__(self, precision):
        self.precision = precision
        self.max_value = 1 << precision
        self.max_range = 1 << (precision + 16)
        self.low = 0
        self.range = self.max_value

    def compress(self, value):
        value = int(value * self.max_value)
        high = self.low + (self.range * value) // self.max_value - 1
        low = self.low + (self.range * value) // self.max_value
        self.low = low
        self.range = high - low + 1
        return high

class ArithmeticDecoder:
    def __init__(self, precision):
        self.precision = precision
        self.max_value = 1 << precision
        self.max_range = 1 << (precision + 16)
        self.low = 0
        self.range = self.max_value

    def decompress(self, code):
        value = ((code - self.low + 1) * self.max_value - 1) // self.range
        high = self.low + (self.range * value) // self.max_value - 1
        low = self.low + (self.range * value) // self.max_value
        self.low = low
        self.range = high - low + 1
        return value / self.max_value

# Example usage:
precision = 25
encoder = ArithmeticEncoder(precision)
decoder = ArithmeticDecoder(precision)

# Float to compress
original_float = 0.456789

# Compression
compressed_code = encoder.compress(original_float)

# Decompression
decompressed_float = decoder.decompress(compressed_code)

print("Original float:", original_float)
print("Decompressed float:", decompressed_float)
