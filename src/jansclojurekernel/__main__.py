#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""clojure kernel main"""

from ipykernel.kernelapp import IPKernelApp
from .kernel import jansclojurekernel
IPKernelApp.launch_instance(kernel_class=jansclojurekernel)
