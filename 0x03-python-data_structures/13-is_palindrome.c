#include "lists.h"
/**
 * is_palindrome -checks if a singly linked list is a palindrome.
 * @head: a pointer to the head node of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp_head;
	int i = 1;
	int arr[i];
	int index;
	int j;
	int palindrome;

	if (head == NULL)
		return (0);
	tmp_head = *head;
	if (tmp_head == NULL || tmp_head->next == NULL)
		return (1);
	/*An empty list is considered a palindrome*/

	while (tmp_head != NULL)
	{
		arr[i] = tmp_head->n;
		tmp_head = tmp_head->next;
		i++;
	}
	for (index = 0, j = i - 1; index < j; i++, j--)
	{
		if (arr[index] != arr[j])
		{
			palindrome = 0;
		}
		else
		{
			  palindrome = 0;
		}
	}
	return (palindrome);
}
