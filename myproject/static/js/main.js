document.addEventListener("DOMContentLoaded", function() {
    // fade out alert messages
    const alerts = document.querySelectorAll('.messages .alert');
    alerts.forEach(alert => {
        alert.addEventListener('animationend', () => {
            alert.style.visibility = 'hidden';
        });
    });

    // highlight current date
    var today = new Date().toISOString().slice(0, 10);

    var dayCells = document.querySelectorAll('.day-cell');
    dayCells.forEach(function(cell) {
        if (cell.dataset.date === today) {
          cell.classList.add('current-date');
        }
    });

    // responsive navbar
    const navbarToggle = document.querySelector('.navbar-toggle');
    const navbarLinks = document.querySelector('.navbar-links');

    navbarToggle.addEventListener('click', () => {
        navbarLinks.classList.toggle('active');
    });
});

$(document).ready(function() {
    // Initialize select2
    $('.js-example-basic-single').select2();

    // Existing event dialog functionality
    $('.event').click(function(event) {
        // Prevent the event from bubbling up to the parent elements
        event.stopPropagation();

        var title = $(this).data('title'); // Get the event title
        var description = $(this).data('description'); // Get the event description
        var eventId = $(this).data('id'); // Get the event ID
        $('#dialog-title').text(title); // Set the title text
        $('#dialog-description').text(description); // Set the description text

        $('#event-dialog').dialog({
            modal: true,
            width: 500,
            buttons: {
                Ok: function() {
                    $(this).dialog("close");
                }
            }
        });

        // Delete event functionality inside dialog
        $('.delete-event-button').click(function() {
            window.location.href = '/mycalendar/event-delete/' + eventId + '/';
        });

        // Edit event functionality inside dialog
        $('.edit-event-button').click(function(event) {
            window.location.href = '/mycalendar/event-edit/' + eventId + '/';
        });
    });

    // Add event functionality
    $('.day-cell').click(function(event) {
        // Check if the clicked element is not an event (to avoid conflict)
        if (!$(event.target).closest('.event').length) {
            var date = $(this).data('date');
            $('#id_date').val(date); // Ensure the date is set in YYYY-MM-DD format

            $('#add-event-modal').dialog({
                modal: true,
                width: 400,
                buttons: {
                    Ok: function() {
                        $('#add-event-form').submit();
                    },
                    Cancel: function() {
                        $(this).dialog("close");
                    }
                }
            });
        }
    });
});

function generateGreeting() {
    var personId = $('#person-select').val(); // Get the selected person ID
    fetch(`/generator/generate/${personId}/`) // Fetch the greeting text
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            $('#greeting-text').val(data.greeting_text); // Set the greeting text in the textarea
        })
        .catch(error => console.error('Error:', error));
}

function generateMail() {
    var personId = $('#person-select').val(); // Get the selected person ID
    fetch(`/generator/generate/${personId}/`) // Fetch the mail text
        .then(response => response.json()) // Convert the response to JSON
        .then(data => {
            $('#mail-text').val(data.mail_text); // Set the mail text in the textarea
        })
        .catch(error => console.error('Error:', error));
}

const search = document.querySelector(".search-box input"), // Get the search input
      subjects = document.querySelectorAll(".subject-box"); // Get all the subjects

search.addEventListener("keyup", () => { // Listen for keyup event
    let searchValue = search.value.trim().toLowerCase(); // Trim spaces and convert to lowercase

    subjects.forEach(subject => { // Loop through each subject
        if (subject.dataset.name.toLowerCase().includes(searchValue)) {
            subject.style.display = "block";
        } else {
            subject.style.display = "none";
        }
    });

    if (searchValue === "") { // If the search input is empty, display all subjects
        subjects.forEach(subject => {
            subject.style.display = "block";
        });
    }
});

function downloadSelected() {
    const checkboxes = document.querySelectorAll('.file-checkbox:checked');
    const zip = new JSZip();

    // Adding files to ZIP
    const filePromises = Array.from(checkboxes).map(checkbox => {
        const fileUrl = checkbox.value;
        const fileName = checkbox.dataset.filename;

        return fetch(fileUrl)
            .then(response => response.blob())
            .then(blob => {
                zip.file(fileName, blob);
            });
    });

    // Creating and downloading ZIP file
    Promise.all(filePromises).then(() => {
        zip.generateAsync({ type: 'blob' })
            .then(content => {
                saveAs(content, 'selected_files.zip');
            });
    });
}

function downloadAll() {
    const checkboxes = document.querySelectorAll('.file-checkbox');
    const zip = new JSZip();

    // Adding files to ZIP
    const filePromises = Array.from(checkboxes).map(checkbox => {
    const fileUrl = checkbox.value;
    const fileName = checkbox.dataset.filename;

        return fetch(fileUrl)
            .then(response => response.blob())
            .then(blob => {
                zip.file(fileName, blob);
            });
    });

    // Creating and downloading ZIP file
    Promise.all(filePromises).then(() => {
        zip.generateAsync({ type: 'blob' })
            .then(content => {
                saveAs(content, 'all_files.zip');
            });
    });
}