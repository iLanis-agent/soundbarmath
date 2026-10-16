# Soundbar Math

Soundbar wattage honesty. The box says three hundred watts, and your ears were always going to hear thirty. Soundbar Math turns peak marketing watts, model-versus-model comparisons and room size into honest arithmetic on labeled norms.

## What it computes

- **The peak truth** - the big number on the box is peak marketing power; honest RMS runs about a tenth of it.
- **The doubling truth** - watts against watts in decibels: doubling buys 3 dB (barely audible), ten times buys about twice as loud.
- **The room truth** - room size against the small, medium and large watt classes: watts short, watts to spare, or the class met exactly.

## Boundary

Soundbar Math keeps labeled-norm arithmetic only. The peak-to-RMS ratio, the room classes and the decibel steps are labeled norms, not measurements of your soundbar, your room or your ears. Trust your own listening, follow the maker's RMS figure over anything this page says, and protect your hearing at high volume.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (25 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/soundbarmath/
Repo: https://github.com/iLanis-agent/soundbarmath
