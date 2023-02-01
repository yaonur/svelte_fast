<script lang="ts">
	export let item;
</script>

<div class="container">
	<h1>This is always rendered and the item value is:{item.value}</h1>
	<slot><h1>Default value in this slot if nothing passed in default slot</h1></slot>
	<slot name="slotOne" prop={item}>
		<h1>Default value in this slot if nothing passed in slotOne slot</h1>
	</slot>
	<slot name="slotTwo"><h1>Default value in this slot if nothing passed in slotTwo slot</h1></slot>
</div>

<style>
	.container {
		width: 100%;
		margin: auto;
	}
</style>
