#include "lists.h"
/**
 * insert_node - that funcation insert node
 * @number: number of new node
 * @head: head
 * Return: address of new or null
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp;
listint_t *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
temp = (*head);
new->n = number;
if (number < (*head)->n)
{
new->next = (*head);
(*head) = new;
return (new);
}
if (temp == NULL)
{
new->next = temp;
(*head) = new;
return (new);
}
while (temp && temp->next->n < number && temp)
{
temp = temp->next;
}
new->next = temp->next;
temp->next = new;
return (new);
}
