import type { Handle } from '@sveltejs/kit';

// @ts-ignore
export const handle = async ({ event, resolve }) => {
    console.log(event.route)
    console.log(event.route.id?.startsWith("/(app)"))
    const theme = event.cookies.get('siteTheme');

    // @ts-ignore
    const response = await resolve(event, {
        transformPageChunk: ({ html }) => html.replace('data-theme=""', `data-theme="${theme}"`)
    });
    return response;
};
