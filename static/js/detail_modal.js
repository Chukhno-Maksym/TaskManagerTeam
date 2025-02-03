let detailsUrl = `/detailed_sidebar/`

const openButtons = document.getElementsByClassName("open-sidebar-btn");
for (let i = 0; i < openButtons.length; i++) {
    openButtons[i].addEventListener("click", function() {
        sidebar.classList.add("open");
    });
}

const closeButtons = document.getElementsByClassName("close-sidebar-btn");
for (let i = 0; i < closeButtons.length; i++) {
    closeButtons[i].addEventListener("click", function() {
        sidebar.classList.remove("open");
    });
}

function getDetails(button) {
    const taskId = button.getAttribute("data-task-id");
    const urlWithTask = `${detailsUrl}?task_id=${taskId}`;

    const updateLink = document.getElementById("update-link");
    updateLink.href = `/task/update/${taskId}`;

    const deleteLink = document.getElementById("delete-link");
    deleteLink.href = `/task/delete/${taskId}`;

    return fetch(urlWithTask, {
        method: 'GET',
    }).then(response => response.json())
        .then(data => showDetails(data))
        .catch(error => console.log("Error", error));
}


function  showDetails(details) {
    console.log(details);

    const taskList = document.getElementById("task-details-list");
    if (taskList) {
        taskList.innerHTML = "";

    details.queryset.forEach(task => {
        const taskItem = document.createElement("li");
        const workers = task.workers.join(", ");
        taskItem.innerHTML = `
            Name: ${task.Name}<br>
            Type: ${task.Type}<br>
            Worker: ${workers}<br>
            Deadline: ${task.Deadline}<br>
            Status: ${task.Status ? 'Completed' : 'Not Completed'}
          `;
        taskList.appendChild(taskItem);

        });
    }
}

