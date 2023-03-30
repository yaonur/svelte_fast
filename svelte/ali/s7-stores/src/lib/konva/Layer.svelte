<script lang='ts'> 
	import SlottedComponent from './../../../../../../sveltekit/consultingninja/firstlook/src/lib/SlottedComponent.svelte';
	import Layer from './Layer.svelte';
import Konva from "konva"
import {getContext, onDestroy, setContext} from "svelte"
import {stageKey,layerKey} from "./context-keys"

// export let draggable=undefined

const {getStage} = getContext(stageKey)
const stage = getStage()
const layer = new Konva.Layer($$props)
$:layer.setAttrs($$props)
stage.add(layer)
setContext(layerKey, {
	getLayer() {
		return layer
	},
})
onDestroy(()=>{
	layer.destroy()
  })

</script>

<slot/>