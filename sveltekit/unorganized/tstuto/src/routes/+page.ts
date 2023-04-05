import type { PageLoad } from './$types';

export const load = (async () => {
    return {
        snippets:[
            {
                title: 'Hello World',
                language: 'html',
                code: '<h1>Hello World</h1>',
                favorite:false
    
            },
            {
                title: 'Second snippet',
                language: 'html',
                code: '<h2>Second snipet</h1>',
                favorite:false
    
            }
        ]
    };
}) satisfies PageLoad;