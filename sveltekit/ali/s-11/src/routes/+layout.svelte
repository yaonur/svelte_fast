<script lang="ts">
	import '../app.css';
	import type { LayoutData } from './$types';
  import {page} from '$app/stores';
	export let data: LayoutData;
  console.log($page)
</script>

<svelte:head>
	<title>Website Name {$page.data.title ? ` - ${$page.data.title}`:''}</title>
	<meta name="description" content="generic description" />
</svelte:head>

{#if data.user}
	<!-- content here -->
	<p />
	ogged in as {data.user.name}
{/if}

<nav class="bg-slate-200 p-1">
	<a href="/">Home</a>
	<a href="/products">Products</a>
</nav>

<slot />

<style lang="postcss">
	a {
		@apply border border-gray-600 bg-slate-100 px-1 text-slate-600;
	}
</style>
