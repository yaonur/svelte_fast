<script lang="ts">
	import type { Card as CardT } from '../lib/types';

	import Card from '../lib/Card.svelte';
	import Nav from '../lib/Nav.svelte';

	let cardsLatest: Array<CardT> = [
		{ fileName: 'stew.jpg', mealName: '5 picalo stews', ownerName: 'John the Stewer' }
	];
	let cardsPopular: Array<CardT> = [
		{ fileName: 'noodles.jpg', mealName: 'Noodly noob', ownerName: 'Patriac the Noodler' }
	];
</script>

<div>
	<Nav />

	<main class="px-16 py-6 bg-gray-500">
		<div class="flex  justify-center md:justify-end">
			<a href="/" class="text-primary">Log in</a>
			<a href="/" class="ml-2 text-primary">Sign up</a>
		</div>

		<header>
			<h2 class="text-6xl font-semibold text-gray-800">Recipes</h2>
			<h3 class="text-2xl font-semibold">For ninjas</h3>
		</header>

		<div>
			<h4 class="mt-12 border-b border-gray-200 pb-2 font-bold">Latest Recipes</h4>
			<div class="mt-8">
				<!-- cards go here -->
				{#each cardsLatest as card}
					<Card {card} />
				{/each}
			</div>

			<h4 class="mt-12 border-b border-gray-200 font-bold">Most Popular</h4>
			<div class="mt-8">
				<!-- cards go here -->
				<!--{#each cardsPopular as card}-->
				<!--	<Card {card} />-->
				<!--{/each}-->
			</div>

			<div class="flex justify-center">
				<div class="bg-secondary-100 text-secondary-200">Load More</div>
			</div>
		</div>
	</main>
</div>

<style lang="postcss">
</style>
