<script lang="ts">
  import Icon from "@iconify/svelte";
  import Tooltip from "./Tooltip.svelte";
  
 let title = 'title';
	let isHovered = false;
	let x = 0;
  let y=0;

	function mouseOver(event,tooltip) {
		isHovered = true;
		x = event.pageX;
    y = event.pageY;
    console.log(tooltip.length)
    title=tooltip
  
	}

	function mouseMove(event) {
    		x = event.pageX;
    y = event.pageY;

	}

	function mouseLeave() {
		isHovered = false;
	}
  
</script>

<div class="absolute bottom-2 z-50 w-full overflow-hidden lg:bottom-8">
  <div class="container mx-auto">
    <div
      class="mx-auto flex h-[96px] w-full max-w-[460px]  items-center justify-between rounded-full bg-black/20 px-10 text-2xl text-white/50 backdrop-blur-2xl"
    >
        <a on:mouseover={(e)=>mouseOver(e,"Home")} on:mousemove={mouseMove} on:mouseleave={mouseLeave} href="/" class="flex h-[60px] w-[80px]  cursor-pointer items-center justify-center" >
          <Icon icon="ri:home-gear-line" />
        </a>
          <a on:mouseover={(e)=>mouseOver(e,"Projects")} on:mousemove={mouseMove} on:mouseleave={mouseLeave} href="/" class="flex h-[60px] w-[80px]  cursor-pointer items-center justify-center" >
          <Icon icon="ri:space-ship-line" />
        </a>
          <a on:mouseover={(e)=>mouseOver(e,"Contact")} on:mousemove={mouseMove} on:mouseleave={mouseLeave} href="/" class="flex h-[60px] w-[80px]  cursor-pointer items-center justify-center" >
          <Icon icon="ic:round-connect-without-contact" />
        </a>
    </div>
  </div>
</div>
{#if isHovered}
	<div class="absolute text-white w-[80px] max-w-[160px] text-center z-50 " style="top: {y-38}px; left: {x-title.length-34}px;">
		{title}
	</div>
 
{/if}


<style lang="postcss">
</style>
