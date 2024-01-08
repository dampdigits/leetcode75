import java.util.Stack;

class Solution {
    public static int[] asteroidCollision(int[] asteroids) {
		Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {
            while (!stack.isEmpty() && stack.peek() > 0 && stack.peek() < -asteroid) {
                stack.pop();  // Right-moving asteroid explodes the left-moving asteroid
            }

            if (stack.isEmpty() || asteroid > 0 || stack.peek() < 0) {
                stack.push(asteroid);  // No collision or left-moving asteroid survives
            } else if (stack.peek() == -asteroid) {
                stack.pop();  // Both asteroids explode
            }
            // If left-moving asteroid survives, do nothing
        }

        // Convert stack to array
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }

        return result;
    }
	public static void main(String[] args) {
		int asteroids[] = {10,2,-5};
		int ans[] = asteroidCollision(asteroids);

		for (int i : ans)
			System.out.println(i);
	}
}
