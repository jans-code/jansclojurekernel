#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansclojurekernel
IPKernelApp.launch_instance(kernel_class=jansclojurekernel)
