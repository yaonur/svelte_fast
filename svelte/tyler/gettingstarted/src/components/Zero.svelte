<script lang="ts">
	import {counter} from "../store";
	// import {count_val} from "../store";
	
	// const zero = () => {
	// 	console.log("zero pressed")
	// 	count_val.set(0)
	// }
</script>

<button on:click={counter.reset}>reset</button>