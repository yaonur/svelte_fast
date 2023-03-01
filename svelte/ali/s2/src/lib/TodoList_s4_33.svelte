<script>
	import Button from './Button.svelte';
	import { createEventDispatcher, onDestroy, onMount, beforeUpdate, afterUpdate } from 'svelte';
 
 

	onMount(() => {
		// console.log('onMount');
		return () => {
			console.log('onMount return');
		};
	});
	onDestroy(() => {
		// console.log('onDestroy');
	});
	beforeUpdate(() => {
		// console.log('beforeUpdate');
		// if (listDiv) {
		//   console.log(listDiv.offsetHeight);
		// }
	});
	afterUpdate(() => {
		// console.log('afterUpdate');
		// console.log(listDiv.offsetHeight);
		if (prevTodos?.length !== todos.length) {
			listDiv.scrollTo(0, listDiv.scrollHeight);
      prevTodos = todos;
		}
	});

	export let todos = [];
	let prevTodos;

	export function clearInput() {
		inputText = '';
	}

	export function focusInput() {
		input.focus();
	}

	let inputText = '';
	let input, listDiv;

	const dispatch = createEventDispatcher();

	const handleAddTodo = () => {
		dispatch('addTodo', { title: inputText });
	};
	let handleRemoveTodo = (id) => {
		dispatch('removeTodo', { id: id });
	};
	let handleToggleTodo = (id, event) => {
		dispatch('toggleTodo', { id: id, completed: event.target.checked });
	};
</script>

<div class="todo-list-wrapper">
	<ul class="max-h-44 overflow-auto todo-list" bind:this={listDiv}>
		{#each todos as { id, title, completed }, index (id)}
			{@const number = index + 1}
			<!--{(console.log(title), '')}-->
			<!--{@debug id ,title}-->
			<li class="my-2 flex justify-between py-1 px-4">
				<label>
					<input
						on:input={(event) => handleToggleTodo(id, event)}
						type="checkbox"
						checked={completed}
					/>
					{number}- {title}
				</label>
				<button
					on:click={() => handleRemoveTodo(id)}
					class="ml-2 bg-cyan-400 p-1 text-gray-700 shadow shadow-cyan-600 hover:bg-cyan-600 "
					>Remove
				</button>
			</li>
		{/each}
	</ul>
	<form class="add-todo-form" on:submit|preventDefault={handleAddTodo}>
		<input bind:this={input} bind:value={inputText} class="text-gray-700" />
		<Button type="submit" disabled={!inputText}>Add</Button>
	</form>
</div>

<style>
	.todo-list-wrapper {
		width: 100%;
		max-width: 500px;
		margin: 0 auto;
	}

	.add-todo-form {
		display: flex;
	}

	.add-todo-form input {
		flex: 1;
	}

	ul {
		padding: 0;
	}

	li {
		list-style: none;
	}
</style>
