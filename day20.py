#credit: hyper neutrino
from collections import deque

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}
    def __repr__(self):
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
broadcast_targets = []

for line in open('input20.txt'):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = outputs
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "lo"
#part 2!!
(feed,) = [name for name, module in modules.items() if "rx" in module.outputs]

cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

presses = 0
#end of part 2 segment

lo = hi = 0

for _ in range(1000):
    lo += 1
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
    
    while q:
        origin, target, pulse = q.popleft()

        if pulse == "lo":
            lo += 1
        else:
            hi += 1
        
        if target not in modules:
            continue
        #pt 2 seg
        module = modules[target]
        if module.name == feed and pulse == "hi":
          seen[origin] += 1

          if origin not in cycle_lengths:
              cycle_lengths[origin] = presses
          else:
              assert presses == seen[origin] * cycle_lengths[origin]
              
          if all(seen.values()):
              x = 1
              for cycle_length in cycle_lengths.values():
                  x = x * cycle_length // math.gcd(x, cycle_length)
              print(x)
              exit(0)
        #end p2 seg
        if module.type == "%":
            if pulse == "lo":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "hi" if module.memory == "on" else "lo"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
            for x in module.outputs:
                q.append((module.name, x, outgoing))
#print(lo * hi)