import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public static int equalPairs(int[][] grid) {
        List<int[]> rows = new ArrayList<>();
        List<int[]> cols = new ArrayList<>();
        int pairs = 0, n = grid.length;

        for (int i = 0; i < n; i++)
            rows.add(grid[i]);

        for (int i = 0; i < n; i++) {
            int temp[] = new int[n];

            for (int j = 0; j < n; j++)
                temp[j] = grid[j][i];

            cols.add(temp);
        }

        for (int[] col : cols)
            for (int[] row : rows)
                if (Arrays.equals(col, row))
                    pairs++;
        
		return pairs;
	}
	public static void main(String[] args) {
		int grid[][] = {{3,1,2,2},{1,4,4,5},{2,4,2,2},{2,4,2,2}};
		System.out.println(equalPairs(grid));
	}
}
