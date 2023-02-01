<script>
  import Navbar from "$lib/Navbar.svelte";
  import { page } from "$app/stores";
  import "../app.css";
</script>

<Navbar />

{#if $page.url.pathname === '/about'}
  <div class="about-container">
    <div class="item">
      <slot />
    </div>
  </div>
{:else}
  <div class="container">
    <slot />
  </div>
{/if}

<style>
  .container {
    padding: 2em;
    margin: auto;
  }
  
  .about-container {
    display: flex;
    flex-direction: column;
  }
  
  .item {
    align-self: flex-end;
  }
</style>
