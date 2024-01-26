class Solution {
    public int findCircleNum(int[][] isConnected) {
        int provinces = 0;
        int n = isConnected.length;
        boolean visited[] = new boolean[n];
        for (int i = 0; i < n; i++)
            if (!visited[i]) {
                provinces ++;
                visit(i, isConnected, visited);
            }
        return provinces;
    }
    private void visit(int i, int[][] isConnected, boolean visited[]) {
        int n = isConnected.length;
        for (int j = 0; j < n; j++)
            if (isConnected[i][j] == 1 && (!visited[j])) {
                visited[j] = true;
                visit(j, isConnected, visited);
            }
    }
}
