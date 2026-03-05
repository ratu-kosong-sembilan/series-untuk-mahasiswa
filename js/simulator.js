/**
 * Series Untuk Mahasiswa - Interactive Simulator
 * Phasor simulation, Impedance calculator, Power triangle
 */

// ============================================
// TAB SWITCHING
// ============================================
document.querySelectorAll('.sim-tab').forEach(tab => {
    tab.addEventListener('click', () => {
        // Update active tab
        document.querySelectorAll('.sim-tab').forEach(t => {
            t.classList.remove('bg-primary-600', 'text-white');
            t.classList.add('bg-white', 'text-slate-600');
        });
        tab.classList.remove('bg-white', 'text-slate-600');
        tab.classList.add('bg-primary-600', 'text-white');
        
        // Show corresponding section
        const simType = tab.dataset.sim;
        document.querySelectorAll('.simulator-section').forEach(section => {
            section.classList.add('hidden');
        });
        document.getElementById(`sim-${simType}`).classList.remove('hidden');
        
        // Initialize canvas if needed
        if (simType === 'phasor') initPhasorSim();
        if (simType === 'impedance') initImpedanceSim();
        if (simType === 'power') initPowerSim();
    });
});

// ============================================
// PHASOR SIMULATOR
// ============================================
let phasorAnimationId = null;
let phasorTime = 0;
let isPhasorPlaying = true;

const phasorState = {
    freq: 50,
    amp: 100,
    phase: 0,
    speed: 1
};

function initPhasorSim() {
    const phasorCanvas = document.getElementById('phasor-canvas');
    const waveCanvas = document.getElementById('wave-canvas');
    
    if (!phasorCanvas || !waveCanvas) return;
    
    // Setup controls
    setupPhasorControls();
    
    // Start animation
    if (phasorAnimationId) cancelAnimationFrame(phasorAnimationId);
    animatePhasor();
}

function setupPhasorControls() {
    // Frequency slider
    const freqSlider = document.getElementById('freq-slider');
    const freqValue = document.getElementById('freq-value');
    freqSlider.addEventListener('input', (e) => {
        phasorState.freq = parseInt(e.target.value);
        freqValue.textContent = `${phasorState.freq} Hz`;
        updatePhasorEquations();
    });
    
    // Amplitude slider
    const ampSlider = document.getElementById('amp-slider');
    const ampValue = document.getElementById('amp-value');
    ampSlider.addEventListener('input', (e) => {
        phasorState.amp = parseInt(e.target.value);
        ampValue.textContent = `${phasorState.amp} V`;
        updatePhasorEquations();
    });
    
    // Phase slider
    const phaseSlider = document.getElementById('phase-slider');
    const phaseValue = document.getElementById('phase-value');
    phaseSlider.addEventListener('input', (e) => {
        phasorState.phase = parseInt(e.target.value);
        phaseValue.textContent = `${phasorState.phase}°`;
        updatePhasorEquations();
    });
    
    // Speed slider
    const speedSlider = document.getElementById('speed-slider');
    const speedValue = document.getElementById('speed-value');
    speedSlider.addEventListener('input', (e) => {
        phasorState.speed = parseFloat(e.target.value);
        speedValue.textContent = `${phasorState.speed}x`;
    });
    
    // Play/Pause button
    const playBtn = document.getElementById('play-btn');
    playBtn.addEventListener('click', () => {
        isPhasorPlaying = !isPhasorPlaying;
        playBtn.innerHTML = isPhasorPlaying ? 
            '<i class="fas fa-pause mr-2"></i>Pause' : 
            '<i class="fas fa-play mr-2"></i>Play';
    });
    
    // Reset button
    const resetBtn = document.getElementById('reset-btn');
    resetBtn.addEventListener('click', () => {
        phasorState.freq = 50;
        phasorState.amp = 100;
        phasorState.phase = 0;
        phasorState.speed = 1;
        phasorTime = 0;
        
        freqSlider.value = 50;
        ampSlider.value = 100;
        phaseSlider.value = 0;
        speedSlider.value = 1;
        
        freqValue.textContent = '50 Hz';
        ampValue.textContent = '100 V';
        phaseValue.textContent = '0°';
        speedValue.textContent = '1x';
        
        updatePhasorEquations();
    });
    
    updatePhasorEquations();
}

