#include <stdio.h>
#include <Python.h>
void print_python_list_info(PyObject *p)
{
long int Size;
int i = 0;
PyListObject *list_Obj;
Size = PyList_Size(p);
printf("[*] Size of the Python List = %ld", Size)
list_Obj = (PyListObject *)p;
printf("[*] Allocated = %ld\n", list_Obj->allocated);
while (i < Size)
{
printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}
