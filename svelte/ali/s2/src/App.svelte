<script lang="ts">
	import TodoList from './lib/TodoList.svelte';
	import { v4 as uuid } from 'uuid';
	import NavBar from './lib/NavBar.svelte';

	const todos = [
		{ id: uuid(), title: 'todo1', completed: true },
		{ id: uuid(), title: 'todo2', completed: true },
		{ id: uuid(), title: 'todo3', completed: true }
	];
</script>


	<TodoList {todos} />

<style lang="postcss">
</style>
