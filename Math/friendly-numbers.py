def friendly_number(number, base=1000, decimals=0, powers=[], suffic=''):
    # powers = powers or ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    powers = powers or ['', 'k', 'M']
    nums = [1, 1000, 1000000]
    for n, power in zip(nums, powers):
        print(number / n)
    return str(number)


friendly_number(255000000000)
assert friendly_number(10240) == '10k'
assert friendly_number(12341234, decimals=1) == '12.3M'
assert friendly_number(12000000, decimals=3) == '12.000M'
assert friendly_number(12461, decimals=1) == '12.5k'
assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB'
assert friendly_number(-150, base=100, powers=['', 'd', 'D']) == '-1d'
assert friendly_number(-155, base=100, decimals=1, powers=['', 'd', 'D']) == '-1.6d'
assert friendly_number(255000000000, powers=['', 'k', 'M']) == '255000M'

