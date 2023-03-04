def acc_seq(seq):
    n = len(seq)
    acc = 0
    result = [0]
    for i in range(n):
        acc += seq[i]
        result.append(acc)
    return result

def solution(sequence):
    N = len(sequence)
    pulse = [(-1) ** i for i in range(N)]
    pulse_seq = [sequence[i] * pulse[i] for i in range(N)]
    pulse_acc = acc_seq(pulse_seq)
    return max(pulse_acc) - min(pulse_acc)