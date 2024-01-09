import java.util.Stack;

class Solution {
    public static int[] asteroidCollision(int[] asteroids) {
		Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {
			if (asteroid > 0 || stack.empty() || stack.peek() < 0)
				stack.push(asteroid);
			else {
				int last = asteroid, top = stack.peek();
				while ((top > 0) && (top <= -asteroid) && (!stack.empty()) && (last != -asteroid)) {
					last = stack.pop();
					if (! stack.empty())
						top = stack.peek();
				}
				if ((stack.empty() || top < 0) && last != -asteroid)
					stack.push(asteroid);
			}
        }

        // Convert stack to array
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }
	public static void main(String[] args) {
		int asteroids[] = {-2,-2,1,-1};
		int ans[] = asteroidCollision(asteroids);

		for (int i : ans)
			System.out.println(i);
	}
}
