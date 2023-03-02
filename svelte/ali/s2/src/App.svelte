<script>
	import TodoList from './lib/TodoList.svelte';
	import { v4 as uuid } from 'uuid';
	import { tick, onMount } from 'svelte';
	let todoList;
	let showList = true;
	let todos = null;
	let error = null;
	let isLoading = false;
	let isAdding = false;
  let disabledItems=[]

	onMount(() => {
		loadTodos();
	});

	async function loadTodos() {
		isLoading = true;
		await fetch('https://jsonplaceholder.typicode.com/todos?_limit=5').then(async (response) => {
			if (response.ok) {
				todos = await response.json();
			} else {
				error = 'An error occurred';
			}
		});
		isLoading = false;
	}
	async function handleAddTodo(event) {
		event.preventDefault();
		isAdding = true;
		await fetch('https://jsonplaceholder.typicode.com/todos?_limit=5', {
			method: 'POST',
			body: JSON.stringify({
				title: event.detail.title,
				completed: false
			}),
			headers: {
				'Content-type': 'application/json; charset=UTF-8'
			}
		}).then(async (response) => {
			if (response.ok) {
				const todo = await response.json();
				todos = [...todos, { ...todo, id: uuid() }];
			} else {
				error = 'An error occurred';
			}
			isAdding = false;
		});
    await tick();
    todoList.focusInput()
		todoList.clearInput();
	}
	async function handleRemoveTodo(event) {
    const id =event.detail.id
    if (disabledItems.includes(id)) return
    disabledItems=[...disabledItems,id]
    await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`, {
      method: 'DELETE',
    }).then(async (response) => {
      if (response.ok) {
        todos = todos.filter((t) => t.id !== id);
      } else {
        error = 'An error occurred';
      }
    });
    disabledItems=disabledItems.filter((i) => i !== id)
	}
	function handleToggleTodo(event) {
		todos = todos.map((todo) => {
			if (todo.id === event.detail.id) {
				return { ...todo, completed: event.detail.value };
			}
			return { ...todo };
		});
	}
</script>

<label>
	<input type="checkbox" bind:checked={showList} />
	Show/Hide list
</label>
{#if showList}
	<div style:max-width="400px">
		<TodoList
			{todos}
			{error}
			{isLoading}
			{isAdding}
      {disabledItems}
			bind:this={todoList}
			on:addtodo={handleAddTodo}
			on:removetodo={handleRemoveTodo}
			on:toggletodo={handleToggleTodo}
		/>
	</div>
{/if}

<style>
</style>
