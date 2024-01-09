class Solution {
    public static String decodeString(String s) {
        String decodedStr = "";

		for (int i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
			if (Character.isLetter(ch))
				decodedStr += ch;
			else if (Character.isDigit(ch)) {
				int num = 0;
				do {
					num = (num * 10) + (ch - 48);
					++i;
					ch = s.charAt(i);
				} while(Character.isDigit(ch));
				int openBrkt = 0, closeBrkt = 0;
				String substr = "";
				++i;
				while (closeBrkt <= openBrkt && i < s.length()) {
					ch = s.charAt(i);
					if (ch == '[')
						openBrkt++;
					else if (ch == ']')
						closeBrkt++;
					substr += ch;
					++i;
				}
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
