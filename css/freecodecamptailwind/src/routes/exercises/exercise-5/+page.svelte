<script lang="ts">
	import Exercise from './Exercise.svelte';
	import Solution from './Solution.svelte';
</script>

<div class="flex gap-1">
	<div class="basis-1/2 border border-gray-900">
		<Exercise />
	</div>
	<div class="basis-1/2 border border-gray-900">
		<Solution />
	</div>
</div>
