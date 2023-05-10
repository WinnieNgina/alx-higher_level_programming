#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head double pointer to the linked list
 * @number: value of the node inserted
 * Return: Linked list node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *tmp_head;

	if (head == NULL)
	/*check if the double pointer has the address for the head node of the list*/
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	/*check if memory for the new_node is allocated successfully*/
	if (new_node == NULL)
		return (NULL);
	/*malloc failure*/
	if (*head == NULL)
	/*Check if the list is empty and make the new node the head node*/
	{
		*head = new_node;
		return (new_node);
	}
	tmp_head = *head;
	/*helps us traverse the linked list*/
	if (number < tmp_head->n)
	{
		new_node->next = tmp_head;
		/*new_node stores address of the head node*/
		*head = new_node;
		return (new_node);
	}
	while (tmp_head->next != NULL && tmp_head->next->n < number)
		tmp_head = tmp_head->next;
	new_node->next = tmp_head->next;
	/*Connect the new node to the next node in the list*/
	tmp_head->next = new_node;
	/*Connect the previous node to the new node*/
	return (new_node);
}
