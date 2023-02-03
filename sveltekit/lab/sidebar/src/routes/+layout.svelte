<script>
	import Icon from '@iconify/svelte';
	import '../app.css';
	import Navbar from '../lib/Navbar.svelte';
</script>

<div class="container">
	<div class="nav-container">
		<Navbar />
	</div>
	<div class="slot-container">
		<slot />
	</div>
</div>

<style>
	.container {
		background-color: var(--primary-background);
		height: 100vh;
		display: flex;
	}
  .nav-container{
    background-color: var(--navbar-background);
  }
</style>
