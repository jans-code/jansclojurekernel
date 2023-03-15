#!/usr/bin/env python
from ipykernel.kernelbase import Kernel
from pexpect import replwrap

clojurewrapper = replwrap.REPLWrapper("clojure", "user=> ", None)

class jansclojurekernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'clojure'
    language_version = '1.11.1.1252'
    language_info = {
        'name': 'clojure',
        'mimetype': 'application/clojure',
        'file_extension': '.clj',
    }
    banner = "Clojure kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            solution = clojurewrapper.run_command(code)
            solution = solution.strip()
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }