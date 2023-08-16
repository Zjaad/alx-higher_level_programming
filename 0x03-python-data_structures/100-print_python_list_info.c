#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t length = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", length);
    printf("[*] Allocated = %ld\n", allocated);
    
    for (Py_ssize_t i = 0; i < length; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
