class Solution {
    public int compress(char[] chars) {
        int idx=0;
        int i=0;
        while(i<chars.length){
            int c=0;
            char ch = chars[i];
            while(i<chars.length && ch==chars[i]){
                c++;
                i++;
            }
            chars[idx++]=ch;
            if(c>1){
                for(char val:Integer.toString(c).toCharArray()){
                    chars[idx++]=val;
                }
            }
        }
        return idx;
    }
}
