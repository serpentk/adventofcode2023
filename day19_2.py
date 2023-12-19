import sys
import re
import math
from operator import gt, lt

rule_re = re.compile(r'([a-z]+)\{(.+)\}')
condition_re = re.compile(r'([xmas])([<>])(\d+):([a-zA-Z]+)')
part_keys = ('x', 'm', 'a', 's')

rules = {
    'R': lambda x: iter((0,)),
    'A': lambda x: iter((math.prod(
        [x[key][1] - x[key][0] + 1 for key in part_keys]),))                       
}

def split_part(part, op, key, value):
    oper = gt if op == '>' else lt
    if oper(part[key][0], value) and oper(part[key][1], value):
        return part, None
    elif op == '<' and part[key][0] < value:
        newpart = part.copy()
        newpart.update({key: (part[key][0], value - 1)})
        part.update({key: (value, part[key][1])})
        return newpart, part
    elif op == '>' and part[key][1] > value:
        newpart = part.copy()
        newpart.update({key: (value + 1, part[key][1])})
        part.update({key: (part[key][0], value)})
        return newpart, part
    return None, part
    
def process_rule(rule_str):
    name, instructions = rule_re.match(rule_str).groups()
    instructions = instructions.split(',')
    def f(part):
        for step in instructions:
            if not part:
                return
            cond = re.match(condition_re, step)
            if cond:
                key, op, val, newrule = cond.groups()
                newpart, part = split_part(part, op, key, int(val))
                if newpart:
                    for p in rules[newrule](newpart):
                        yield p
            else:
                for p in rules[step](part):
                    yield p
    return name, f


for line in sys.stdin:
    rule_str = line.strip()
    if not rule_str: break
    name, rule = process_rule(rule_str)
    rules[name] = rule

s = sum(rules['in']({k: (1, 4000) for k in part_keys}))

print(s)
