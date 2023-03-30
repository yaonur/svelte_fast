<script lang="ts">
  import { onMount } from "svelte";
  import Head from "./lib/components/Head.svelte";
  import Settings from "./lib/pages/Settings.svelte";
  import Home from "./lib/pages/Home.svelte";
  import Context from "./lib/pages/Context.svelte";
  import KonvaPage from "./lib/pages/KonvaPage.svelte";
  import ModuleContext from "./lib/pages/ModuleContext.svelte";
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
    } else if (path === "/module") {
      page = "module";
    } else if (path === "/konva") {
      page = "konva";
    } else {
      window.location.hash = "/";
    }
  }
</script>

<svelte:window on:hashchange={onRouteChange} />
<Head />

<nav>
  <a href="#/">Home</a>
  <a href="#/settings">Settings</a>
  <a href="#/context">Context</a>
  <a href="#/konva">Konva</a>
  <a href="#/module">Module</a>
</nav>

{#if page === "home"}
  <Home />
{:else if page === "settings"}
  <Settings />
{:else if page === "context"}
  <Context />
{:else if page === "module"}
  <ModuleContext />
{:else if page === "konva"}
  <KonvaPage />
{/if}
