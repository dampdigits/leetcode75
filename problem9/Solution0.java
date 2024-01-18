public class Solution {
	public static void main(String[] args) {
		char chars[] = {'a','b','b','b','b','b','b','b','b','b','b','b','b'};
		System.out.println(compress(chars));
		for (char c : chars) {
			System.out.print(c + " ");
		}
	}
	public static int compress(char[] chars) {
		int strlen = chars.length, idx = 0, repeat = 0;
		char prev = ' ';
		
		// traverse through chars
        for (int i = 0; i < strlen; i++) {
			char ch = chars[i];
			// Check if current character does not match with previous
			if (ch != prev) {
				// Check for repetitions for previous character
				if (repeat > 0) {
					// Increment to count prev char along with repetitions
					++repeat;
					
					// Create char array to store the digits in repeat
					char digits[] = Integer.toString(repeat).toCharArray();
					// Store those digits in chars
					System.arraycopy(digits, 0, chars, idx, digits.length);
					
					idx = idx + digits.length;
					repeat = 0;
				}
				// add new character to chars
				chars[idx] = ch;
				// Set it as new previous to check with next character
				prev = ch;
				++idx;
			} else {
				++repeat;
			}
		}

		if (repeat > 0) {
			++repeat;
			// Create char array to store the digits in repeat
			char digits[] = Integer.toString(repeat).toCharArray();
			// Store those digits in chars
			System.arraycopy(digits, 0, chars, idx, digits.length);
			idx = idx + digits.length;
		}

		return idx;
    }
}

