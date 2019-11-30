"""
Definition for the nodes of linked list
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists: [ListNode]) -> ListNode:
    """
    Merges k sorted linked lists.
    :param lists: A list of pointers to the head of linked lists to be merged.
    :return: pointer to head of the merged linked list.
    """

    def merge(l1, l2):
        """
        Merges 2 sorted linked lists.
        :param l1: The head of the first list.
        :param l2: The head of the second list.
        :return: The head of the merged linked list.
        """
        # Edge cases, where nothing is to be done.
        if l1 is None and l2 is None: return l1
        if l1 is None: return l2
        if l2 is None: return l1

        # Vars to hold,
        # head -> a dummy head to keep a reference to the start of the merged
        # list.
        # _iter -> to move through the merged list.
        head = ListNode(float('-inf'))
        _iter = head

        # As long as both the lists are not exhausted,
        while l1 and l2:

            # Make the next of _iter as the smaller node.
            if l1.val <= l2.val:
                _iter.next = l1
                l1 = l1.next
            else:
                _iter.next = l2
                l2 = l2.next
            # Move _iter forward.
            _iter = _iter.next

        # If either of the lists remain, add them to the end,
        # Note: at-least one of the lists would be exhausted by now,
        # and the remaining one is sorted in itself, which is why this works.
        if not l1: _iter.next = l2
        if not l2: _iter.next = l1

        # Return a reference to the start of the merged list.
        return head.next

    # Vars to hold,
    # n -> The number of linked lists to be merged
    # interval -> gap between the two linked lists being merged each time.
    n, interval = len(lists), 1

    # As long as the interval is smaller than n,
    while interval < n:
        # Merge 2 linked lists in the list spaced interval apart.
        for i in range(0, n - interval, interval * 2):
            lists[i] = merge(lists[i], lists[i + interval])
        # Double the interval
        interval *= 2

    # If there is a result available, return it.
    return lists[0] if n > 0 else None
