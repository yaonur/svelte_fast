<script lang="ts">
  import {onMount} from "svelte";
  import Settings from "./lib/pages/Settings.svelte";
  import Home from "./lib/pages/Home.svelte";
  onMount(() => {
    onRouteChange();
  })
  let page;
  function onRouteChange(){
    const path = window.location.hash.slice(1);
    if(path==='/'){
      page = 'home'}
    else if(path==='/settings'){
      page = 'settings'}
    else{
      window.location.hash='/'
    }
  }

</script>
<svelte:window on:hashchange={onRouteChange}/>

<nav>
  <a href="#/">Home</a>
  <a href="#/settings">Settings</a>
</nav>

{#if page === 'home'}
  <Home></Home>
{:else if page === 'settings'}
  <Settings></Settings>
  
{/if}
