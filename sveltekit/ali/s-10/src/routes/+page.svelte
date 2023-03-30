<script>
	import { goto, beforeNavigate, afterNavigate } from '$app/navigation';
	import { Button } from '$components';

	beforeNavigate((url) => {
		console.log('beforeNavigate', url);
	});
	afterNavigate((url) => {
		console.log('afterNavigate', url);
	});
</script>

<button
	on:click={() => {
		goto('/about');
	}}>About</button
>
