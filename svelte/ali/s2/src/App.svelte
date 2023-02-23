<script>
	import Button from './lib/Button.svelte';
</script>

<Button shadow="true" on:click|once={() => alert(true)} disabled="true">Something</Button>
<Button shadow="true">2. button</Button>
<div>
	<h1>Hey</h1>
	<p>paragraph</p>
</div>

<button class="bg-sky-700 px-4 py-2 text-white hover:bg-sky-800 sm:px-8 sm:py-3">...</button>

<style lang="postcss">
	h1 {
		display: flex;
		justify-content: center;
		color: black;
		font-size: 2rem;
		transition: transform 5s ease;

		&:hover {
			transform: rotate(2turn);
		}
	}

	p {
		background-color: #1a1a1a;
		color: var(--textColor);
	}
</style>
