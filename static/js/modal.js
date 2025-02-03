document.addEventListener('DOMContentLoaded', function () {
    const openButtons = document.querySelectorAll('.modal-btn-open');
    const closeButtons = document.querySelectorAll('.modal-btn-close');

    openButtons.forEach(button => {
        button.addEventListener('click', function () {
            const taskId = this.getAttribute('data-task-id');
            const modal = document.getElementById(`modal-${taskId}`);
            modal.classList.remove('is-hidden');
        });
    });

    closeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const modal = this.closest('.backdrop');
            modal.classList.add('is-hidden');
        });
    });
});
