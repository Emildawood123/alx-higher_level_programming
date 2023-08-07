#include "lists.h"
/**
 * check_cycle - no or there
 * @list: list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
listint_t *list1 = list;
listint_t *list2 = list;
if (list == NULL)
{
return (0);
}
while (list1 && list2 && list2->next)
{
list1 = list1->next;
list2 = list2->next;
list2 = list2->next;
if (list1 == list2)
{
return (1);
}
}
return (0);
}
