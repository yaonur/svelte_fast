<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;

	//@ts-ignore
	$: products = data.products.products;
	// $: console.log(products);
</script>

<h2>{data.title}</h2>
<button class="text-white px-4 sm:px-8 py-2 sm:py-3 bg-sky-700 hover:bg-sky-800">...</button>

{#if products && products.length > 0}
	<ul class="grid gap-2 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
		{#each products as product}
			<li class="">
				<img src={product.thumbnail} alt={product.title} />
				<h3>
					<a href="/product/{product.id}">{product.title}</a>
				</h3>
				<p>
					{product.description}
				</p>
			</li>
		{/each}
	</ul>
{/if}

<style lang="postcss">
</style>
