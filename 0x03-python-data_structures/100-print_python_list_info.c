#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object point
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item;
	const char *typeName;
	Py_ssize_t size = PyList_Size(p); /*Get the size of the list*/
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	/*Get the allocated size*/
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		/*Get each item in the list*/
		/*Get the type of each item*/
		typeName = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, typeName);
	}
}
