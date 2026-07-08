let circulars = [];
let selectedId = null;

const circularListEl = document.getElementById("circular-list");
const runBtn = document.getElementById("run-btn");
const agentPanel = document.getElementById("agent-panel");
const reportPanel = document.getElementById("report-panel");
const reasoningLog = document.getElementById("reasoning-log");
const reportHeader = document.getElementById("report-header");
const flagsList = document.getElementById("flags-list");
const statusPill = document.getElementById("status-pill");

async function loadCirculars() {
  const res = await fetch("/api/circulars");
  circulars = await res.json();
  circularListEl.innerHTML = "";
  circulars.forEach((c) => {
    const div = document.createElement("div");
    div.className = "circular-card";
    div.dataset.id = c.id;
    div.innerHTML = `
      <div class="c-title">${c.title}</div>
      <div class="c-subject">${c.subject}</div>
    `;
    div.onclick = () => selectCircular(c.id);
    circularListEl.appendChild(div);
  });
}

function selectCircular(id) {
  selectedId = id;
  document.querySelectorAll(".circular-card").forEach((el) => {
    el.classList.toggle("selected", el.dataset.id === id);
  });
  runBtn.disabled = false;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function runAgent() {
  if (!selectedId) return;
  runBtn.disabled = true;
  agentPanel.style.display = "block";
  reportPanel.style.display = "none";
  reasoningLog.innerHTML = "";
  flagsList.innerHTML = "";
  statusPill.textContent = "● Agent analyzing...";

  const res = await fetch("/api/analyze/" + selectedId);
  const data = await res.json();

  for (let i = 0; i < data.reasoning_steps.length; i++) {
    const div = document.createElement("div");
    div.className = "reasoning-step";
    div.style.animationDelay = "0s";
    div.innerHTML = `<span class="dot"></span><span>${data.reasoning_steps[i]}</span>`;
    reasoningLog.appendChild(div);
    agentPanel.scrollIntoView({ behavior: "smooth", block: "nearest" });
    await sleep(750);
  }

  await sleep(400);
  reportPanel.style.display = "block";
  reportHeader.innerHTML = `
    <b>${data.title}</b><br>
    ${data.subject}<br><br>
    <b>Compared against:</b> ${data.company_doc}<br>
    <b>Summary:</b> ${data.summary}
  `;

  data.flags.forEach((f, i) => {
    const div = document.createElement("div");
    div.className = "flag-card " + f.severity.toLowerCase();
    div.style.animationDelay = (i * 0.15) + "s";
    div.innerHTML = `
      <div class="flag-top">
        <span class="flag-clause">${f.clause}</span>
        <span class="severity-badge ${f.severity.toLowerCase()}">${f.severity} priority</span>
      </div>
      <div class="flag-current">${f.current}</div>
      <div class="flag-issue">${f.issue}</div>
    `;
    flagsList.appendChild(div);
  });

  statusPill.textContent = "● Analysis complete";
  reportPanel.scrollIntoView({ behavior: "smooth", block: "start" });
}

function resetDemo() {
  selectedId = null;
  runBtn.disabled = true;
  agentPanel.style.display = "none";
  reportPanel.style.display = "none";
  reasoningLog.innerHTML = "";
  flagsList.innerHTML = "";
  statusPill.textContent = "● Monitoring SEBI circulars";
  document.querySelectorAll(".circular-card").forEach((el) => el.classList.remove("selected"));
  window.scrollTo({ top: 0, behavior: "smooth" });
}

runBtn.addEventListener("click", runAgent);
document.getElementById("reset-btn").addEventListener("click", resetDemo);

loadCirculars();
