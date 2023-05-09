#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it
 * @list: Pointer to the head node of the linked list
 *
 * Return: 0 if no cycle exist, 1 if cycle exists
 */

int check_cycle(listint_t *list)
{
	listint_t *single, *doubles;

	if (!list)
		return (0);

	single = list;
	doubles = list;

	while (doubles && doubles->next)
	{
		single = single->next;
		doubles = doubles->next->next;

		if (single == doubles)
			return (1);
	}

	return (0);
}

