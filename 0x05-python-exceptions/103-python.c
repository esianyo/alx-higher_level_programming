#include <Python.h>
#include <stdio.h>
#include <floatobject.h>

/**
 * print_python_list - Prints basic information about a Python list object
 * @p: Pointer to the PyObject representing the Python list
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object
 * @p: Pointer to the PyObject representing the Python bytes
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_GET_SIZE(p);
	char *data = PyBytes_AS_STRING(p);
	int max_bytes = size < 10 ? size : 10;
	int i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", data);

	printf("  first %d bytes: ", max_bytes);
	for (i = 0; i < max_bytes; i++)
	{
		printf("%02x", (unsigned char)data[i]);
		if (i < max_bytes - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic information about a Python float object
 * @p: Pointer to the PyObject representing the Python float
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid PyFloatObject\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  value: %f\n", value);
}
