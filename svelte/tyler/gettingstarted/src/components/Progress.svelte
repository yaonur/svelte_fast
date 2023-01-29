<script lang="ts">
	import {tweened} from "svelte/motion"
	import {cubicOut} from "svelte/easing";
	let duration=10000;
	
	const progress = tweened(0, {
		duration: 2000,
		easing:cubicOut,
	});
</script>
<button on:click={()=>progress.set(0)}>0%</button>
<button on:click={()=>progress.set(.5)}>50></button>
<button on:click={()=>progress.set(1,{duration})}>100%</button>

<div class="outer">
	<div class="inner" style="width:{$progress*100}%"></div>
</div>

<style>
	.inner, .outer {
		height: 40px;
		border-radius: 10px;
	}
	
	.outer {
		width: 80vw;
		margin: 30px auto;
		background-color: transparent;
		border: 1px solid white;
		
	}
	
	.inner {
		width: 40%;
		background-color: tomato;
	}
</style>