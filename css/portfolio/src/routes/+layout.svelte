<script>
	import '../app.css';
  import Nav from "$lib/Nav.svelte";
  import Header from "$lib/Header.svelte";
</script>

<div class="h-screen overflow-hidden bg-site bg-cover bg-no-repeat">
  <Header></Header>
  <Nav></Nav>
	<slot />
</div>
