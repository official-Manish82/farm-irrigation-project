const API_BASE = "http://127.0.0.1:8000";

// Global Farm State
let farmData = {
    n: 5,
    matrix: [],
    water_reqs: [],
    yields: [],
    capacity: 100,
    target: 50
};

// Charts
let timeChartObj = null;
let waterChartObj = null;
let timeData = { sort: 0, kruskal: 0, dijkstra: 0, knapsack: 0, warshall: 0, subset: 0 };

document.getElementById('btn-sample').addEventListener('click', generateSampleData);
document.getElementById('btn-export').addEventListener('click', () => {
    const element = document.getElementById('pdf-content');
    html2pdf().from(element).save('Farm_Irrigation_Optimization_Report.pdf');
});

function updateLoader(show) {
    document.getElementById('global-loader').style.display = show ? 'block' : 'none';
}

function showError(msg) {
    const toast = document.getElementById('error-toast');
    toast.textContent = msg;
    toast.classList.remove('hidden');
    setTimeout(() => toast.classList.add('hidden'), 3000);
}

function generateSampleData() {
    const n = parseInt(document.getElementById('in-n').value) || 5;
    farmData.n = n;
    farmData.capacity = parseInt(document.getElementById('in-cap').value) || 100;
    farmData.target = parseInt(document.getElementById('in-target').value) || 50;

    farmData.matrix = Array.from({length: n}, () => 
        Array.from({length: n}, () => Math.random() > 0.4 ? Math.floor(Math.random() * 20) + 1 : 0)
    );
    // Make undirected for MST logic
    for(let i=0; i<n; i++) {
        farmData.matrix[i][i] = 0;
        for(let j=i+1; j<n; j++) {
            farmData.matrix[j][i] = farmData.matrix[i][j];
        }
    }

    farmData.water_reqs = Array.from({length: n}, () => Math.floor(Math.random() * 40) + 10);
    farmData.yields = Array.from({length: n}, () => Math.floor(Math.random() * 500) + 100);

    renderWaterChart();
    alert("Sample dataset generated successfully!");
}

async function apiCall(endpoint, payload) {
    updateLoader(true);
    try {
        const res = await fetch(`${API_BASE}${endpoint}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        if(!res.ok) throw new Error("API Error");
        const data = await res.json();
        updateTimeChart(endpoint.substring(1), data.execution_time_ms);
        return data;
    } catch (e) {
        showError(`Failed to fetch ${endpoint}. Is backend running?`);
        console.error(e);
    } finally {
        updateLoader(false);
    }
}

async function runSort() {
    if(farmData.water_reqs.length === 0) generateSampleData();
    const payload = { fields: farmData.water_reqs.map((req, i) => ({id: i, water_req: req})) };
    const res = await apiCall('/sort', payload);
    if(res) document.getElementById('res-sort').innerHTML = `<b>Sort Priorities:</b><br/> ${res.sorted_fields.map(f => `F${f.id}(${f.water_req}L)`).join(', ')}`;
}

async function runKruskal() {
    if(farmData.matrix.length === 0) generateSampleData();
    const res = await apiCall('/kruskal', {matrix: farmData.matrix});
    if(res) document.getElementById('res-kruskal').innerHTML = `<b>MST Cost:</b> ${res.total_cost} units<br/><b>Edges:</b> ${res.mst_edges.length}`;
}

async function runDijkstra() {
    if(farmData.matrix.length === 0) generateSampleData();
    const res = await apiCall('/dijkstra', {matrix: farmData.matrix, source: 0});
    if(res) document.getElementById('res-dijkstra').innerHTML = `<b>Path Distances from F0:</b><br/> ${Object.entries(res.distances).map(([k,v]) => `F${k}:${v}`).join(', ')}`;
}

async function runKnapsack() {
    if(farmData.water_reqs.length === 0) generateSampleData();
    const payload = { water_reqs: farmData.water_reqs, yields: farmData.yields, capacity: farmData.capacity };
    const res = await apiCall('/knapsack', payload);
    if(res) document.getElementById('res-knapsack').innerHTML = `<b>Max Yield:</b> $${res.max_yield}<br/><b>Fields Selected:</b> [${res.selected_fields.map(i=>'F'+i).join(', ')}]`;
}

async function runWarshall() {
    if(farmData.matrix.length === 0) generateSampleData();
    const res = await apiCall('/warshall', {matrix: farmData.matrix});
    if(res) document.getElementById('res-warshall').innerHTML = `<b>Connectivity:</b><br/>Computed ${farmData.n}x${farmData.n} matrix.`;
}

async function runSubsetSum() {
    if(farmData.water_reqs.length === 0) generateSampleData();
    const payload = { water_reqs: farmData.water_reqs, target: farmData.target };
    const res = await apiCall('/subset-sum', payload);
    if(res) document.getElementById('res-subset').innerHTML = `<b>Exact ${farmData.target}L Match:</b><br/> ${res.found ? 'Yes: [' + res.subset.join('L, ') + 'L]' : 'Not possible'}`;
}

async function runAll() {
    await Promise.all([runSort(), runKruskal(), runDijkstra(), runKnapsack(), runWarshall(), runSubsetSum()]);
}

// Charting Logic
function updateTimeChart(algo, time) {
    timeData[algo] = time;
    const ctx = document.getElementById('timeChart').getContext('2d');
    if(timeChartObj) timeChartObj.destroy();
    
    timeChartObj = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(timeData).map(k => k.toUpperCase()),
            datasets: [{
                label: 'Execution Time (ms)',
                data: Object.values(timeData),
                backgroundColor: '#3b82f6'
            }]
        },
        options: { responsive: true, scales: { y: { beginAtZero: true } } }
    });
}

function renderWaterChart() {
    const ctx = document.getElementById('waterChart').getContext('2d');
    if(waterChartObj) waterChartObj.destroy();

    waterChartObj = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: farmData.water_reqs.map((_, i) => `Field ${i}`),
            datasets: [
                { label: 'Water Requirement (L)', data: farmData.water_reqs, backgroundColor: '#10b981' },
                { label: 'Yield ($)', data: farmData.yields, backgroundColor: '#94a3b8' }
            ]
        },
        options: { responsive: true, scales: { y: { beginAtZero: true } } }
    });
}

// Init empty charts
updateTimeChart('init', 0);