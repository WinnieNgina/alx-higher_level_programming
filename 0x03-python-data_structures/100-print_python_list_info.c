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

	Py_ssize_t size = PyList_Size(p);  /*Get the size of the list*/
	printf("Size of the list: %zd\n", size);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);  /*Get each item in the list*/
		/*Get the type of each item*/
		typeName = Py_TYPE(item)->tp_name;
		printf("Item %zd: Type = %s\n", i, typeName);
	}
}

