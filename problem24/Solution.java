class Solution {
    public static String removeStars(String s) {
        StringBuilder ans = new StringBuilder();

        for (char ch : s.toCharArray())
            if (ch == '*') {
                if (! ans.isEmpty())
                    ans.deleteCharAt(ans.length() - 1);
            }
            else
                ans.append(ch);

        return ans.toString();
    }
	public static void main(String[] args) {
		String s = "leet**cod*e";
		System.out.println(removeStars(s));
	}
}
