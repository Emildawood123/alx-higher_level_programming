#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
int size
int i = 0;
PyObject *object;
size = Py_SIZE(p);
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
while (i < size)
{
printf("Element %d: ", i);
object = PyList_GetItem(p, i);
printf("%s\n", Py_TYPE(object)->tp_name);
i++;
}
}

