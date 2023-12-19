import sys
import re

part_re = re.compile(r'\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}')
rule_re = re.compile(r'([a-z]+)\{(.+)\}')
condition_re = re.compile(r'([xmas])([<>])(\d+):([a-zA-Z]+)')

rules = {
    'R': lambda x: 0,
    'A': lambda x: x['x'] + x['m'] + x['a'] + x['s']
}

def process_rule(rule_str):
    name, instructions = rule_re.match(rule_str).groups()
    instructions = instructions.split(',')
    def f(part):
        for step in instructions:
            cond = re.match(condition_re, step)
            if cond:
                key, op, val, newrule = cond.groups()
                c = (part[key] > int(val)) if op == '>' else (part[key] < int(val))
                if c:
                    return rules[newrule](part)
            else:
                return rules[step](part)
        return 0
    return name, f

def process_part(part_str):
    x, m, a, s = part_re.match(part_str).groups()
    return {'x': int(x), 'm': int(m), 'a': int(a), 's': int(s)}

for line in sys.stdin:
    rule_str = line.strip()
    if not rule_str: break
    name, rule = process_rule(rule_str)
    rules[name] = rule

s = 0
for line in sys.stdin:
    part = process_part(line)
    s += rules['in'](part)

print(s)
