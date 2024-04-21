def encode(data:float, golomb_parameter:int)-> str:
    """
    Encode a non-negative integer x using Golomb-Rice coding with parameter k.

    Parameters:
    x (int): The non-negative integer to encode.
    k (int): The parameter k in Golomb-Rice coding, which determines the
             divisor M as 2^k.

    Returns:
    str: The Golomb-Rice encoded binary string.
    """
    
    quotionet  = data >> golomb_parameter   # Equivalent to integer division of x by 2^k
    remainder = data & ((1<< golomb_parameter)-1)       # Equivalent to x mod 2^k
    
    unary_code =  '1'*quotionet + '0'
    remainder = bin(remainder)[2:].zfill(golomb_parameter)
    
    return unary_code + remainder
    
    
    
    

def decode(encoded_string, k):
    """
    Decode a Golomb-Rice encoded binary string back to a non-negative integer.

    Parameters:
    encoded_string (str): The Golomb-Rice encoded binary string.
    k (int): The parameter k used during encoding, which determines the divisor M as 2^k.

    Returns:
    int: The decoded non-negative integer.
    """
    # Find the first '0' to determine the quotient in unary coding
    quotient = 0
    while encoded_string[quotient] == '1':
        quotient += 1

    # The remainder is the next k bits in the binary string
    remainder_start = quotient + 1
    remainder_end = remainder_start + k
    remainder = encoded_string[remainder_start:remainder_end]

    # Convert binary string to integer
    remainder_value = int(remainder, 2)

    # Calculate the original number
    original_number = (quotient << k) + remainder_value  # (quotient * 2^k) + remainder
    return original_number
