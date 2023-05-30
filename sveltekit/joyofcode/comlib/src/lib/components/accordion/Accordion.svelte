<script lang="ts">
	import {getAccordionOptions,setAccordionOptions} from './context'


	export let colapse = false;
	export let className=''
	setAccordionOptions({colapse})

	
</script>

<div class="w-main p-main text-white  bg-bg border-slate-700 shadow-slate-700 {className}">
	<slot />
</div>
