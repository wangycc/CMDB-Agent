#!/bin/env python
#coding=utf-8

import platform

class BasePlugin(object):
    
    @classmethod
    def instance(cls):
        if hasattr(cls,'instance'):
            return getattr(cls(),'instance')
        else:
            obj = cls()
            setattr(cls,'instance',obj)
            return obj
    def is_os_32(self):
        os_bit,executable_type = platform.architecture()
        if os_bit == '32bit':
            return True
        elif os_bit == '64bit':
            return False
        else:
            raise Exception('Unkown os bit')

    def execute(self):
        result = platform.system()
        if result == 'linux':
            return self.linux()
        elif result == 'windows':
            return self.windows()
        else:
            raise Exception('Unkown os system')

    def windows(self):
        raise Exception('You must implement  windows')

    def linux(self):
        raise Exception('You must implement linux')



            

