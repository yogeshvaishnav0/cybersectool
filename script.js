// Navigation Logic
function showSection(sectionId) {
    // Hide all sections
    document.getElementById('home-section').classList.add('hidden');
    document.getElementById('dorking-section').classList.add('hidden');
    document.getElementById('exif-section').classList.add('hidden');
    document.getElementById('ai-section').classList.add('hidden');

    // Show selected section
    if(sectionId === 'home') document.getElementById('home-section').classList.remove('hidden');
    if(sectionId === 'dorking') document.getElementById('dorking-section').classList.remove('hidden');
    if(sectionId === 'exif') document.getElementById('exif-section').classList.remove('hidden');
    if(sectionId === 'ai') document.getElementById('ai-section').classList.remove('hidden');
}

// Google Dorking Logic (Adapted from your code)
function executeDork() {
    const query = document.getElementById('dork-query').value;
    const type = document.getElementById('dork-type').value;
    const engine = document.getElementById('dork-engine').value;

    if (!query) {
        alert("Please enter a target keyword!");
        return;
    }

    let dork = "";

    // Dorking Strategies
    if (type === "TV/Movies") {
        dork = `${query} +(mkv|mp4|avi|mov) -inurl:(jsp|php|html|aspx) intitle:index.of`;
    } 
    else if (type === "Books") {
        dork = `${query} +(pdf|epub|mobi) -inurl:(jsp|php|html|aspx) intitle:index.of`;
    }
    else if (type === "Music") {
        dork = `${query} +(mp3|flac|wav) intitle:index.of`;
    }
    else if (type === "Sensitive") {
        // Advanced Bug Bounty Dork
        dork = `site:${query} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ini | ext:env`;
    }
    else if (type === "Directory") {
        dork = `site:${query} intitle:index.of`;
    }
    else {
        // Default Google Search
        dork = query;
    }

    // Engine Selection
    let url = "";
    if (engine === "google") {
        url = `https://www.google.com/search?q=${encodeURIComponent(dork)}`;
    } else if (engine === "duckduckgo") {
        url = `https://duckduckgo.com/?q=${encodeURIComponent(dork)}`;
    } else if (engine === "startpage") {
        url = `https://www.startpage.com/do/dsearch?query=${encodeURIComponent(dork)}`;
    }

    // Open in new tab
    console.log("Executing Dork: ", dork);
    window.open(url, '_blank');
}