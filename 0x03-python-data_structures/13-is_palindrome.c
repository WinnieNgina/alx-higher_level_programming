#include "lists.h"
/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: a pointer to the head node of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_head = *head;
	int i = 0;
	int arr[10000];
	int index;
	int j;

	if (tmp_head == NULL || tmp_head->next == NULL)
		return (1);
	/*An empty list is considered a palindrome*/

	while (tmp_head != NULL)
	/*Copy the linked list values into the array*/
	{
		arr[i] = tmp_head->n;
		tmp_head = tmp_head->next;
		i++;
	}
	/*Check if the array is a palindrome*/
	for (index = 0, j = i - 1; index < j; index++, j--)
	{
		if (arr[index] != arr[j])
			return (0);
	}
	return (1);
}
