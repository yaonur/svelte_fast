import type { LayoutServerLoad } from './$types';

export const load:LayoutServerLoad = (async () => {
    const user ={name:"john",id:1}
    return {user};
}) 