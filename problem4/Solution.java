class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
		// return true if no new flowers
        if (n == 0)
            return true;
		// count = no. of empty spots, planted = no. of flowers planted
        for (int count=1, planted=0, i=0; i < flowerbed.length; i++) {
			// check for empty spot
            if (flowerbed[i] == 0) {
				// if this is the 3rd empty spot in a row || the second empty spot and the last spot
                if (count == 2 || (count==1 && i==flowerbed.length-1)){
					// if all plants are planted
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
