import { writable,get } from "svelte/store";


export const snippetStore=writable<CodeSnippet[]>([])

export function addSnippet(input:CodeSnippetInput){
	const snippets=get(snippetStore)
	snippetStore.update(()=>{
		return [{...input,favorite:false},...snippets]

	})
}

export function deleteSnippet(index:number){
	const snippets=get(snippetStore)
	snippetStore.update(()=>{
		return snippets.filter((_,i)=>i!==index)
	})
}

export function toggleFavorite(index:number){
	const snippets=get(snippetStore)

	snippetStore.update(()=>{
		return snippets.map((snippet,i)=>{
			if(i===index){
				return {...snippet,favorite:!snippet.favorite}
			}
			return snippet
		})
	})
}