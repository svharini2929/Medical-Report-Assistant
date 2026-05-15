const fileInput = document.getElementById("fileInput");
const uploadZone = document.getElementById("uploadZone");
const previewArea = document.getElementById("previewArea");
const previewImg = document.getElementById("previewImg");
const fileName = document.getElementById("fileName");
const removeFile = document.getElementById("removeFile");
const analyzeBtn = document.getElementById("analyzeBtn");
const loaderCard = document.getElementById("loaderCard");
const resultCard = document.getElementById("resultCard");
const resultBody = document.getElementById("resultBody");
const disclaimerBox = document.getElementById("disclaimerBox");
const downloadBtn = document.getElementById("downloadBtn");

let selectedFile = null;

// --- SYSTEM STATUS CHECK ---
fetch("/analyze", { method: "GET" })
    .catch(() => {})
    .finally(() => {
        const dot = document.querySelector(".status-dot");
        const text = document.querySelector(".status-text");
        dot.classList.add("connected");
        text.textContent = "System Ready";
    });

// --- DRAG & DROP ---
uploadZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadZone.classList.add("dragover");
});

uploadZone.addEventListener("dragleave", () => {
    uploadZone.classList.remove("dragover");
});

uploadZone.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadZone.classList.remove("dragover");
    const file = e.dataTransfer.files[0];
    if (file) handleFile(file);
});

uploadZone.addEventListener("click", () => fileInput.click());

fileInput.addEventListener("change", () => {
    if (fileInput.files[0]) handleFile(fileInput.files[0]);
});

function handleFile(file) {
    if (!file.type.startsWith("image/")) {
        alert("Please upload an image file (JPG, PNG, JPEG).");
        return;
    }
    selectedFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImg.src = e.target.result;
        fileName.textContent = file.name;
        uploadZone.style.display = "none";
        previewArea.style.display = "flex";
        analyzeBtn.disabled = false;
        resultCard.style.display = "none";
        loaderCard.style.display = "none";
    };
    reader.readAsDataURL(file);
}

// --- REMOVE FILE ---
removeFile.addEventListener("click", () => {
    selectedFile = null;
    fileInput.value = "";
    previewArea.style.display = "none";
    uploadZone.style.display = "block";
    analyzeBtn.disabled = true;
    resultCard.style.display = "none";
    loaderCard.style.display = "none";
});

// --- ANALYZE ---
analyzeBtn.addEventListener("click", async () => {
    if (!selectedFile) return;

    analyzeBtn.disabled = true;
    resultCard.style.display = "none";
    loaderCard.style.display = "block";

    const step1 = document.getElementById("step1");
    const step2 = document.getElementById("step2");
    const step3 = document.getElementById("step3");

    // Reset steps
    [step1, step2, step3].forEach(s => {
        s.classList.remove("step-done");
        s.classList.add("step-pending");
    });

    // Animate steps
    activateStep(step1);
    await delay(2000);
    completeStep(step1);
    activateStep(step2);
    await delay(2000);
    completeStep(step2);
    activateStep(step3);

    const formData = new FormData();
    formData.append("report", selectedFile);

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        completeStep(step3);
        await delay(400);
        loaderCard.style.display = "none";

        if (data.error) {
            alert("Error: " + data.error);
            analyzeBtn.disabled = false;
            return;
        }

        resultBody.innerHTML = data.explanation;
        disclaimerBox.innerHTML = "⚠️ " + data.disclaimer;
        resultCard.style.display = "block";
        resultCard.scrollIntoView({ behavior: "smooth" });

        downloadBtn.onclick = () => {
            const blob = new Blob([resultBody.innerText], { type: "text/plain" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "report_analysis.txt";
            a.click();
            URL.revokeObjectURL(url);
        };

    } catch (err) {
        loaderCard.style.display = "none";
        alert("Something went wrong. Please try again.");
        console.error(err);
    }

    analyzeBtn.disabled = false;
});

function activateStep(step) {
    step.classList.remove("step-pending");
    const icon = step.querySelector(".step-icon");
    if (icon) {
        const spinner = document.createElement("div");
        spinner.className = "step-spinner";
        step.replaceChild(spinner, icon);
    }
}

function completeStep(step) {
    step.classList.add("step-done");
    const spinner = step.querySelector(".step-spinner");
    if (spinner) {
        const icon = document.createElement("div");
        icon.className = "step-icon";
        icon.textContent = "✅";
        step.replaceChild(icon, spinner);
    }
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}