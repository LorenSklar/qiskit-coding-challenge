## TO DO
# implement quantum tie breaker
# how do I renormalize?


## MODULES
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute

## FUNCTIONS
def shuffle(n=52):
    # |0> represents absent, |1> represents present
    return [1 for i in range(n)]

def deal(cards):
    # how many cards in this deck?
    n = len(cards)
    
    # initialize an n bit quantum register
    q = QuantumRegister(n)

    # initialize an n bit classical register
    c = ClassicalRegister(n)
    
    # initialize a circuit using the quantum and classical registers
    circuit = QuantumCircuit(q, c)

    for i in range(n):
        if cards[i] == 1:
            # if card is in the deck, randomize the bit
            circuit.h(q[i])
        else:
            # else card remains |0>
            pass
       
    # measure the bits
    for i in range(n):
        circuit.measure(q[i], c[i])

    # submit job
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=128)
    result = job.result()
    count = result.get_counts()

    # how many times did each card change from present |1> to absent |0>?
    c = [0 for i in range(n)]
    for a in count.keys():
        for i in range(n):
            if a[i] == '0' and cards[i] == 1:
                c[i] += count[a]

    if track:
        print ("Counts: " + str(c))

    # which card was removed most often?
    a = []
    high = 0
    for i in range(n):
        if c[i] > high:
            high = c[i]
    for i in range(n):
        if c[i] == high:
            a += [i]

    if track:
        print ("Position of highest count(s): " + str(a))

    # quantum tie breaker
    x = a[0]

    # remove card from deck
    cards[x] = 0
               
    return x, cards


## MAIN
track = True
n = 13

# shuffle
cards = shuffle(n)
print("Deck: " + str(cards))

# deal
x, cards = deal(cards)
print("Card: " + str(x))
print("Deck: " + str(cards))

