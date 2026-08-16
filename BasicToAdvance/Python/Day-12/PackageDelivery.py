packages = [4,6,7,8,9]
days = 3

def can_do(packages , capacity, days):
    used_days = 1
    current_weight = 0
    for package in packages:
        if current_weight + package <= capacity:
            current_weight += package
        else:
            used_days += 1
            current_weight = package
    return used_days <= days

def ship_within(packages , days):
    low = max(packages)
    high = sum(packages)
    answer = high

    while low <= high:
        mid = (low + high)//2
        if can_do(packages , mid ,days):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

x = ship_within(packages,days)
print(x)