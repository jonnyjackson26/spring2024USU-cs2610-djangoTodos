console.log('hh');

for (let checkbox of document.querySelectorAll("input[type='checkbox']")) {
    checkbox.addEventListener('change', (e) => {
        console.log(e.target.dataset.todoId);
        const body = new FormData();
        body.append("is_completed", e.target.checked);
        fetch(`/todos/${e.target.dataset.todoId}/`, {
            method: 'post',
            body
        });
    });
}