#credit completely to hyper neutrino

cache = {}

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1
    
    key = (cfg, nums)
    
    if key in cache:
        return cache[key]

    result = 0
    
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
        
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result

total = 0

for line in open('input12.txt'):
    cfg, nums = line.split()
    #for part 2
    cfg = (cfg + "?")*5
    nums = ("," + nums) * 5
    nums = nums[1:]
    cfg = cfg[0:-1]
    #end of part two changes
    nums = tuple(map(int, nums.split(",")))
    total += count(cfg, nums)

print(total)