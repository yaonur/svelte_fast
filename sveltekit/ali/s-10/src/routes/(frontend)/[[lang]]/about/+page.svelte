<script lang="ts">
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';

</script>

<h1>About</h1>
{JSON.stringify($page.params, null, 2)}
<button
	on:click={() => {
		goto('/');
	}}>Home</button
>
