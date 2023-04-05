
export const load = (async (event) => {
    console.log("+layout.server.ts: load() running")
    return {
        session: await event.locals.getSession(),
    };
}) 