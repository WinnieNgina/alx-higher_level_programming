#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	/*Declare two pointers to traverse the linked list*/
	if (list == NULL)
	/*chech if the list is empty, therefore no circle*/
		return (0);
	slow = list;
	/*initalize the slow pointer at the head node*/
	fast = list->next;
	/*intialize the fast pointer at the node after head node*/

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		/*If the slow and fast pointers meet at the same node, there is a cycle*/
			return (1);
		slow = slow->next;
		fast = fast->next->next;
		/*we move the slow pointer one step forward*/
		/*and the fast pointer two steps forward.*/
	}
	return (0);
}

