import sys
import re
from enum import IntEnum
from collections import deque


class Pulse(IntEnum):
    Low = 0
    High = 1
    
class System:
    def __init__(self):
        self.pulses = deque()
        self.sent = {Pulse.Low: 0, Pulse.High: 0}
        self.modules = dict()

    def add_module(self, mod, connections):
        if mod.startswith('%'):
            newmod = FlipFlop(mod[1:], connections, self)
        elif mod.startswith('&'):
            senders = [name
                       for name in self.modules
                       if mod[1:] in self.modules[name].connections]
            newmod = Conjunction(mod[1:], connections, self)
            newmod.recent = {name: Pulse.Low for name in senders}
        else:
            newmod = Broadcaster(mod, connections, self)
        self.modules[newmod.name] = newmod

        for mod in self.modules.values():
            if (isinstance(mod, Conjunction) and mod.name in newmod.connections):
                mod.recent[newmod.name] = Pulse.Low
        return newmod.name

    def send_pulse(self, pulse, receiver, sender):
        #if sender in('hn', 'fz', 'xf', 'mp', 'xn'):
        if sender in('jn', 'fb', 'gp', 'jl'):
            senders_data[sender][-1].append(int(pulse))
            #print(self.modules[sender].show_state(), pulse)
        self.pulses.append((pulse, receiver, sender))
        self.sent[pulse] += 1

    def try_turn_machine_on(self):
        self.send_pulse(Pulse.Low, 'broadcaster', None)
        while self.pulses:
            #print(self.show_state())
            #print('....................................')
            pulse, receiver, sender = self.pulses.popleft()
            if receiver == 'rx' and pulse == Pulse.Low:
                return True
            #print('{} -{}-> {}'.format(sender or 'button', pulse, receiver))
            if receiver in self.modules:
                self.modules[receiver].process_pulse(pulse, sender)
        return False

    def get_stats(self):
        return self.sent[Pulse.High] * self.sent[Pulse.Low]

    def show_state(self):
        return(
            '\n'.join([m.show_state() for m in self.modules.values()] + [str(x) for x in [self.pulses, self.sent]]))
        
    
button = System()


class Module:
    def __init__(self, name, connections, system):
        self.name = name
        self.connections = connections
        self.system = system

    def process_pulse(self, pulse, sender):
        newpulse = self.transform_pulse(pulse, sender)
        for c in self.connections:
            self.system.send_pulse(newpulse, c, self.name)

    def transform_pulse(self, pulse, sender):
        return pulse

    def show_state(self):
        return self.name


class Broadcaster(Module):
    pass


class FlipFlop(Module):
    def __init__(self, name, connections, system):
        super().__init__(name, connections, system)
        self.on = False

    def process_pulse(self, pulse, sender):
        if pulse == Pulse.High: return
        self.on = not self.on
        super().process_pulse(pulse, sender)
        
    def transform_pulse(self, pulse, sender):
        return Pulse.High if self.on else Pulse.Low

    def show_state(self):
         return('{}: {}'.format(self.name, self.on))

    
class Conjunction(Module):
    def __init__(self, name, connections, system):
        super().__init__(name, connections, system)
        self.recent = {}

    def process_pulse(self, pulse, sender):
        self.recent[sender] = pulse
        super().process_pulse(pulse, sender)
        
    def transform_pulse(self, pulse, sender):
        return Pulse.Low if all([p == Pulse.High for p in self.recent.values()]) else Pulse.High

    def get_recent_str(self):
        return ''.join([str(int(v)) for v in self.recent.values()])
        
    
    def show_state(self):
        return('{}: {}'.format(self.name, self.get_recent_str()))


f = open('graph.dot', 'w')
f.write('digraph {\n')
    
for line in sys.stdin:
    mod, conn_str = line.strip().split(' -> ')
    name = button.add_module(mod, conn_str.split(', '))
    color = ' color=red' if mod.startswith('&') else ''
    f.write('\t{} [label="{}"{}]\n'.format(name, mod, color))
    for c in conn_str.split(', '):
        f.write('\t{} -> {}\n'.format(name, c))
    button.add_module(mod, conn_str.split(', '))

f.write('}\n')
f.close()
    
# presses = 0
# machine_on = False
# while not machine_on:
#     presses += 1
#     machine_on = button.try_turn_machine_on()
senders = ('jn', 'fb', 'gp', 'jl')
senders_data = {name: [] for name in senders}
for i in range(10000):
    for s in senders_data:
        senders_data[s].append([])
    button.try_turn_machine_on()

    #print('------------------------', i)

# print(presses)

for s in senders:
    print('{}:-----------------------'.format(s))
    for step, d in enumerate(senders_data[s]):
        if 0 in d:
            print(step + 1, d)

