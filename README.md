universalbus
===========
  Публикация события
  ```
  from universalbus import EventSender
  sender = EventSender('guest', 'guest', 'localhost', '/', exchange='my_exchange')
  sender.push('kernel.critical', {'event_id': 13})
  ```

  Реакция на события
  ```
  from universalbus import EventListener
  sender = EventSender('guest', 'guest', 'localhost', '/', exchange='my_exchange')
  listener = EventListener('guest', 'guest', 'localhost', '/', exchange='my_exchange', queue='events', ['kernel.*', '*.critical'])

  def callback(chanel, method, properties, body):
    print method.routing_key, body

  listener.register_callback(callback)
  ```
