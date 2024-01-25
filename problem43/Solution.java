class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        List<Integer> keys = new ArrayList<>();
        keys.add(0);
        for (int i = 0; i < keys.size(); i++) {
            for (int j = rooms.get(keys.get(i)).size() - 1; j >= 0; j--) {
                int key = rooms.get(keys.get(i)).get(j);
                if (!keys.contains(key))
                    keys.add(key);
            }
        }
        return keys.size() == rooms.size();
    }
}
