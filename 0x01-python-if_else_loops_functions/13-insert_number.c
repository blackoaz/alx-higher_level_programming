#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - function for insert node at a position
 * @head: poniter to the first node
 * @number: number to be added to the list
 * Return: returns address of new node or Null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!head || !(*head))
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	node = *head;
	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}
	if (number <= node->n)
	{
		new_node->n = number;
		new_node->next = node;
		node = new_node->next;
		*head = new_node;
		return (new_node);
	}
	while (node)
	{
		if (!node->next)
			return (add_nodeint_end(head, number));
		if ((number > node->n) && (number <= (node->next)->n))
		{
			new_node->n = number;
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}
		node = node->next;
	}
	free(new_node);
	return (NULL);
}
