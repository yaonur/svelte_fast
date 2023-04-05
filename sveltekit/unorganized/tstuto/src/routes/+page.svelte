<script lang="ts">
	import CodeSnippetCard from '$comp/CodeSnippetCard.svelte';
	import { addSnippet, snippetStore } from '$stores/SnippetStore';
	import type { PageData } from './$types';
	let formData: CodeSnippetInput = {
		title: '',
		language: 'html',
		code: ''
	};
	export let data: PageData;
	snippetStore.set(data.snippets);
</script>

<div class="flex justify-center">
	<div class="grid min-w-full grid-cols-1 gap-4 md:min-w-[750px]">
		<h3 class="py-6 text-center">Create a code snipped</h3>
		<div class="card text-token w-full space-y-4 p-4">
			<label class="label">
				<span>Snippet Title</span>
				<input
					type="text"
					class="input"
					placeholder="Enter title here.."
					bind:value={formData.title}
				/>
			</label>
			<label class="label">
				<span>Programming Language</span>
				<select name="" id="" class="select" bind:value={formData.language}>
					<option value="html">HTML</option>
					<option value="css">CSS</option>
					<option value="typescript">TypeScript</option>
				</select>
			</label>
			<label class="label">
				<span>Code Snippet</span>
				<textarea
					class="textarea"
					cols="30"
					rows="4"
					placeholder="Enter your snippet code here..."
					bind:value={formData.code}
				/>
			</label>
			<button type="button" class="btn variant-filled-primary btn-sm" on:click={()=>{addSnippet(formData)}}>Add Snippet</button>
		</div>
		<h2>My snippets</h2>
		{#each $snippetStore as snippet, index}
			<!-- content here -->
			<CodeSnippetCard {snippet} {index} />
		{/each}
	</div>
</div>
