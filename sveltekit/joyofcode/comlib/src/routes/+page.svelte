<script lang="ts">
	import { Accordion, AccordionItem } from '$comp/accordion';
	const items = [
		{ title: 'Item 1', content: 'Content 1' },
		{ title: 'Item 2', content: 'Content 2' },
		{ title: 'Item 3', content: 'Content 3' },
		{ title: 'Item 4', content: 'Content 4' },
		{ title: 'Item 5', content: 'Content 5' }
	];
</script>

<Accordion colapse className="text-red-200 bg-bg">
	{#each items as item,i}
		<!-- content here -->
		<AccordionItem open={i===0}>
			<svlete:fragment slot="title"> {item.title}</svlete:fragment>
			<svlete:fragment slot="content"> {item.content}</svlete:fragment>
		</AccordionItem>
	{/each}
</Accordion>
