import type { PageServerLoad } from './$types';
export const load: PageServerLoad = async ({parent}) => {
	// console.log('Products Load function');
	const parentData=await parent()
	// console.log(parentData)
	const products = await (await import('$lib/dumy-products.json')).default;
	return { products };
	// return {products:[{id:1},{id:2},{id:3}]}
};
