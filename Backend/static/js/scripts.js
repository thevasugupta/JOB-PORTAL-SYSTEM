// Handle Job Posting (for future use with forms)
async function postJob(event) {
    event.preventDefault();

    const jobData = {
        title: document.getElementById('job-title').value,
        location: document.getElementById('job-location').value,
        skills: document.getElementById('job-skills').value,
        salary: document.getElementById('job-salary').value
    };

    try {
        const response = await fetch('/jobs', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jobData)
        });

        const result = await response.json();
        alert(result.message);
        location.reload(); // Reload the page to update the jobs list
    } catch (error) {
        console.error('Error posting job:', error);
        alert('Failed to post job.');
    }
}

// Handle Search Functionality
async function searchJobs(event) {
    event.preventDefault();

    const criteria = document.getElementById('search-criteria').value;

    try {
        const response = await fetch(`/search?criteria=${criteria}`);
        const html = await response.text();
        document.getElementById('results').innerHTML = html;
    } catch (error) {
        console.error('Error searching jobs:', error);
        alert('Failed to search jobs.');
    }
}
