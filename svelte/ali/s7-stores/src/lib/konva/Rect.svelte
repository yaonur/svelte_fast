<script lang="ts">
  import Konva from "konva";
  import { getContext, onDestroy } from "svelte";
  import { layerKey } from "./context-keys";

  //   export let x: number = undefined;
  //   export let y: number = undefined;
  //   export let width: number = undefined;
  //   export let height: number = undefined;
  //   export let fill: string = undefined;
  //   export let stroke = undefined;
  //   export let strokeWidth = undefined;

  //   const rect = new Konva.Rect({
  //     x,
  //     y,
  //     width,
  //     height,
  //     fill,
  //     stroke,
  //     strokeWidth,
  //   });
  //   $: rect.setAttrs({
  // 	x,
  // 	y,
  // 	width,
  // 	height,
  // 	fill,
  // 	stroke,
  // 	strokeWidth,
  //   })
  const rect = new Konva.Rect( $$props );
  $: rect.setAttrs( $$props );

  interface Layercontext {
    getLayer: () => any; // replace any with the actual return type of getLayer
  }

  const { getLayer }: Layercontext = getContext(layerKey);
  const layer = getLayer();
  layer.add(rect);
  onDestroy(() => {
    rect.destroy();
  });
</script>
