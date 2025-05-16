// Example: Confirmation dialog for delete buttons
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this?')) {
                event.preventDefault(); // Prevent the link from following the URL
            }
        });
    });
});