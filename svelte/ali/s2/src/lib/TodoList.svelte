<svelte:options immutable={true} />

<script>
	import Button from './Button.svelte';
	import { createEventDispatcher, afterUpdate } from 'svelte';
	import FaRegTrashAlt from 'svelte-icons/fa/FaRegTrashAlt.svelte';

	afterUpdate(() => {
		if (autoscroll) listDiv.scrollTo(0, listDivScrollHeight);
		autoscroll = false;
	});
	export let todos = null;
	export let error = null;
	export let isLoading = false;
	export let isAdding = false;
	export let disabledItems = [];
	let prevTodos = todos;
	let inputText = '';
	let input, listDiv, autoscroll, listDivScrollHeight;
	const dispatch = createEventDispatcher();
	$: {
		autoscroll = todos && prevTodos && todos.length > prevTodos.length;
		prevTodos = todos;
	}

	export function clearInput() {
		inputText = '';
	}

	export function focusInput() {
		input.focus();
	}

	function handleAddTodo() {
		console.log(isAdding);
		const isNotCancelled = dispatch(
			'addtodo',
			{
				title: inputText
			},
			{
				cancelable: true
			}
		);
		if (isNotCancelled) {
			inputText = '';
		}
	}

	function handleRemoveTodo(id) {
		dispatch('removetodo', {
			id
		});
	}

	function handleToggleTodo(id, value) {
		dispatch('toggletodo', {
			id,
			value
		});
	}
</script>

<div class="todo-list-wrapper">
	{#if isLoading}
		<div class="state-text">Loading...</div>
	{:else if error}
		<div class="state-text">Error: {error}</div>
	{:else if todos}
		<div class="todo-list" bind:this={listDiv}>
			<div bind:offsetHeight={listDivScrollHeight}>
				{#if todos.length === 0}
					<p class="state-text">No todos yet</p>
				{:else}
					<ul>
						{#each todos as { id, title, completed } (id)}
							<li class:completed>
								<label>
									<input
										on:input={(event) => {
											event.currentTarget.checked = completed;
											handleToggleTodo(id, !completed);
										}}
										type="checkbox"
										checked={completed}
									/>
									{title}
								</label>
								<button
									disabled={disabledItems.includes(id)}
									class="remove-todo-button"
									aria-label="Remove todo: {title}"
									on:click={() => handleRemoveTodo(id)}
								>
									<span style:width="10px" style:display="inline-block">
										<FaRegTrashAlt />
									</span>
								</button>
							</li>
						{/each}
					</ul>
				{/if}
			</div>
		</div>
	{/if}
	<form class="add-todo-form" on:submit|preventDefault={handleAddTodo}>
		<input
			bind:this={input}
			bind:value={inputText}
			placeholder="New Todo"
			disabled={isAdding || !todos}
		/>
		<Button type="submit" class="add-todo-button" disabled={!inputText || isAdding || !todos}
			>Add</Button
		>
	</form>
</div>

<style lang="postcss">
	.todo-list-wrapper {
		background-color: #424242;
		border: 1px solid #424242;

		.state-text {
			margin: 0;
			padding: 15px;
			text-align: center;
		}

		.add-todo-form {
			padding: 15px;
			background-color: #303030;
			display: flex;
			flex-wrap: wrap;
			border-top: 1px solid #4b4b4b;

			:global(.add-todo-button) {
				background-color: aqua;
			}

			input {
				flex: 1;
				margin-right: 10px;
				background-color: #424242;
				border: 1px solid #4b4b4b;
				padding: 10px;
				color: #fff;
				border-radius: 5px;
				margin-right: 10px;
			}
		}
	}

	.todo-list {
		max-height: 150px;
		overflow: auto;

		ul {
			margin: 0;
			padding: 10px;
			list-style: none;

			li {
				margin-bottom: 5px;
				display: flex;
				align-items: center;
				background-color: #303030;
				border-radius: 5px;
				padding: 10px;
				position: relative;

				label {
					cursor: pointer;
					font-size: 18px;
					display: flex;
					align-items: baseline;
					padding-right: 20px;

					input[type='checkbox'] {
						margin: 0 10px 0 0;
						cursor: pointer;
					}
				}

				&.completed > label {
					text-decoration: line-through;
					color: #ccc;
				}

				.remove-todo-button {
					border: none;
					background: none;
					padding: 5px;
					position: absolute;
					right: 10px;
					cursor: pointer;
					display: none;
					 &:disabled {
              opacity: 0.4;
              cursor: not-allowed;
            }

					:global(svg) {
						fill: #db1414;
					}
				}

				&:hover {
					.remove-todo-button {
						display: block;
					}
				}
			}
		}
	}
</style>
