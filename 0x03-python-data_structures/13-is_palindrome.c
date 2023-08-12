#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - that funcation to know p...
 * @head: head of linked list
 * Return: 0 no or yes 1
 */
int is_palindrome(listint_t **head)
{
listint_t *temp = (*head);
listint_t *temp2 = (*head);
int count = 0;
int *first, *second;
int i = 0, c;
while (temp)
{
temp = temp->next;
count++;
}
first = malloc((count / 2) * sizeof(int));
second = malloc((count / 2) * sizeof(int));
while (i < count / 2)
{
first[i] = temp2->n;
temp2 = temp2->next;
i++;
}
i = 0;
while (i < count / 2)
{
second[i] = temp2->n;
temp2 = temp2->next;
i++;
}
for (c = 0; c < count / 2; c++)
{
if (first[c] == second[i - 1])
{
i--;
continue;
}
else
{
return (0);
}
i--;
}
return (1);
}
