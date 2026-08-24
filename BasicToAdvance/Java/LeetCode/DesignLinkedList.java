public class DesignLinkedList {
	private static class Node {
		int val;
		Node next;

		Node(int val) {
			this.val = val;
		}
	}

	public static class MyLinkedList {
		private Node head;
		private Node tail;

		public int get(int index) {
			Node current = head;
			for (int i = 0; current != null; i++, current = current.next) {
				if (i == index) {
					return current.val;
				}
			}
			return -1;
		}

		public void addAtHead(int val) {
			Node node = new Node(val);
			node.next = head;
			head = node;
			if (tail == null) {
				tail = node;
			}
		}

		public void addAtTail(int val) {
			Node node = new Node(val);
			if (tail == null) {
				head = tail = node;
				return;
			}
			tail.next = node;
			tail = node;
		}

		public void addAtIndex(int index, int val) {
			if (index < 0) {
				return;
			}

			int length = 0;
			Node current = head;
			while (current != null) {
				length++;
				current = current.next;
			}

			if (index > length) {
				return;
			}
			if (index == 0) {
				addAtHead(val);
				return;
			}
			if (index == length) {
				addAtTail(val);
				return;
			}

			current = head;
			for (int i = 1; i < index; i++) {
				current = current.next;
			}
			Node node = new Node(val);
			node.next = current.next;
			current.next = node;
		}

		public void deleteAtIndex(int index) {
			if (index < 0 || head == null) {
				return;
			}
			if (index == 0) {
				head = head.next;
				if (head == null) {
					tail = null;
				}
				return;
			}

			Node previous = head;
			for (int i = 1; i < index && previous.next != null; i++) {
				previous = previous.next;
			}
			if (previous.next == null) {
				return;
			}
			if (previous.next == tail) {
				tail = previous;
			}
			previous.next = previous.next.next;
		}
	}
}
