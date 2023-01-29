<script lang="ts">
	import {counter} from "../store";
	import {count_val} from "../store";
	
	const add = () => {
		count_val.update(prev => prev += 1)
	}
	const counter_add = () => {
		console.log("counter add pressed")
		counter.add()
	}

</script>

<button on:click={counter_add}>add</button>
