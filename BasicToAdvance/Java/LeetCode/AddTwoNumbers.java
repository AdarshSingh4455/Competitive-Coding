class ListNode {
	int val;
	ListNode next;

	ListNode() {
	}

	ListNode(int val) {
		this.val = val;
	}

	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}
}

class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		if (l1 == null && l2 == null) {
			return null;
		}

		ListNode dummy = new ListNode(0);
		ListNode current = dummy;
		int carry = 0;

		while (l1 != null || l2 != null || carry != 0) {
			int x = l1 != null ? l1.val : 0;
			int y = l2 != null ? l2.val : 0;
			int total = x + y + carry;

			current.next = new ListNode(total % 10);
			carry = total / 10;
			current = current.next;

			if (l1 != null) {
				l1 = l1.next;
			}
			if (l2 != null) {
				l2 = l2.next;
			}
		}

		return dummy.next;
	}
}
