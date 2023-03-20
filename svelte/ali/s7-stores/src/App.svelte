<script lang="ts">
  import { onMount } from "svelte";
  import Head from "./lib/components/Head.svelte";
  import Settings from "./lib/pages/Settings.svelte";
  import Home from "./lib/pages/Home.svelte";
  import Context from "./lib/pages/Context.svelte";
  onMount(() => {
    onRouteChange();
  });
  let page;
  function onRouteChange() {
    const path = window.location.hash.slice(1);
    if (path === "/") {
      page = "home";
    } else if (path === "/settings") {
      page = "settings";
    } else if (path === "/context") {
      page = "context";
    } else {
      window.location.hash = "/";
    }
  }
</script>

<svelte:window on:hashchange={onRouteChange} />
<Head></Head>


<nav>
  <a href="#/">Home</a>
  <a href="#/settings">Settings</a>
  <a href="#/context">Context</a>
</nav>

{#if page === "home"}
  <Home />
{:else if page === "settings"}
  <Settings />
  {:else if page === "context"}
  <Context />

{/if}

