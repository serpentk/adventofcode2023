import sys
import re
from enum import Enum
from collections import deque


class Pulse(Enum):
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

    def send_pulse(self, pulse, receiver, sender):
        self.pulses.append((pulse, receiver, sender))
        self.sent[pulse] += 1

    def push_button(self):
        self.send_pulse(Pulse.Low, 'broadcaster', None)
        while self.pulses:
            pulse, receiver, sender = self.pulses.popleft()
            if receiver in self.modules:
                self.modules[receiver].process_pulse(pulse, sender)

    def get_stats(self):
        return self.sent[Pulse.High] * self.sent[Pulse.Low]


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

    
class Conjunction(Module):
    def __init__(self, name, connections, system):
        super().__init__(name, connections, system)
        self.recent = {}

    def process_pulse(self, pulse, sender):
        self.recent[sender] = pulse
        super().process_pulse(pulse, sender)
        
    def transform_pulse(self, pulse, sender):
        return Pulse.Low if all([p == Pulse.High for p in self.recent.values()]) else Pulse.High


for line in sys.stdin:
    mod, conn_str = line.strip().split(' -> ')
    button.add_module(mod, conn_str.split(', '))

for i in range(1000):
    button.push_button()

print(button.get_stats())
