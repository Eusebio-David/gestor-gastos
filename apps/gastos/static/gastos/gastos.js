
document.addEventListener('DOMContentLoaded', function () {
    const viewMode = document.getElementById('view-mode');
    const editMode = document.getElementById('edit-mode');
    const editButton = document.getElementById('edit-button');
    const editModeButton = document.getElementById('edit-mode-button');
    const cancelEditButton = document.getElementById('cancel-edit-button');

    function activateEditMode() {
        viewMode.classList.add('hidden');
        editMode.classList.remove('hidden');
    }

    function activateViewMode() {
        editMode.classList.add('hidden');
        viewMode.classList.remove('hidden');
    }

    editButton?.addEventListener('click', activateEditMode);
    editModeButton?.addEventListener('click', activateEditMode);
    cancelEditButton?.addEventListener('click', activateViewMode);
});
