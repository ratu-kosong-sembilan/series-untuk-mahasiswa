const rSlider = document.getElementById("r");
const lSlider = document.getElementById("l");
const cSlider = document.getElementById("c");
const vSlider = document.getElementById("v");
const preset = document.getElementById("preset");
const model = document.getElementById("model");
const inputMode = document.getElementById("inputMode");
const customName = document.getElementById("customName");
const savePresetBtn = document.getElementById("savePreset");
const deletePresetBtn = document.getElementById("deletePreset");

const rVal = document.getElementById("rVal");
const lVal = document.getElementById("lVal");
const cVal = document.getElementById("cVal");
const vVal = document.getElementById("vVal");

const runBtn = document.getElementById("run");
const pauseBtn = document.getElementById("pause");
const resetBtn = document.getElementById("reset");
const exportBtn = document.getElementById("exportCsv");
const statusEl = document.getElementById("status");

const showDidt = document.getElementById("showDidt");
const showIntegral = document.getElementById("showIntegral");
const cardDidt = document.getElementById("cardDidt");
const cardInt = document.getElementById("cardInt");

const chartI = document.getElementById("chartI");
const chartV = document.getElementById("chartV");
const chartDidt = document.getElementById("chartDidt");
const chartInt = document.getElementById("chartInt");

const legendI = document.getElementById("legendI");
const legendV = document.getElementById("legendV");
const legendDidt = document.getElementById("legendDidt");
const legendInt = document.getElementById("legendInt");

const tipI = document.getElementById("tipI");
const tipV = document.getElementById("tipV");
const tipDidt = document.getElementById("tipDidt");
const tipInt = document.getElementById("tipInt");

const crossI = document.getElementById("crossI");
const crossV = document.getElementById("crossV");
const crossDidt = document.getElementById("crossDidt");
const crossInt = document.getElementById("crossInt");

const ctxI = chartI.getContext("2d");
const ctxV = chartV.getContext("2d");
const ctxDidt = chartDidt.getContext("2d");
const ctxInt = chartInt.getContext("2d");

let timer = null;
let t = 0;
let dt = 0.002; // 2 ms
let duration = 2; // 2 seconds window

let i = 0;
let vCap = 0;
let integralI = 0;

const dataI = [];
const dataV = [];
const dataDidt = [];
const dataInt = [];
const timeAxis = [];

function updateLabels() {
  rVal.textContent = rSlider.value;
  lVal.textContent = lSlider.value;
  cVal.textContent = cSlider.value;
  vVal.textContent = vSlider.value;
}

function saveState() {
  const state = {
    model: model.value,
    preset: preset.value,
    inputMode: inputMode.value,
    r: rSlider.value,
    l: lSlider.value,
    c: cSlider.value,
    v: vSlider.value,
    customName: customName.value,
  };
  localStorage.setItem("simulasiState", JSON.stringify(state));
}

function loadState() {
  const raw = localStorage.getItem("simulasiState");
  if (!raw) return;
  try {
    const state = JSON.parse(raw);
    if (state.model) model.value = state.model;
    if (state.preset) preset.value = state.preset;
    if (state.inputMode) inputMode.value = state.inputMode;
    if (state.r) rSlider.value = state.r;
    if (state.l) lSlider.value = state.l;
    if (state.c) cSlider.value = state.c;
    if (state.v) vSlider.value = state.v;
    if (state.customName) customName.value = state.customName;
  } catch {
    // ignore corrupted state
  }
}

function updateModelUI() {
  const m = model.value;
  if (m === "rl") {
    lSlider.disabled = false;
    cSlider.disabled = true;
  } else if (m === "rc") {
    lSlider.disabled = true;
    cSlider.disabled = false;
  } else {
    lSlider.disabled = false;
    cSlider.disabled = false;
  }
}

function ensureCustomOption(name) {
  const value = `custom:${name}`;
  const exists = Array.from(preset.options).some((opt) => opt.value === value);
  if (exists) return;
  const opt = document.createElement("option");
  opt.value = value;
  opt.textContent = `Custom: ${name}`;
  preset.appendChild(opt);
}

function removeCustomOption(name) {
  const value = `custom:${name}`;
  Array.from(preset.options).forEach((opt) => {
    if (opt.value === value) {
      opt.remove();
    }
  });
}

