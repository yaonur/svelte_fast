<script lang="ts">
	import {count_val} from "./store";
	import {counter} from "./store"
	import Add from "./components/Add.svelte";
	import Subtract from "./components/Subtract.svelte";
	import Zero from "./components/Zero.svelte";
	import Progress from "./components/Progress.svelte";
	
	// let count
	// count_val.subscribe((val) => count = val)
	const languages = ['typescript', 'javascript', 'rust', 'python']
	let favorites: string[] = []
	let favorite: string = ''


</script>
<!--<h1>{$count_val}</h1>-->
<h1>{$counter}</h1>

<Zero></Zero>
<Add></Add>
<Subtract/>
<br>

{#each languages as language }
	<label>
		<input type="checkbox" value="{language}" bind:group={favorites}> {language}
	</label>
{/each}
<br>
<h1>Selected favorites: {favorites}</h1>
<br>
{#each languages as language }
	<label>
		<input type="radio" value="{language}" bind:group={favorite}> {language}
	</label>
{/each}
<br>
<h1>Selected favorite: {favorite}</h1>
<br>
<Progress/>


<style>
</style>