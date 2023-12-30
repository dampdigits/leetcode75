class Solution {
    public String reverseVowels(String s) {
        StringBuilder ans = new StringBuilder(s);
        for (int i=0, j=s.length()-1; i < j; i++) {
            char ch1 = s.charAt(i);
            if (ch1=='a' || ch1=='A' || ch1=='e' || ch1=='E' || ch1=='i' || ch1=='I' || ch1=='o' || ch1=='O' || ch1=='u' || ch1=='U')
            {
                for (; j>i; j--) {
                    char ch2 = s.charAt(j);
                    if (ch2=='a' || ch2=='A' || ch2=='e' || ch2=='E' || ch2=='i' || ch2=='I' || ch2=='o' || ch2=='O' || ch2=='u' || ch2=='U') {
                        ans.replace(i,i+1,Character.toString(ch2));
                        ans.replace(j,j+1,Character.toString(ch1));
                        --j;
                        break;
                    }
                }
            }
        }
        return ans.toString();
    }
}
