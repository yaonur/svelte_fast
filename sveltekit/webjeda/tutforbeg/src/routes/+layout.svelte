<script lang="ts">
	import Navbar from '../lib/Navbar.svelte';
	import '../app.css';
  import Footer from "$lib/Footer.svelte";
</script>

<Navbar />
<!--<div class="container">-->
	<slot />
<!--</div>-->

<Footer/>
<style>
	h1 {
		margin: 0;
		font-size: 2.5em;
	}
</style>
