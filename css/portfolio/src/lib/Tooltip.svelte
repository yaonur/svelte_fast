<script>
	export let title = '';
	let isHovered = false;
	let x = 0;
	let w = 0;

	function mouseOver(event) {
		isHovered = true;
		x = event.layerX;
		w = event.srcElement.clientWidth;
		console.log(event);
	}

	function mouseMove(event) {
		x = event.layerX
		w = event.srcElement.clientWidth;
	}

	function mouseLeave() {
		isHovered = false;
	}
</script>

<div
 
	class="transform transition-all duration-200 ease-in-out hover:scale-110 hover:shadow-lg"
	on:mouseover={mouseOver}
	on:mouseleave={mouseLeave}
	on:mousemove={mouseMove}
>
  <div class="-z-10">
	<slot />
  </div>
</div>

