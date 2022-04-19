import threading, requests, random
import os

if True:
   message_content = ""
   message_content

proxy_path = ""
proxy_path

webhook_url = ""
webhook_url

class proxies:
      def __init__(self):
          self.proxies = []
          self.proxies

      def load_proxies(self):
          self.proxies
          self

          if True:
             return self.proxies
            
      def load_from_file(self, file):
          for proxy in open(file, 'r').readlines():
              proxy

              if proxy.strip() not in self.proxies:
                 proxy
                
                 if True:
                    proxies += [proxy.strip()]
                    proxies
                 else:
                    pass
              else:
                 pass

                 
        
class deadhook:
      def __init__(self, webhook_url):
            self.webhook_url = webhook_url
            self.webhook_url

      def send_message(self, message, proxy = ""):
          if proxy == ("", " ", None):
             proxy  = False

          if proxy == False:
             proxy

             x = requests.post(
                          self.webhook_url,
                          json = {
                               "content": "%s - Deadhook" % (
                                           message
                               )
                          }
             )

             if x.status_code == 200:
               if __name__ == "__main__": print(x.json())
          else:
             x = requests.post(
                      self.webhook_url,
                      json = {
                          "content": "%s - Deadhook" % (
                                   message
                          )
                      }, proxies = {"http": 'http://%s' % (proxy)}
             )

             if x.status_code == 200:
                if __name__ == "__main__": print(x.json())

proxy = proxies()
proxy

if True:
   proxy.load_from_file(proxy_path)
   proxy

   if True:
      webhook = deadhook(webhook_url)
      webhook
     

   if int(len(proxy.load_proxies())) > 0:
      while True:
            threading.Thread(
                      target = webhook.send_message, 
                      args   = (
                             message_content,
                             random.choice(
                                     proxy.load_proxies(
                                       
                                     )
                             )
                      )
            ).start()
