.. grokking-algorithms documentation master file, created by
   sphinx-quickstart on Thu Oct  1 10:17:49 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


=================================
Grokking Algorithms Concepts documentation
=================================

Problems
==========

Problem 1:
----------

I can't figure out the binary search implementation!?
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: What I tried
  
  At first I try to implement binary search without AI help or viewing book's implementation.
  But this is not worked. After that I use AI to get a correct implementation but my code output
  was not correct! Finally I used book's implementation in page 9 to correct my different program.


.. ▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼

Problem 2:
----------

I was a little confused about logarithms!
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: What I tried
  
  1. Read the book's definition for logarithms.

  2. Watch some tutorials in KhanAcademy about logarithms.

  3. Solve some practices in KhanAcademy about logarithms.


.. ▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼

Problem 3:
----------

I had no idea to understand the concept of permuatation!
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: What I tried
  
  1. Watch one video about permutation in KhanAcademy

  2. Compare this concept to factorial concept (n!) and the ambiguity was resolved.


.. ▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼

Problem 4:
----------

I want to inspect call stacks in a Python program that runs a recursive factorial function!
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: What I tried

  1. I used the ``strace`` tool to inspect call stacks but it is not useful because ``strace``
     just traces system calls in kernel space and does not show me user calls in user space (which Python programs use).
  2. I asked AI to get help. It suggests that I use one of these tools:

     * ``py-spy``
     * ``gdb``
     * ``faulthandler``
     * ``perf``
  3. First I used ``py-spy``::

      py-spy record -o out.svg --pid 66763

    .. image:: _static/out.svg


     
This is a very long sentence that I want to keep
several source lines, but it should render as a
single paragraph in the PDF.






.. toctree::
   :maxdepth: 3
   :caption: Contents:

