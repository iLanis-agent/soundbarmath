import math, json

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def article(n):
    s = str(n)
    return "An" if (s.startswith("8") or s.startswith("11") or s.startswith("18")) else "A"

def peak_truth(peak):
    if not (peak > 0):
        raise ValueError("the peak watts must be above zero")
    rms = peak / 10
    return f"{article(peak)} {peak}-watt peak on the box is {fixed1(rms)} watts RMS honestly."

def double_truth(a, b):
    if not (a > 0):
        raise ValueError("the first watts must be above zero")
    if not (b > 0):
        raise ValueError("the second watts must be above zero")
    db = 10 * math.log10(b / a)
    if db == 0:
        return f"{a} watts against {a} is the same loudness honestly."
    abs_r = tenths(abs(db))
    if abs_r <= 3:
        verdict = "barely audible"
    elif abs_r < 10:
        verdict = "a clear step"
    else:
        verdict = "about twice as loud"
    direction = "buys" if db > 0 else "loses"
    return f"{b} watts against {a} {direction} {fixed1(abs_r)} dB honestly - {verdict}."

def room_truth(sqft, rms):
    if not (sqft > 0):
        raise ValueError("the room size must be above zero")
    if not (rms > 0):
        raise ValueError("the RMS watts must be above zero")
    if sqft < 150:
        cls, cls_watts = "small", 20
    elif sqft < 300:
        cls, cls_watts = "medium", 50
    else:
        cls, cls_watts = "large", 100
    margin = rms - cls_watts
    if margin < 0:
        verdict = f"runs {fixed1(-margin)} watts short honestly"
    elif margin > 0:
        verdict = f"has {fixed1(margin)} watts to spare honestly"
    else:
        verdict = "meets the class exactly honestly"
    return f"{article(sqft)} {sqft}-square-foot room asks the {cls} {cls_watts}-watt class; {fixed1(rms)} honest watts {verdict}."

FNS = {"peakTruth": peak_truth, "doubleTruth": double_truth, "roomTruth": room_truth}

CASES = [
    ("peakTruth", [300]),
    ("peakTruth", [1000]),
    ("peakTruth", [50]),
    ("peakTruth", [1]),
    ("peakTruth", [800]),
    ("peakTruth", [0]),
    ("peakTruth", [-5]),
    ("doubleTruth", [300, 600]),
    ("doubleTruth", [300, 3000]),
    ("doubleTruth", [100, 400]),
    ("doubleTruth", [300, 150]),
    ("doubleTruth", [200, 200]),
    ("doubleTruth", [50, 500]),
    ("doubleTruth", [30, 240]),
    ("doubleTruth", [0, 600]),
    ("doubleTruth", [300, 0]),
    ("roomTruth", [250, 50]),
    ("roomTruth", [120, 30]),
    ("roomTruth", [400, 30]),
    ("roomTruth", [200, 60]),
    ("roomTruth", [150, 20]),
    ("roomTruth", [80, 20]),
    ("roomTruth", [600, 150]),
    ("roomTruth", [0, 50]),
    ("roomTruth", [250, 0]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written")
