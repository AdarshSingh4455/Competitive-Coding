class BinarySearchSolution {
	private int[] nums;
	private int target;

	public BinarySearchSolution(int[] nums, int target) {
		this.nums = nums;
		this.target = target;
	}

	public int search(int[] nums, int target) {
		int low = 0;
		int high = nums.length - 1;

		while (low <= high) {
			int mid = low + (high - low) / 2;
			if (nums[mid] == target) {
				return mid;
			} else if (nums[mid] > target) {
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}

		return -1;
	}

	public static void main(String[] args) {
		int[] nums = {-1, 0, 3, 5, 9, 12};
		int target = 9;
		BinarySearchSolution solution = new BinarySearchSolution(nums, target);
		System.out.println(solution.search(solution.nums, solution.target));
	}
}
