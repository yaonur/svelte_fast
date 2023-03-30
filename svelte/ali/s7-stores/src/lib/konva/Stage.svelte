<script lang="ts">
	import { stageKey } from './context-keys';
  import Konva from "konva";
  import { onDestroy, onMount, setContext } from "svelte";

//   export let width;
//   export let height;

  let container;
  let stage;
  $: if(stage) stage.setAttrs($$props);

  setContext(stageKey, {
	getStage() {
	  return stage;
	},
  });
  onMount(() => {
    stage = new Konva.Stage({
      container,
     ...$$props
    });
  });
  onDestroy(() => {
	if(stage) stage.destroy();
  });
</script>

<div bind:this={container}>
 {#if stage}
	 <slot />
 {/if}
</div>
