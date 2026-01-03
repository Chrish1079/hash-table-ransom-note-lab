def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Track letter counts from the magazine using a dictionary (hash table)
    magazine_counts = {}
    for char in magazine:
        magazine_counts[char] = magazine_counts.get(char, 0) + 1
    
    # Check each character in the ransom note
    for char in ransomNote:
        # Return False early if character is missing or depleted
        if char not in magazine_counts or magazine_counts[char] <= 0:
            return False
        # Decrement the count as we use the character
        magazine_counts[char] -= 1
    
    # All characters can be constructed
    return True
