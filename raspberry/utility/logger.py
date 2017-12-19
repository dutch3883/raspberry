class Logger:
    def _out(str):
        print(str)
    
    def error(str):
        _out('[Error]: '+str)
    
    def info(str):
        _out('[Info]: '+str)
        
    def debug(str):
        _out('[Debug]: '+str)