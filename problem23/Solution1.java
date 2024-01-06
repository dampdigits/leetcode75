class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length, count=0;
        int[][] grid2 = new int[n][n];
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++)
                grid2[j][i]=grid[i][j];

        for(int i=0;i<n;i++) {
            int[] arr = grid[i];
            for(int j=0;j<n;j++) {
                int[] arr2 = grid2[j];
                if(Arrays.equals(arr,arr2))
                    count++;
            }
        }
        return count;
    }
}
