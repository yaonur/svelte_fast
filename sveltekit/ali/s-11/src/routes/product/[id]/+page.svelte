<script lang="ts">
	import { stylesheets } from './../../../../../../joyofcode/stratch/.svelte-kit/output/server/nodes/0.js';
    import type { PageData } from './$types';
    
    export let data: PageData;
    const product=data.product
</script>
<!-- <svelte:head>
    <title>{product?.title}</title>
</svelte:head> -->
{#if product}
     <!-- content here -->
     <img src={product.thumbnail} alt={product.title}>
     <h1>{product.title}</h1>
     <p>{product.description}</p>


{/if}

<style lang='postcss'> 
img {
    width: 60%;
}

</style>