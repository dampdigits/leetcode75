class Solution {
    // Create a map (HashMap) of HashMaps to represent the weighted graph
    Map<String, Map<String, Double>> graph = new HashMap<>();

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        for (int i = 0; i < equations.size(); i++) {
            List<String> equation = equations.get(i);
            String var1 = equation.get(0);
            String var2 = equation.get(1);
            double value = values[i];

            graph.putIfAbsent(var1, new HashMap<>());
            graph.putIfAbsent(var2, new HashMap<>());

            graph.get(var1).put(var2, value);
            graph.get(var2).put(var1, 1 / value); // Add inverse value for backtracking
        }

        double[] results = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);
            String start = query.get(0);
            String end = query.get(1);

            if (!graph.containsKey(start) || !graph.containsKey(end)) {
                results[i] = -1;
                continue;
            }

            double result = dfs(start, end, new HashSet<>(), 1.0);
            if (result == 0) results[i] = -1;
            else results[i] = result;
        }
        return results;
    }

    private double dfs(String current, String target, Set<String> visited, double accumulatedValue) {
        if (current.equals(target)) return accumulatedValue;

        visited.add(current);

        for (Map.Entry<String, Double> neighbor : graph.get(current).entrySet()) {
            String var = neighbor.getKey();
            double val = neighbor.getValue();
            
            if (!visited.contains(var)) {
                double result = dfs(var, target, visited, accumulatedValue*val);
                if (result != 0) return result;
            }
        }

        return 0.0; // No path found
    }
}
