public class Solution {
	public static void main(String[] args) {
		System.out.println(isSubsequence("axc", "ahbgdc"));
	}
	public static boolean isSubsequence(String s, String t) {
        int i, j, slen = s.length(), tlen = t.length();
		for (i = 0, j = 0; i < slen && j < tlen; j++) {
        	if (s.charAt(i) == t.charAt(j))
				++i;
        }
		if (i == slen)
			return true;
		return false;
    }
}
