#include "lists.h"
/**
 * insert_node - function for insert node at a position
 * @head: poniter to the first node
 * @number: number to be added to the list
 * Return: returns address of new node or Null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;
	int i, j;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number, tmp = *head;
	if (!(*head))
		return (*head = new, new->next = NULL, new);
	for (i = 0; tmp; i++)
	{
		if (number > tmp->n)
		{
			if (!tmp->next)
				return (tmp->next = new, new->next = NULL, new);
			tmp = tmp->next;
			continue;
		}
		else
		{
			new->next = tmp;
			if (tmp == *head)
			{
				*head = new;
				break;
			}
			tmp = *head;
			for (j = 0; j < i; j++)
			{
				if (j == (i - 1))
				{
					tmp->next = new;
					break;
				}
				tmp = tmp->next;
			}
			break;
		}
	}
	return (new);
}
