#!/usr/bin/env python3
import re


def first(program):
    class Step:
        pass

    diagnostic = None
    curr_state = None
    states = {}
    state = None
    step = None
    for line in program.split("\n"):
        line = line.strip()
        if not line:
            continue

        match = re.match("Begin in state (\w+)\.", line)
        if match is not None:
            curr_state = match.group(1)

        match = re.match("Perform a diagnostic checksum after (\d+) steps\.", line)
        if match is not None:
            diagnostic = int(match.group(1))

        match = re.match("In state (\w+):", line)
        if match is not None:
            state = {}
            states[match.group(1)] = state

        match = re.match("If the current value is ([01]):", line)
        if match is not None:
            step = Step()
            state[int(match.group(1))] = step

        match = re.match("- Write the value ([01])\.", line)
        if match is not None:
            step.value = int(match.group(1))

        match = re.match("- Move one slot to the (left|right)\.", line)
        if match is not None:
            step.direction = match.group(1)

        match = re.match("- Continue with state (\w+)\.", line)
        if match is not None:
            step.to = match.group(1)

    if diagnostic is None or curr_state is None or not states:
        return None

    tape = [0 for x in range(10)]
    position = 5
    for i in range(diagnostic):
        state = states[curr_state]
        step = state[tape[position]]

        tape[position] = step.value

        if step.direction == 'right':
            position += 1
            if position >= len(tape):
                tape += [0 for x in range(10)]
        if step.direction == 'left':
            position -= 1
            if position < 0:
                tape = [0 for x in range(10)] + tape
                position += 10

        curr_state = step.to

    return tape.count(1)


if __name__ == '__main__':
    data = """
Begin in state A.
Perform a diagnostic checksum after 12586542 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state B.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state A.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state F.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state D.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
"""

    res = first(data)
    print(">>> %s" % res)