function loadCustomPresets() {
  Object.keys(localStorage)
    .filter((key) => key.startsWith("preset_"))
    .forEach((key) => {
      const raw = localStorage.getItem(key);
      if (!raw) return;
      try {
        const payload = JSON.parse(raw);
        if (payload && payload.name) ensureCustomOption(payload.name);
      } catch {
        // ignore bad preset
      }
    });
}

function applyPreset(value) {
  if (value === "motor") {
    model.value = "rl";
    rSlider.value = 5;
    lSlider.value = 0.2;
    cSlider.value = 0.0002;
    vSlider.value = 220;
  } else if (value === "cap") {
    model.value = "rc";
    rSlider.value = 20;
    lSlider.value = 0.02;
    cSlider.value = 0.005;
    vSlider.value = 220;
  } else if (value === "fast") {
    model.value = "rl";
    rSlider.value = 1;
    lSlider.value = 0.01;
    cSlider.value = 0.0005;
    vSlider.value = 110;
  } else if (value.startsWith("custom:")) {
    const name = value.replace("custom:", "");
    const raw = localStorage.getItem(`preset_${name}`);
    if (raw) {
      try {
        const payload = JSON.parse(raw);
        if (payload.model) model.value = payload.model;
        if (payload.inputMode) inputMode.value = payload.inputMode;
        if (payload.r) rSlider.value = payload.r;
        if (payload.l) lSlider.value = payload.l;
        if (payload.c) cSlider.value = payload.c;
        if (payload.v) vSlider.value = payload.v;
      } catch {
        // ignore bad preset
      }
    }
  }
  updateLabels();
  updateModelUI();
  resetSim();
  saveState();
}

function resetSim() {
  t = 0;
  i = 0;
  vCap = 0;
  integralI = 0;
  dataI.length = 0;
  dataV.length = 0;
  dataDidt.length = 0;
  dataInt.length = 0;
  timeAxis.length = 0;
  drawAll();
  statusEl.textContent = "Siap";
}

function lastValue(arr) {
  if (arr.length === 0) return 0;
  return arr[arr.length - 1];
}

function updateLegendValues() {
  legendI.textContent = lastValue(dataI).toFixed(3);
  legendV.textContent = lastValue(dataV).toFixed(3);
  legendDidt.textContent = lastValue(dataDidt).toFixed(3);
  legendInt.textContent = lastValue(dataInt).toFixed(3);
}

function stepSim() {
  const R = parseFloat(rSlider.value);
  const L = parseFloat(lSlider.value);
  const C = parseFloat(cSlider.value);
  const V = parseFloat(vSlider.value);
  const input =
    inputMode.value === "impulse" ? (t <= dt ? V / dt : 0) : V;
  const safeInput = Math.min(input, V * 50);

  let didt = 0;
  let vOut = 0;

  if (model.value === "rl") {
    // RL series: di/dt = (V - R*i) / L
    const f = (iState) => (safeInput - R * iState) / L;
    const k1 = f(i);
    const k2 = f(i + 0.5 * dt * k1);
    const k3 = f(i + 0.5 * dt * k2);
    const k4 = f(i + dt * k3);
    i = i + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
    didt = f(i);
    vOut = safeInput - R * i;
  } else if (model.value === "rc") {
    // RC series: dv/dt = (V - vC) / (R*C)
    const f = (vState) => (safeInput - vState) / (R * C);
    const k1 = f(vCap);
    const k2 = f(vCap + 0.5 * dt * k1);
    const k3 = f(vCap + 0.5 * dt * k2);
    const k4 = f(vCap + dt * k3);
    vCap = vCap + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4);
    i = (safeInput - vCap) / R;
    didt = -(1 / R) * f(vCap);
    vOut = vCap;
  } else {
    // RLC series: di/dt = (V - R*i - vC) / L, dv/dt = i / C
    const fI = (iState, vState) => (safeInput - R * iState - vState) / L;
    const fV = (iState) => iState / C;
    const k1i = fI(i, vCap);
    const k1v = fV(i);
    const k2i = fI(i + 0.5 * dt * k1i, vCap + 0.5 * dt * k1v);
    const k2v = fV(i + 0.5 * dt * k1i);
    const k3i = fI(i + 0.5 * dt * k2i, vCap + 0.5 * dt * k2v);
    const k3v = fV(i + 0.5 * dt * k2i);
    const k4i = fI(i + dt * k3i, vCap + dt * k3v);
    const k4v = fV(i + dt * k3i);
    i = i + (dt / 6) * (k1i + 2 * k2i + 2 * k3i + k4i);
    vCap = vCap + (dt / 6) * (k1v + 2 * k2v + 2 * k3v + k4v);
    didt = fI(i, vCap);
    vOut = vCap;
  }

  integralI += i * dt;

  dataI.push(i);
  dataV.push(vOut);
  dataDidt.push(didt);
  dataInt.push(integralI);
  timeAxis.push(t);

  t += dt;
  if (t >= duration) {
    pauseSim();
    statusEl.textContent = "Selesai";
  }
}

