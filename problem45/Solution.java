import java.util.List;
import java.util.ArrayList;

public class Solution {
    private int reorderCount = 0;
    private List<Integer> visited = new ArrayList<>();
	private List<List<Integer>> graph = new ArrayList<>();

    public static void main(String[] args) {
        int connections[][] = {{0,1},{1,3},{2,3},{4,0},{4,5}};
        System.out.println("Reorders = " + new Solution().minReorder(6, connections));
    }

    public int minReorder(int n, int[][] connections) {
		for (int i = 0; i < n; i++)
			graph.add(i, new ArrayList<>());

		for (int[] pair : connections) {
			graph.get(pair[0]).add(pair[1]);
			graph.get(pair[1]).add(-pair[0]);
		}
		dfs(0);
		return reorderCount;
    }

    private void dfs(int city) {
		if (visited.contains(city)) return;
		visited.add(city);
		for (int neighbour : graph.get(city)) {
			if (visited.contains(Math.abs(neighbour))) continue;
			if (neighbour > 0) reorderCount++;
			dfs(Math.abs(neighbour));
		}
    }
}

