#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - funtion that prints basic info about python list
 * @p: the python object
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	PyObject *item;
	PyListObject *list;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Error:Object is not a list.\n");
		return;
	}

	size = PyList_Size(p);
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);


	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
	if (PyErr_Occurred())
		PyErr_Print();
}
