import { error,redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load = (async ({params}) => {
    const id =+params.id

    if(!isNaN(id)){
        const products = await (await import('$lib/dumy-products.json')).default;
        const product=products.products.find(p=>p.id===id )
        return {product,title:`Product ${product?.title}`};
}
else {
    throw error(404,"Product not found")
    // throw redirect(301,"/products")
}

}) satisfies PageServerLoad;