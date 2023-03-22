<script>
	import Navbar from '$lib/components/Navbar.svelte';
	import '../app.css';
</script>

<div class="text-gray-600 font-body">
	<div>
		<Navbar />
	</div>
	<slot />
</div>
