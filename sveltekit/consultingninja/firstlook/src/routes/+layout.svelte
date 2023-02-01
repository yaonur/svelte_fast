<script lang="ts">
  import Navbar from "../lib/Navbar.svelte";
  import "@picocss/pico";
</script>
<div data-theme="dark">
  <Navbar></Navbar>
  <slot></slot>
</div>
<style>
  div{
    height: 100vh;
    background-color: var(--background-color);
  }
</style>