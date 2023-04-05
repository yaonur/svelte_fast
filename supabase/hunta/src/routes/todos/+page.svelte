<script lang="ts">
	import type { PageData } from '../$types';
	export let data: PageData;
	console.log(data)
	
</script>

<div>Todos</div>
{#each data.todos as todo}
	 <!-- content here -->
	 <p>{todo.todo}</p>
{/each}