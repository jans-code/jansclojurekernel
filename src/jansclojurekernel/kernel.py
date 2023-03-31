#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""clojure kernel"""

from ipykernel.kernelbase import Kernel
from pexpect import replwrap

def code_valid(string):
    """Test for valid input to avoid kernel hang"""
    string = string.strip()
    if string != '':
        bracket = 0
        gbracket = 0
        ebracket = 0
        quote = 0
        sense = True
        for elem in string:
            if sense:
                if elem == '(':
                    bracket += 1
                elif elem == ')':
                    bracket -= 1
                elif elem == '{':
                    gbracket += 1
                elif elem == '}':
                    gbracket -= 1
                elif elem == '[':
                    ebracket += 1
                elif elem == ']':
                    ebracket -= 1
                elif elem == '"':
                    sense = False
                    bracket += 1
            else:
                if elem == '"':
                    sense = True
                    bracket -= 1
        if bracket == 0 and gbracket == 0 and ebracket == 0 and quote == 0 and sense:
            return True
        else:
            return False
    else:
        return False

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
            code = code.replace("\n", " ")
            code = code.strip()
            if code_valid(code):
                solution = clojurewrapper.run_command(code)
                solution = solution.strip()
            else:
                solution = "Your input was incomplete or invalid."
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }