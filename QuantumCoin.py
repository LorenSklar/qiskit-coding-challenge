
## MODULES
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit import BasicAer


## FUNCTIONS
def flip():
    # initialize a quantum register with a single bit
    q = QuantumRegister(1)

    # initialize a classical register with a single bit
    c = ClassicalRegister(1)
    
    # initialize a circuit acting on the single quantum bit
    circuit = QuantumCircuit(q, c)

    # randomize the bit using a Hadamard gate
    circuit.h(q[0])

    # measure the bit
    circuit.measure(q, c)

    # submit job to qasm simulator
    job = execute(circuit, BasicAer.get_backend('qasm_simulator'), shots=1)

    # determine output
    counts = job.result().get_counts()

    if track:
        print(counts)

    try:
        out = 0
        counts['0']
    except:
        out = 1

    return out
 

## MAIN
track = False
count_0 = 0
count_1 = 0
for i in range(0,100):
    bit = flip()
    if bit == 0:
        count_0 += 1
    else:
        count_1 += 1

print("0: " + str(count_0))
print("1: " + str(count_1))

