#!/usr/bin/env python3
"""
🧙‍♂️ The Fibonacci Sequence Spell 🧙‍♂️
Ancient Magic by Kiro the Grey Hat

This mystical scroll generates the sacred Fibonacci numbers,
where each number is the sum of the two preceding ones.
The sequence begins with 0 and 1, mirroring the duality
of all existence in the magical realm.
"""

def fibonacci_spell(n):
    """
    Conjures the first n numbers of the Fibonacci sequence
    
    Args:
        n (int): Number of Fibonacci numbers to generate
        
    Returns:
        list: The sacred sequence of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the mystical sequence
    fib_sequence = [0, 1]
    
    # Cast the spell to generate the remaining numbers
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

def display_magical_results(sequence):
    """
    Display the results with proper mystical formatting
    """
    print("✨" * 50)
    print("🧙‍♂️  THE FIBONACCI SEQUENCE SPELL HAS BEEN CAST!  🧙‍♂️")
    print("✨" * 50)
    print()
    
    print("The first 10 sacred Fibonacci numbers are:")
    print("-" * 40)
    
    for i, num in enumerate(sequence):
        print(f"Position {i+1:2d}: {num:3d}")
    
    print("-" * 40)
    print(f"Sum of all numbers: {sum(sequence)}")
    print(f"Golden ratio approximation: {sequence[-1]/sequence[-2]:.6f}")
    print("✨" * 50)

if __name__ == "__main__":
    # Cast the spell for the first 10 Fibonacci numbers
    magical_sequence = fibonacci_spell(10)
    display_magical_results(magical_sequence)
    
    # Additional magical insight
    print("\n🔮 Mystical Properties:")
    print(f"   • Each number is the sum of the two before it")
    print(f"   • The ratio between consecutive numbers approaches φ (phi) ≈ 1.618033...")
    print(f"   • This sequence appears throughout nature: shells, flowers, galaxies!")
    print("✨ The magic of mathematics reveals itself! ✨")