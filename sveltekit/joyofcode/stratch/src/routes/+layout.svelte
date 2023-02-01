<script lang="ts">
	import '@picocss/pico';
	import '../app.css';
</script>

<body data-theme="dark">
	<slot />
</body>

<style>
	body{
		height: 100vh;
		background-color: var(--background-color);
	}
</style>