function maxAbs(data) {
  return Math.max(...data.map((v) => Math.abs(v))) || 1;
}

function robustMax(data) {
  if (data.length < 10) return maxAbs(data);
  const abs = data.map((v) => Math.abs(v)).sort((a, b) => a - b);
  const idx = Math.floor(abs.length * 0.98);
  return abs[idx] || 1;
}

function runSim() {
  if (timer) return;
  statusEl.textContent = "Running";
  timer = setInterval(() => {
    stepSim();
    drawAll();
  }, 16);
}

function pauseSim() {
  if (timer) {
    clearInterval(timer);
    timer = null;
    statusEl.textContent = "Jeda";
  }
}

function drawGrid(ctx, w, h) {
  ctx.clearRect(0, 0, w, h);
  ctx.strokeStyle = "#f3f3f3";
  ctx.lineWidth = 1;
  for (let x = 0; x < w; x += 25) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, h);
    ctx.stroke();
  }
  for (let y = 0; y < h; y += 20) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(w, y);
    ctx.stroke();
  }

  ctx.strokeStyle = "#e0e0e0";
  ctx.lineWidth = 1.2;
  for (let x = 0; x < w; x += 50) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, h);
    ctx.stroke();
  }
  for (let y = 0; y < h; y += 40) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(w, y);
    ctx.stroke();
  }
}

function drawAxes(ctx, w, h, maxVal, unit) {
  ctx.fillStyle = "#9aa0a6";
  ctx.font = "11px Segoe UI, Tahoma, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "top";

  const ticks = 4;
  for (let iTick = 0; iTick <= ticks; iTick++) {
    const x = 10 + ((w - 20) * iTick) / ticks;
    const tLabel = ((duration * iTick) / ticks).toFixed(2);
    ctx.fillText(`${tLabel}s`, x, h - 16);
  }

  ctx.textAlign = "right";
  ctx.textBaseline = "middle";
  for (let iTick = 0; iTick <= ticks; iTick++) {
    const y = h / 2 - (h * 0.4 * (iTick - ticks / 2)) / (ticks / 2);
    const val = ((maxVal * (ticks / 2 - iTick)) / (ticks / 2)).toFixed(2);
    ctx.fillText(`${val} ${unit}`, 46, y);
  }
}

