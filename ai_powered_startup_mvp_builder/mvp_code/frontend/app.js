const API_URL = 'http://localhost:8000/api';
let currentProjectId = null;

// Navigation
const navIntake = document.getElementById('nav-intake');
const navFeatures = document.getElementById('nav-features');
const navStories = document.getElementById('nav-stories');
const navExport = document.getElementById('nav-export');

const stepIntake = document.getElementById('step-intake');
const stepFeatures = document.getElementById('step-features');
const stepStories = document.getElementById('step-stories');
const stepExport = document.getElementById('step-export');

function showStep(stepEl, navEl) {
    document.querySelectorAll('.step').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav li').forEach(el => el.classList.remove('active'));
    
    stepEl.classList.add('active');
    navEl.classList.add('active');
}

// Ensure proper step navigation
navIntake.addEventListener('click', () => showStep(stepIntake, navIntake));
navFeatures.addEventListener('click', () => { if(currentProjectId) showStep(stepFeatures, navFeatures); });
navStories.addEventListener('click', () => { if(currentProjectId) showStep(stepStories, navStories); });
navExport.addEventListener('click', () => { if(currentProjectId) showStep(stepExport, navExport); });

// Step 1: Intake
document.getElementById('btn-intake').addEventListener('click', async () => {
    const title = document.getElementById('project-title').value || 'My MVP';
    const raw_idea = document.getElementById('project-idea').value;
    const constraints = document.getElementById('project-constraints').value || 'None';

    if (!raw_idea) return alert("Please enter an idea.");

    try {
        // Create project
        const res = await fetch(`${API_URL}/projects`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, raw_idea, constraints })
        });
        const data = await res.json();
        currentProjectId = data.project_id;
        
        // Fetch project details to show AI output
        const projRes = await fetch(`${API_URL}/projects/${currentProjectId}`);
        const projData = await projRes.json();

        const outputBox = document.getElementById('intake-output');
        outputBox.innerHTML = `
            <h3>AI Analysis</h3>
            <p><strong>Problem Statement:</strong><br/>${projData.problem_statement}</p>
            <p><strong>Target Users:</strong><br/>${projData.target_users}</p>
            <button class="btn btn-secondary" onclick="showStep(stepFeatures, navFeatures)" style="margin-top: 15px;">Proceed to Features &rarr;</button>
        `;
        outputBox.classList.remove('hidden');

    } catch (err) {
        console.error(err);
        alert("Error creating project!");
    }
});

// Step 2: Features
document.getElementById('btn-generate-features').addEventListener('click', async () => {
    try {
        const res = await fetch(`${API_URL}/projects/${currentProjectId}/features/generate`, { method: 'POST' });
        const features = await res.json();
        
        const container = document.getElementById('features-container');
        container.innerHTML = '';
        container.classList.remove('hidden');

        features.forEach(f => {
            const el = document.createElement('div');
            el.className = 'feature-card';
            el.innerHTML = `
                <h3>${f.title}</h3>
                <p>${f.description}</p>
                <div class="priority-tag">${f.priority.toUpperCase()}</div>
            `;
            container.appendChild(el);
        });

        document.getElementById('btn-proceed-stories').classList.remove('hidden');
    } catch (err) {
        console.error(err);
        alert("Error generating features!");
    }
});

document.getElementById('btn-proceed-stories').addEventListener('click', () => {
    showStep(stepStories, navStories);
});

// Step 3: Stories
document.getElementById('btn-generate-stories').addEventListener('click', async () => {
    try {
        const res = await fetch(`${API_URL}/projects/${currentProjectId}/stories/generate`, { method: 'POST' });
        const stories = await res.json();
        
        const list = document.getElementById('stories-list');
        list.innerHTML = '';
        list.classList.remove('hidden');

        stories.forEach(s => {
            const li = document.createElement('li');
            li.textContent = s.full_text;
            list.appendChild(li);
        });

        document.getElementById('btn-proceed-export').classList.remove('hidden');
    } catch (err) {
        console.error(err);
        alert("Error generating stories!");
    }
});

document.getElementById('btn-proceed-export').addEventListener('click', () => {
    showStep(stepExport, navExport);
});

// Step 4: Export
document.getElementById('btn-generate-export').addEventListener('click', async () => {
    try {
        const res = await fetch(`${API_URL}/export/${currentProjectId}`);
        const data = await res.json();
        
        const pane = document.getElementById('export-pane');
        const mkd = document.getElementById('markdown-output');
        
        pane.classList.remove('hidden');
        mkd.textContent = data.markdown;
        
    } catch (err) {
        console.error(err);
        alert("Error generating document!");
    }
});
