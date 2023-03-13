#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - function for checking a cycle in a linked list
 * @list: pointer to the list
 * Return: returns 0 if there is no cycle 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *p = list, listint_t *q = list;

	while (p && q && p->next)
	{
		p = p->next;
		q = q->next->next;

		if (p == q)
		{
			return (1);
		}
	}
	return (0);

}
