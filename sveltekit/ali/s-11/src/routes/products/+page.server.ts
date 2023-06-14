import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';
export const load: PageServerLoad = async ({parent,fetch}) => {
	// console.log('Products Load function');
	// const parentData=await parent()
	// console.log(parentData)
	const response = await fetch('/api/products')
	if (response.ok) {
		const products = response.json()
		return { products };
	} 
	const erorJSON = await response.json();
	throw error(response.status, errorJSON.message)
};
