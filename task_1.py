# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def insertion_sort_linked_list(head):
    dummy = ListNode(0)
    dummy.next = head
    prev_sorted = dummy
    curr_unsorted = head
    while curr_unsorted:
        if curr_unsorted.next and curr_unsorted.next.val < prev_sorted.next.val:
            while prev_sorted.next and prev_sorted.next.val < curr_unsorted.next.val:
                prev_sorted = prev_sorted.next
            temp = prev_sorted.next
            prev_sorted.next = curr_unsorted.next
            curr_unsorted.next = curr_unsorted.next.next
            prev_sorted.next.next = temp
            prev_sorted = dummy
        else:
            curr_unsorted = curr_unsorted.next
    return dummy.next

def merge_sorted_linked_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Тест

# Створення тестового однозв'язного списку
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(5)

print("Вихідний список:")
print_linked_list(head)

# Реверсування списку
reversed_head = reverse_linked_list(head)
print("\nПісля реверсування:")
print_linked_list(reversed_head)

# Сортування вставками
sorted_head = insertion_sort_linked_list(reversed_head)
print("\nПісля сортування:")
print_linked_list(sorted_head)

# Об'єднання двох відсортованих списків
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

merged_head = merge_sorted_linked_lists(l1, l2)
print("\nПісля об'єднання двох відсортованих списків:")
print_linked_list(merged_head)
