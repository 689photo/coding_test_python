def solution(n, wires):
    need_check = []
    new_wires = []
    cut_wire = []
    result = []
    
    for i in range(n-1):
        i = 0
        cut_wire.append(wires.pop(i))
        need_check.extend(wires[0])
        
        while need_check:
            w = need_check.pop()
            new_wires.append(w)
            for wire in wires:
                if w in wire:
                    for m in wire:
                        if m not in new_wires:
                            need_check.append(m)
        result.append(abs((n - len(set(new_wires))) - len(set(new_wires))))
        new_wires = []            
        wires.append(cut_wire.pop())
    
    return min(result)