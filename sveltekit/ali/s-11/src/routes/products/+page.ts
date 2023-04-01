import type { PageLoad } from './$types';
export const load: PageLoad = async () => {
	// console.log('Products Load function');
	const products = await (await import('$lib/dumy-products.json')).default;
	return { products };
	// return {products:[{id:1},{id:2},{id:3}]}
};
