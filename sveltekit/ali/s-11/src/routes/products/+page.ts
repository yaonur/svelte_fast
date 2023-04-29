import type { PageLoad } from './$types';

export const load: PageLoad = (async ({data}) => {
    // console.log(data)
    return {products:data.products,title:"Products Page"};
}) 