function updatePhasorEquations() {
    const omega = 2 * Math.PI * phasorState.freq;
    const period = (1 / phasorState.freq * 1000).toFixed(2);
    
    document.getElementById('time-eq').textContent = 
        `v(t) = ${phasorState.amp} sin(${omega.toFixed(0)}t + ${phasorState.phase}°)`;
    
    document.getElementById('phasor-eq').textContent = 
        `V = ${phasorState.amp}∠${phasorState.phase}° V`;
    
    document.getElementById('rms-value').textContent = 
        `Vrms = ${(phasorState.amp / Math.sqrt(2)).toFixed(2)} V`;
    
    document.getElementById('period-value').textContent = period;
}

function animatePhasor() {
    if (isPhasorPlaying) {
        phasorTime += 0.016 * phasorState.speed * (phasorState.freq / 50);
    }
    
    drawPhasorDiagram();
    drawWaveform();
    
    phasorAnimationId = requestAnimationFrame(animatePhasor);
}

function drawPhasorDiagram() {
    const canvas = document.getElementById('phasor-canvas');
    const ctx = canvas.getContext('2d');
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = 120;
    
    // Clear canvas
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw grid
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1;
    for (let i = 0; i <= canvas.width; i += 40) {
        ctx.beginPath();
        ctx.moveTo(i, 0);
        ctx.lineTo(i, canvas.height);
        ctx.stroke();
    }
    for (let i = 0; i <= canvas.height; i += 40) {
        ctx.beginPath();
        ctx.moveTo(0, i);
        ctx.lineTo(canvas.width, i);
        ctx.stroke();
    }
    
    // Draw axes
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX, 20);
    ctx.lineTo(centerX, canvas.height - 20);
    ctx.moveTo(20, centerY);
    ctx.lineTo(canvas.width - 20, centerY);
    ctx.stroke();
    
    // Labels
    ctx.fillStyle = '#94a3b8';
    ctx.font = '14px Inter';
    ctx.fillText('Im', centerX + 10, 30);
    ctx.fillText('Re', canvas.width - 40, centerY - 10);
    
    // Calculate phasor angle (rotating)
    const angularFreq = 2 * Math.PI * phasorState.freq / 50; // normalized
    const rotationAngle = phasorTime * angularFreq + (phasorState.phase * Math.PI / 180);
    
    // Draw phasor vector
    const endX = centerX + radius * Math.cos(rotationAngle);
    const endY = centerY - radius * Math.sin(rotationAngle);
    
    // Vector line
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(endX, endY);
    ctx.stroke();
    
    // Arrow head
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath();
    ctx.arc(endX, endY, 8, 0, Math.PI * 2);
    ctx.fill();
    
    // Draw projection circle
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Draw projection to real axis
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(endX, endY);
    ctx.lineTo(endX, centerY);
    ctx.stroke();
    
    // Projection point
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(endX, centerY, 6, 0, Math.PI * 2);
    ctx.fill();
    
    // Center dot
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(centerX, centerY, 5, 0, Math.PI * 2);
    ctx.fill();
    
    // Info text
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 16px Inter';
    ctx.fillText('Diagram Phasor', 20, 40);
    
    ctx.font = '14px Inter';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText(`Amplitudo: ${phasorState.amp} V`, 20, 70);
    ctx.fillText(`Fasa: ${((rotationAngle * 180 / Math.PI) % 360).toFixed(1)}°`, 20, 90);
    ctx.fillText(`Frekuensi: ${phasorState.freq} Hz`, 20, 110);
}

function drawWaveform() {
    const canvas = document.getElementById('wave-canvas');
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw axes
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(30, canvas.height / 2);
    ctx.lineTo(canvas.width - 20, canvas.height / 2);
    ctx.moveTo(30, 20);
    ctx.lineTo(30, canvas.height - 20);
    ctx.stroke();
    
    // Labels
    ctx.fillStyle = '#94a3b8';
    ctx.font = '12px Inter';
    ctx.fillText('v(t)', 10, canvas.height / 2 - 10);
    ctx.fillText('t', canvas.width - 30, canvas.height / 2 + 20);
    ctx.fillText('+Vm', 35, 40);
    ctx.fillText('-Vm', 35, canvas.height - 30);
    
    // Draw sine wave
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 3;
    ctx.beginPath();
    
    const amplitude = 80;
    const centerY = canvas.height / 2;
    const width = canvas.width - 60;
    
    for (let x = 0; x < width; x++) {
        const t = (x / width) * 2 * Math.PI;
        const phaseRad = phasorState.phase * Math.PI / 180;
        const y = centerY - amplitude * Math.sin(t + phasorTime + phaseRad);
        
        if (x === 0) {
            ctx.moveTo(30 + x, y);
        } else {
            ctx.lineTo(30 + x, y);
        }
    }
    ctx.stroke();
    
    // Draw current position indicator
    const currentX = 30 + ((phasorTime % (2 * Math.PI)) / (2 * Math.PI)) * width;
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(currentX, 20);
    ctx.lineTo(currentX, canvas.height - 20);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Title
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 16px Inter';
    ctx.fillText('Gelombang Sinusoidal', 20, 30);
}

// ============================================
// IMPEDANCE CALCULATOR
// ============================================
const impedanceState = {
    R: 10,
    L: 100,
    C: 100,
    freq: 50
};

function initImpedanceSim() {
    setupImpedanceControls();
    updateImpedanceCalc();
}

function setupImpedanceControls() {
    // Resistance
    const rSlider = document.getElementById('r-slider');
    const rValue = document.getElementById('r-value');
    rSlider.addEventListener('input', (e) => {
        impedanceState.R = parseInt(e.target.value);
        rValue.textContent = `${impedanceState.R} Ω`;
        updateImpedanceCalc();
    });
    
    // Inductance
    const lSlider = document.getElementById('l-slider');
    const lValue = document.getElementById('l-value');
    lSlider.addEventListener('input', (e) => {
        impedanceState.L = parseInt(e.target.value);
        lValue.textContent = `${impedanceState.L} mH`;
        updateImpedanceCalc();
    });
    
    // Capacitance
    const cSlider = document.getElementById('c-slider');
    const cValue = document.getElementById('c-value');
    cSlider.addEventListener('input', (e) => {
        impedanceState.C = parseInt(e.target.value);
        cValue.textContent = `${impedanceState.C} µF`;
        updateImpedanceCalc();
    });
    
    // Frequency
    const zFreqSlider = document.getElementById('z-freq-slider');
    const zFreqValue = document.getElementById('z-freq-value');
    zFreqSlider.addEventListener('input', (e) => {
        impedanceState.freq = parseInt(e.target.value);
        zFreqValue.textContent = `${impedanceState.freq} Hz`;
        updateImpedanceCalc();
    });
}

function updateImpedanceCalc() {
    const omega = 2 * Math.PI * impedanceState.freq;
    
    // Calculate reactances
    const XL = omega * (impedanceState.L / 1000); // Convert mH to H
    const XC = 1 / (omega * (impedanceState.C / 1000000)); // Convert µF to F
    const X = XL - XC;
    
    // Calculate impedance
    const Z = Math.sqrt(Math.pow(impedanceState.R, 2) + Math.pow(X, 2));
    const theta = Math.atan2(X, impedanceState.R) * 180 / Math.PI;
    
    // Update display
    document.getElementById('xl-value').textContent = XL.toFixed(2);
    document.getElementById('xc-value').textContent = XC.toFixed(2);
    document.getElementById('display-r').textContent = `${impedanceState.R} Ω`;
    document.getElementById('display-xl').textContent = `${XL.toFixed(2)} Ω`;
    document.getElementById('display-xc').textContent = `${XC.toFixed(2)} Ω`;
    document.getElementById('display-x').textContent = `${X.toFixed(2)} Ω`;
    
    document.getElementById('z-mag').textContent = `${Z.toFixed(2)} Ω`;
    document.getElementById('z-angle').textContent = `${theta.toFixed(2)}°`;
    document.getElementById('z-rect').textContent = `Z = ${impedanceState.R.toFixed(2)} + j${X.toFixed(2)} Ω`;
    document.getElementById('z-polar').textContent = `Z = ${Z.toFixed(2)}∠${theta.toFixed(2)}° Ω`;
    
    // Draw diagram
    drawImpedanceDiagram(impedanceState.R, X, Z, theta);
}

function drawImpedanceDiagram(R, X, Z, theta) {
    const canvas = document.getElementById('impedance-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    
    // Scale factor
    const maxVal = Math.max(Math.abs(R), Math.abs(X), Z);
    const scale = 100 / (maxVal || 1);
    
    // Clear canvas
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw axes
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(30, centerY);
    ctx.lineTo(canvas.width - 30, centerY);
    ctx.moveTo(centerX, 30);
    ctx.lineTo(centerX, canvas.height - 30);
    ctx.stroke();
    
    // Labels
    ctx.fillStyle = '#94a3b8';
    ctx.font = '14px Inter';
    ctx.fillText('+jX (XL)', centerX + 10, 40);
    ctx.fillText('-jX (XC)', centerX + 10, canvas.height - 20);
    ctx.fillText('R', canvas.width - 50, centerY - 10);
    
    // Draw R component (horizontal)
    const rLength = R * scale;
    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + rLength, centerY);
    ctx.stroke();
    
    // Draw X component (vertical)
    const xLength = X * scale;
    ctx.strokeStyle = X >= 0 ? '#22c55e' : '#3b82f6';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(centerX + rLength, centerY);
    ctx.lineTo(centerX + rLength, centerY - xLength);
    ctx.stroke();
    
    // Draw Z (hypotenuse)
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(centerX + rLength, centerY - xLength);
    ctx.stroke();
    
    // Draw angle arc
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.arc(centerX, centerY, 30, -theta * Math.PI / 180, 0);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Labels
    ctx.fillStyle = '#ef4444';
    ctx.font = 'bold 12px Inter';
    ctx.fillText('R', centerX + rLength / 2, centerY - 10);
    
    ctx.fillStyle = X >= 0 ? '#22c55e' : '#3b82f6';
    ctx.fillText(X >= 0 ? 'XL' : 'XC', centerX + rLength + 10, centerY - xLength / 2);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Z', centerX + rLength / 2 - 10, centerY - xLength / 2 - 10);
    
    // Angle label
    ctx.fillStyle = '#f59e0b';
    ctx.font = '12px Inter';
    ctx.fillText(`θ=${theta.toFixed(1)}°`, centerX + 35, centerY - 10);
    
    // Title
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 16px Inter';
    ctx.fillText('Diagram Impedansi', 20, 40);
}

// ============================================
// POWER TRIANGLE
// ============================================
const powerState = {
    S: 1000,
    pf: 0.8
};

function initPowerSim() {
    setupPowerControls();
    updatePowerCalc();
}

function setupPowerControls() {
    // Apparent power
    const sSlider = document.getElementById('s-slider');
    const sValue = document.getElementById('s-value');
    sSlider.addEventListener('input', (e) => {
        powerState.S = parseInt(e.target.value);
        sValue.textContent = `${powerState.S} VA`;
        updatePowerCalc();
    });
    
    // Power factor
    const pfSlider = document.getElementById('pf-slider');
    const pfValue = document.getElementById('pf-value');
    const angleSlider = document.getElementById('power-angle-slider');
    const angleValue = document.getElementById('power-angle-value');
    
    pfSlider.addEventListener('input', (e) => {
        powerState.pf = parseFloat(e.target.value);
        pfValue.textContent = powerState.pf.toFixed(2);
        const angle = Math.acos(powerState.pf) * 180 / Math.PI;
        angleSlider.value = angle.toFixed(2);
        angleValue.textContent = `${angle.toFixed(2)}°`;
        updatePowerCalc();
    });
    
    angleSlider.addEventListener('input', (e) => {
        const angle = parseFloat(e.target.value);
        powerState.pf = Math.cos(angle * Math.PI / 180);
        pfSlider.value = powerState.pf.toFixed(2);
        pfValue.textContent = powerState.pf.toFixed(2);
        angleValue.textContent = `${angle.toFixed(2)}°`;
        updatePowerCalc();
    });
}

function updatePowerCalc() {
    const P = powerState.S * powerState.pf;
    const phi = Math.acos(powerState.pf);
    const Q = powerState.S * Math.sin(phi);
    
    document.getElementById('p-value').textContent = `${P.toFixed(0)} W`;
    document.getElementById('q-value').textContent = `${Q.toFixed(0)} VAR`;
    
    // Update interpretation
    const pfIndicator = document.getElementById('pf-indicator');
    const pfText = document.getElementById('pf-text');
    
    if (powerState.pf >= 0.9) {
        pfIndicator.style.background = '#22c55e';
        pfText.textContent = 'Faktor daya sangat bagus (>0.9 ideal)';
    } else if (powerState.pf >= 0.7) {
        pfIndicator.style.background = '#eab308';
        pfText.textContent = 'Faktor daya cukup (bisa ditingkatkan)';
    } else {
        pfIndicator.style.background = '#ef4444';
        pfText.textContent = 'Faktor daya buruk (perlu perbaikan)';
    }
    
    const reactivePercent = (Q / powerState.S * 100).toFixed(1);
    document.getElementById('reactive-percent').textContent = 
        `${reactivePercent}% daya reaktif (tidak produktif)`;
    
    drawPowerTriangle(P, Q, powerState.S, phi);
}

function drawPowerTriangle(P, Q, S, phi) {
    const canvas = document.getElementById('power-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Scale
    const maxVal = Math.max(P, Q, S);
    const scale = 180 / maxVal;
    
    const startX = 100;
    const startY = canvas.height - 100;
    
    // Draw P (horizontal - active power)
    const pLen = P * scale;
    ctx.strokeStyle = '#f97316';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(startX + pLen, startY);
    ctx.stroke();
    
    // Draw Q (vertical - reactive power)
    const qLen = Q * scale;
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(startX + pLen, startY);
    ctx.lineTo(startX + pLen, startY - qLen);
    ctx.stroke();
    
    // Draw S (hypotenuse - apparent power)
    const sLen = S * scale;
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(startX + pLen, startY - qLen);
    ctx.stroke();
    
    // Fill triangle
    ctx.fillStyle = 'rgba(34, 197, 94, 0.1)';
    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(startX + pLen, startY);
    ctx.lineTo(startX + pLen, startY - qLen);
    ctx.closePath();
    ctx.fill();
    
    // Draw angle arc
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 2;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.arc(startX, startY, 40, -phi, 0);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Labels
    ctx.fillStyle = '#f97316';
    ctx.font = 'bold 16px Inter';
    ctx.fillText(`P = ${P.toFixed(0)} W`, startX + pLen / 2 - 30, startY + 30);
    
    ctx.fillStyle = '#3b82f6';
    ctx.fillText(`Q = ${Q.toFixed(0)} VAR`, startX + pLen + 15, startY - qLen / 2);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText(`S = ${S.toFixed(0)} VA`, startX + pLen / 2 - 50, startY - qLen / 2 - 20);
    
    // Angle label
    ctx.fillStyle = '#22c55e';
    ctx.font = '14px Inter';
    ctx.fillText(`φ = ${(phi * 180 / Math.PI).toFixed(1)}°`, startX + 50, startY - 15);
    
    // Power factor
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 16px Inter';
    ctx.fillText(`cos(φ) = ${powerState.pf.toFixed(2)}`, startX, 50);
    
    // Legend
    ctx.font = '14px Inter';
    ctx.fillStyle = '#f97316';
    ctx.fillText('● P (Daya Aktif - W)', canvas.width - 200, 50);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('● Q (Daya Reaktif - VAR)', canvas.width - 200, 75);
    ctx.fillStyle = '#22c55e';
    ctx.fillText('● S (Daya Semu - VA)', canvas.width - 200, 100);
    
    // Title
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 18px Inter';
    ctx.fillText('Segitiga Daya (Power Triangle)', 20, 40);
}

// ============================================
// INITIALIZATION
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    initPhasorSim();
});
