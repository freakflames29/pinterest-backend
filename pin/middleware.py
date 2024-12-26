import time
class DelayMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,rq):
        response = self.get_response(rq)
        time.sleep(0)
        return response
        
        