"""in this project we create a daily report that tracks the use of machines. which users are currently connected to which machines,
so the output should be the users that are currenly logged in"""

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date) # ordered chronologicly
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set() #we use set not list because it avoids duplicate entries and has efficient membrship testing which means it is faster
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
        if event.user in machines[event.machine]:#ensures that if a user logged out without logging in we have no errors
           machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0: #ensures that we dont print any machines when nobody is currently logged in 
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
users = current_users(events)
print(users)  #OUTPUT: {'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': set()}
generate_report(users) #OUTPUT: webserver.local: lane
