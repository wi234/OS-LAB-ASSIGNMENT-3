def fifo(pages, frames):
    frame = []
    faults = 0
    for p in pages:
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                frame.pop(0)
                frame.append(p)
            faults += 1
    return faults


def lru(pages, frames):
    frame = []
    faults = 0
    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < frames:
                frame.append(pages[i])
            else:
                lru_index = min(range(len(frame)), key=lambda x: pages[:i][::-1].index(frame[x]) if frame[x] in pages[:i] else float('inf'))
                frame[lru_index] = pages[i]
            faults += 1
    return faults


def optimal(pages, frames):
    frame = []
    faults = 0
    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < frames:
                frame.append(pages[i])
            else:
                future = []
                for f in frame:
                    if f in pages[i+1:]:
                        future.append(pages[i+1:].index(f))
                    else:
                        future.append(float('inf'))
                frame[future.index(max(future))] = pages[i]
            faults += 1
    return faults


def mru(pages, frames):
    frame = []
    faults = 0
    recent = []
    for p in pages:
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                frame.remove(recent[-1])
                frame.append(p)
            faults += 1
        if p in recent:
            recent.remove(p)
        recent.append(p)
    return faults


def second_chance(pages, frames):
    frame = []
    ref = []
    faults = 0
    pointer = 0

    for p in pages:
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
                ref.append(0)
            else:
                while ref[pointer] == 1:
                    ref[pointer] = 0
                    pointer = (pointer + 1) % frames
                frame[pointer] = p
                ref[pointer] = 0
                pointer = (pointer + 1) % frames
            faults += 1
        else:
            ref[frame.index(p)] = 1
    return faults


# Example Run
pages = list(map(int, input("Enter pages: ").split()))
frames = int(input("Enter frames: "))

print("FIFO Faults:", fifo(pages, frames))
print("LRU Faults:", lru(pages, frames))
print("Optimal Faults:", optimal(pages, frames))
print("MRU Faults:", mru(pages, frames))
print("Second Chance Faults:", second_chance(pages, frames))
