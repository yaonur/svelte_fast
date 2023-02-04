<script lang="ts">
	import Navbar from '../lib/Navbar.svelte';
	import '../app.css';
</script>

<Navbar />
<!--<div class="container">-->
	<slot />
<!--</div>-->

<style>
	h1 {
		margin: 0;
		font-size: 2.5em;
	}
</style>
