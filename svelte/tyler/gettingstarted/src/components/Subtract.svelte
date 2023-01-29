<script lang="ts">
	import {counter} from "../store";
	import {count_val} from "../store";
	
	const subtract = () => {
		count_val.update(prev => --prev)
	}
</script>

<button on:click={counter.subtract}>subtract</button>
