jQuery(document).ready(function () {
    jQuery("#id_bug_type").click(function () {
        const optionsByBugType = {
            feature: ['new', 'started', 'completed'],
            bug: ['new', 'started', 'resolved']
        };
        const bugTypeDropdown = document.getElementById('id_bug_type');
        const bugStatusDropdown = document.getElementById('id_bug_status');
       
        const selectedBugType = bugTypeDropdown.value;
        console.log(bugTypeDropdown.value)
        const bugStatusOptions = optionsByBugType[selectedBugType];
        bugStatusDropdown.innerHTML = ''

        bugStatusOptions.forEach(status => {
            const option = document.createElement('option');
            option.value = status;
            option.textContent = status.charAt(0).toUpperCase() + status.slice(1);
            bugStatusDropdown.appendChild(option);
        });

    });
});
