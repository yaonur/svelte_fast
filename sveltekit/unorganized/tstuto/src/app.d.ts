// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
// and what to do when importing types
declare global {
	declare namespace App {
		// interface Locals {}
		interface PageData {
			snippets: CodeSnippet[];
		}
		// interface Error {}
		// interface Platform {}
	}
}

interface CodeSnippetInput {
	title: string;
	language: string;
	code: string;
}
interface CodeSnippet{
	title:string
	language:string
	code:string
	favorite:boolean
}
