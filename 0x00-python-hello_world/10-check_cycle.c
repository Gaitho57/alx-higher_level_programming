#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
#include "lists.h"

int check_cycle(listint_t *list) {
    if (list == NULL || list->next == NULL) {
        return 0;
    }

    listint_t *wlker = list;
    listint_t *runna = list;

    while (runna != NULL && runna->next != NULL) {
        wlker = wlker->next;
        runna = runna->next->next;

        if (wlker == runna) {
            return 1;
        }
    }
    return 0;
}