function drawLine(ctx, data, color, unit) {
  const w = ctx.canvas.width;
  const h = ctx.canvas.height;
  drawGrid(ctx, w, h);

  if (data.length < 2) return;

  const maxVal = robustMax(data);
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;
  ctx.beginPath();
  data.forEach((val, idx) => {
    const x = (idx / (data.length - 1)) * (w - 20) + 10;
    const y = h / 2 - (val / maxVal) * (h * 0.4);
    if (idx === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();

  ctx.strokeStyle = "#bbb";
  ctx.beginPath();
  ctx.moveTo(0, h / 2);
  ctx.lineTo(w, h / 2);
  ctx.stroke();

  drawAxes(ctx, w, h, maxVal, unit);
}

function drawAll() {
  drawLine(ctxI, dataI, "#e53935", "A");
  drawLine(ctxV, dataV, "#1e88e5", "V");
  drawLine(ctxDidt, dataDidt, "#fb8c00", "A/s");
  drawLine(ctxInt, dataInt, "#43a047", "C");
  updateLegendValues();
}

rSlider.addEventListener("input", updateLabels);
lSlider.addEventListener("input", updateLabels);
cSlider.addEventListener("input", updateLabels);
vSlider.addEventListener("input", updateLabels);
[
  rSlider,
  lSlider,
  cSlider,
  vSlider,
  model,
  preset,
  inputMode,
].forEach((el) => el.addEventListener("change", saveState));
model.addEventListener("change", () => {
  updateModelUI();
  resetSim();
});

preset.addEventListener("change", (e) => applyPreset(e.target.value));

runBtn.addEventListener("click", runSim);
pauseBtn.addEventListener("click", pauseSim);
resetBtn.addEventListener("click", resetSim);

showDidt.addEventListener("change", () => {
  cardDidt.style.display = showDidt.checked ? "block" : "none";
});

showIntegral.addEventListener("change", () => {
  cardInt.style.display = showIntegral.checked ? "block" : "none";
});

function attachTooltip(canvas, data, tipEl, crossEl, label, unit) {
  canvas.addEventListener("mousemove", (e) => {
    if (data.length < 2) return;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const w = canvas.width;
    const idx = Math.max(
      0,
      Math.min(data.length - 1, Math.round(((x - 10) / (w - 20)) * (data.length - 1)))
    );
    const time = idx * dt;
    const value = data[idx];
    tipEl.style.opacity = "1";
    tipEl.style.left = `${x}px`;
    tipEl.style.top = `${(idx / (data.length - 1)) * rect.height}px`;
    tipEl.textContent = `${label}: ${value.toFixed(3)} ${unit} | t=${time.toFixed(
      3
    )}s`;
    crossEl.style.opacity = "1";
    crossEl.style.left = `${x}px`;
  });

  canvas.addEventListener("mouseleave", () => {
    tipEl.style.opacity = "0";
    crossEl.style.opacity = "0";
  });
}

attachTooltip(chartI, dataI, tipI, crossI, "I", "A");
attachTooltip(chartV, dataV, tipV, crossV, "V", "V");
attachTooltip(chartDidt, dataDidt, tipDidt, crossDidt, "di/dt", "A/s");
attachTooltip(chartInt, dataInt, tipInt, crossInt, "Int", "C");

loadCustomPresets();
loadState();
loadCustomPresets();
updateLabels();
updateModelUI();
resetSim();

function saveCustomPreset() {
  const name = (customName.value || "").trim();
  if (!name) return;
  const presetKey = `preset_${name}`;
  const payload = {
    name,
    model: model.value,
    inputMode: inputMode.value,
    r: rSlider.value,
    l: lSlider.value,
    c: cSlider.value,
    v: vSlider.value,
  };
  localStorage.setItem(presetKey, JSON.stringify(payload));
  loadCustomPresets();
  preset.value = `custom:${name}`;
  saveState();
}

savePresetBtn.addEventListener("click", saveCustomPreset);

deletePresetBtn.addEventListener("click", () => {
  const value = preset.value || "";
  if (!value.startsWith("custom:")) return;
  const name = value.replace("custom:", "");
  const ok = window.confirm(`Hapus preset "${name}"?`);
  if (!ok) return;
  localStorage.removeItem(`preset_${name}`);
  removeCustomOption(name);
  preset.value = "custom";
  saveState();
});

exportBtn.addEventListener("click", () => {
  if (timeAxis.length === 0) return;
  const rows = [
    `# model=${model.value}`,
    `# R=${rSlider.value}`,
    `# L=${lSlider.value}`,
    `# C=${cSlider.value}`,
    `# V=${vSlider.value}`,
    `# dt=${dt}`,
    `# duration=${duration}`,
    "t,i,v,didt,integral",
  ];
  for (let idx = 0; idx < timeAxis.length; idx++) {
    rows.push(
      `${timeAxis[idx].toFixed(6)},${dataI[idx].toFixed(6)},${dataV[idx].toFixed(
        6
      )},${dataDidt[idx].toFixed(6)},${dataInt[idx].toFixed(6)}`
    );
  }
  const blob = new Blob([rows.join("\n")], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "simulasi-transien.csv";
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
});
