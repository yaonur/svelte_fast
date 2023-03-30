<script lang ts>
  import { onMount } from "svelte";
  import { Stage, Layer, Rect } from "../konva";
  let showCanvas = true;
  let x =20

</script>

<input type="checkbox" bind:checked={showCanvas} />
<input type="range" bind:value={x} min={20} max={300} />

<!-- content here -->
{#if showCanvas}
<Stage width={300} height={400}>
  <Layer>
      <Rect {x} y={20} width={100} height={100} fill="blue" />
	</Layer>
	<Layer draggable={true} {x}>
		<Rect x={30} y={30} width={100} height={100} fill="red" />
	</Layer>
</Stage>
{/if}
