import java.util.Queue;
import java.util.LinkedList;
class Solution {
    public static String predictPartyVictory(String senate) {
		Queue<Integer> d = new LinkedList<>();
		Queue<Integer> r = new LinkedList<>();

		int i = 0;
		for (char ch : senate.toCharArray()) {
			if (ch == 'D') d.add(i);
			else r.add(i);
			i++;
		}
		while (!r.isEmpty() && !d.isEmpty()) {
			if(r.peek() < d.peek()) r.add(i);
			else d.add(i);
			d.poll();
			r.poll();
			i++;
		}
		return r.isEmpty() ? "Dire" : "Radiant";
    }
	public static void main(String[] args) {
		System.out.println(predictPartyVictory("RDD"));
	}
}
