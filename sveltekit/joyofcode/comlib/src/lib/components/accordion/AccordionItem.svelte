<script lang="ts">
	import {slide} from 'svelte/transition'
	import { getContext } from 'svelte';
	import { getAccordionOptions } from './context';
	export let open = false;

	const componentId = crypto.randomUUID();

	const{colapse,activeComponentId}= getAccordionOptions()

	

	function setActive() {
		$activeComponentId = componentId;
	}

	function handleClick() {
		colapse ? setActive() : toggleOpen();
	}
	function toggleOpen() {
		open = !open;
	}
	$: open && colapse && setActive();
	$: isActive = $activeComponentId === componentId;
	$: isOpen = colapse ? isActive : open;
</script>

<div class="">
	<button
		class=" p-main flex  w-full cursor-pointer justify-between text-inherit transition duration-500 ease-in-out hover:bg-gray-600"
		on:click={handleClick}
		aria-expanded={isOpen}
		aria-controls="accordion-{componentId}"
	>
		<div>
			<slot name="title" />
		</div>
		<div class="{open ? 'rotate-90' : ''} transition duration-500">&#x1F449;</div>
	</button>
	{#if isOpen}
		<!-- content here -->
		<div transition:slide|local
		role="region"
		aria-hidden={!isOpen}
		aria-labelledby="accordion-{componentId}"
		>
			<slot name="content" />
		</div>

	{/if}
</div>
