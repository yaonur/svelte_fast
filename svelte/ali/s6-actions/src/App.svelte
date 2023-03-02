<script lang="ts">
  import { onMount } from "svelte";
  import tippy from "tippy.js";
  import "tippy.js/dist/tippy.css";
  import longpress from "./lib/actions/longpress";
  import tooltip from "./lib/actions/tooltip";

  let button;

  onMount(() => {
    tippy(".tooltip", {
      content: "tooltip content",
    });
    tippy(button, {
      content: "tooltip content",
    });
  });

  let showButton = true;
  let duration = 1000;
</script>

<label><input type="checkbox" bind:checked={showButton} />Toggle</label>
{#if showButton}
  <button
    class="tooltip"
    data-tippy-content="Some tip text"
    use:longpress={{ duration: duration }}
    on:longpress={() => {
      alert("pressed");
    }}
    >Hey
  </button>
{/if}
<label>
  <input type="range" bind:value={duration} max={4000} step={100} />{duration}ms
</label>

<button bind:this={button}>Button</button>
<button use:tooltip={{ content: "some tooltip text" }}>Action Button</button>

<style lang="postcss">
</style>
