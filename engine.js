// Soundbar Math engine - hypothetical arithmetic on labeled norms only.
// Peak-to-RMS ratios, room classes and decibel steps are labeled norms,
// not measurements of your soundbar, your room or your ears.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }
function article(n) { const s = String(n); return (s.startsWith("8") || s.startsWith("11") || s.startsWith("18")) ? "An" : "A"; }

function peakTruth(peak) {
  if (!(peak > 0)) throw new Error("the peak watts must be above zero");
  const rms = peak / 10; // labeled norm: honest RMS runs about a tenth of the peak figure
  return `${article(peak)} ${peak}-watt peak on the box is ${fixed1(rms)} watts RMS honestly.`;
}

function doubleTruth(a, b) {
  if (!(a > 0)) throw new Error("the first watts must be above zero");
  if (!(b > 0)) throw new Error("the second watts must be above zero");
  const db = 10 * Math.log10(b / a);
  if (db === 0) return `${a} watts against ${a} is the same loudness honestly.`;
  const absR = tenths(Math.abs(db)); // rounded figure the verdict judges
  let verdict;
  if (absR <= 3) verdict = "barely audible";
  else if (absR < 10) verdict = "a clear step";
  else verdict = "about twice as loud";
  const direction = db > 0 ? "buys" : "loses";
  return `${b} watts against ${a} ${direction} ${fixed1(absR)} dB honestly - ${verdict}.`;
}

function roomTruth(sqft, rms) {
  if (!(sqft > 0)) throw new Error("the room size must be above zero");
  if (!(rms > 0)) throw new Error("the RMS watts must be above zero");
  let cls, clsWatts;
  if (sqft < 150) { cls = "small"; clsWatts = 20; }
  else if (sqft < 300) { cls = "medium"; clsWatts = 50; }
  else { cls = "large"; clsWatts = 100; }
  const margin = rms - clsWatts;
  let verdict;
  if (margin < 0) verdict = `runs ${fixed1(-margin)} watts short honestly`;
  else if (margin > 0) verdict = `has ${fixed1(margin)} watts to spare honestly`;
  else verdict = "meets the class exactly honestly";
  return `${article(sqft)} ${sqft}-square-foot room asks the ${cls} ${clsWatts}-watt class; ${fixed1(rms)} honest watts ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { peakTruth, doubleTruth, roomTruth };
}
