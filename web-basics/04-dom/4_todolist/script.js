const $inputTodo = document.querySelector('#input-todo');
$inputTodo.onkeyup = (e) => e.key == 'Enter' ? triggerCreateTodo() : null;

const $todoList = document.querySelector('#todo-list');
$todoList.innerHTML = '';

const $btnAdd = document.querySelector('#btn-add');
$btnAdd.onclick = triggerCreateTodo;

// load from local storage
const todoList = JSON.parse(localStorage.getItem('todoList')) || {};
for (const id in todoList) {
    addTodoToDOM(todoList[id]);
}


function triggerCreateTodo() {
    const todo = createTodo();
    addTodoToDOM(todo);
    updateLocalStorage();
}


function updateLocalStorage() {
    localStorage.setItem('todoList', JSON.stringify(todoList));
}


function createTodo() {
    const content = $inputTodo.value.trim();
    if (!content) {
        return;
    }
    $inputTodo.value = '';

    const todo = {
        id: Date.now(),
        content: content,
        completed: false
    }
    todoList[todo.id] = todo;

    return todo;
}


function addTodoToDOM(todo) {
    const $li = document.createElement('li');
    $li.classList.add('todo-item');

    const $checkbox = document.createElement('input');
    $checkbox.type = 'checkbox';

    const $span = document.createElement('span');
    if (todo.completed) {
        $span.classList.add('completed');
    }

    const $textComplete = document.createTextNode(todo.content);

    const $btnDelete = document.createElement('button')
    $btnDelete.classList.add('delete-btn');

    const $textDelete = document.createTextNode('삭제');

    $todoList.appendChild($li);

    $li.appendChild($checkbox);
    $li.appendChild($span);
    $li.appendChild($btnDelete);

    $span.appendChild($textComplete);
    $btnDelete.appendChild($textDelete);

    $checkbox.onclick = () => updateTodo($checkbox.checked, todo, $span);
    $btnDelete.onclick = () => removeTodo(todo, $li);
}


function updateTodo(checked, todo, $span) {
    if (checked) {
        $span.classList.add('completed');
        todo.completed = true;
    } else {
        $span.classList.remove('completed');
        todo.completed = false;
    }

    updateLocalStorage();
}


function removeTodo(todo, $li) {
    delete todoList[todo.id];
    $todoList.removeChild($li);

    updateLocalStorage();
}
