class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0)
            return true;
        for (int count=1, planted=0, i=0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                if (count == 2 || (count==1 && i==flowerbed.length-1)){
                    if (planted+1 == n)
                        return true;
                    ++planted;
                    count = 1;
                } else
                    ++count;
            } else
                count = 0;
        }
        return false;
    }
}
