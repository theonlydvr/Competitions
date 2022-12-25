import math
def run_blueprint(costs,resources,generation,time):
    global geodes
    geodes = max(geodes, resources['g'])
    can_build_g = all(resources[e] > costs['g'][e] for e in costs['g'].keys())
    # If in the ideal case more geodes could be gathered than current best
    if resources['g']+generation['g']*time+sum(list(range(time)))>geodes:
        for bot in costs.keys():
            if (bot != 'g' and not can_build_g) or bot == 'g':
                if all(generation[e] > 0 for e in costs[bot].keys()): # Skip impossible tasks
                    time_req = [math.ceil((costs[bot][res]-resources[res])/generation[res]) for res in costs[bot].keys()]
                    build_time = max(0, max(time_req))
                    # Skip tasks that would take too log or not payoff
                    if build_time + 1 >= time or (bot =='r' and time-1-build_time <= costs[bot]['r']):
                        geodes = max(geodes, resources['g'] + time*generation['g'])
                    else:
                        new_resources = resources.copy()
                        for res in costs[bot].keys():
                            new_resources[res] -= costs[bot][res]
                        for res in generation.keys():
                            new_resources[res] += generation[res]*(build_time+1)
                        new_generation = generation.copy()
                        new_generation[bot] += 1
                        run_blueprint(costs,new_resources,new_generation,time-1-build_time)                
            
P1
total_quality = 0
num = 1
with open('input.txt', 'r') as f:
    for line in f:
        geodes = 0
        comps = line.split('.')
        costs = {}
        ore_line = comps[0].split(' ')
        costs['r'] = {'r': int(ore_line[-2])}
        clay_line = comps[1].split(' ')
        costs['c'] = {'r': int(clay_line[-2])}
        obsidian_line = comps[2].split(' ')
        costs['o'] = {'r': int(obsidian_line[-5]), 'c': int(obsidian_line[-2])}
        geode_line = comps[3].split(' ')
        costs['g'] = {'r': int(geode_line[-5]), 'o': int(geode_line[-2])}
        resources = {}
        resources['r'] = 0
        resources['c'] = 0
        resources['o'] = 0
        resources['g'] = 0
        run_blueprint(costs,resources,{'r':1,'c':0,'o':0,'g':0},24)
        total_quality += num*geodes
        num += 1

print(total_quality)

# P2
total_quality = 1
num = 0
with open('input.txt', 'r') as f:
    for line in f:
        geodes = 0
        comps = line.split('.')
        costs = {}
        ore_line = comps[0].split(' ')
        costs['r'] = {'r': int(ore_line[-2])}
        clay_line = comps[1].split(' ')
        costs['c'] = {'r': int(clay_line[-2])}
        obsidian_line = comps[2].split(' ')
        costs['o'] = {'r': int(obsidian_line[-5]), 'c': int(obsidian_line[-2])}
        geode_line = comps[3].split(' ')
        costs['g'] = {'r': int(geode_line[-5]), 'o': int(geode_line[-2])}
        resources = {}
        resources['r'] = 0
        resources['c'] = 0
        resources['o'] = 0
        resources['g'] = 0
        run_blueprint(costs,resources,{'r':1,'c':0,'o':0,'g':0},32)
        total_quality *= geodes
        num += 1
        if num == 3:
            break

print(total_quality)