#include "lists.h"
/**
 * check_cycle - checks if linked list contains a cycle
 * @list: linked list check
 *
 * Return: one if list has cycle, zero if it isn't a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (!list)
		return (0);

	while (slw && fst && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
			return (1);
	}
	return (0);
}



