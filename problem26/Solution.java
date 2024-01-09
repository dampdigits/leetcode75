class Solution {
    public static String decodeString(String s) {
        String decodedStr = "";

		for (int i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
			// Concat if letter
			if (Character.isLetter(ch))
				decodedStr += ch;
			else if (Character.isDigit(ch)) {
				int num = 0;
				// Extract number
				do {
					num = (num * 10) + (ch - 48);
					++i;
					ch = s.charAt(i);
				} while(Character.isDigit(ch));
				// Extract substring to be repeated
				int openBrkt = 0, closeBrkt = 0;
				String substr = "";
				++i;
				while (closeBrkt <= openBrkt) {
					ch = s.charAt(i);
					if (ch == '[')
						openBrkt++;
					else if (ch == ']')
						closeBrkt++;
					substr += ch;
					++i;
				}
				// Repeat substring and concat
				decodedStr += new String(new char[num]).replace("\0", decodeString(substr));
				i--;
			}
		}
		return decodedStr;
    }
	public static void main(String[] args) {
		System.out.println(decodeString("2[a3[b]x]efg"));
	}
}
