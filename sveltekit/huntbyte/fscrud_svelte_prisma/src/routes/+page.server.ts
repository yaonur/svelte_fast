import type {Actions, PageServerLoad} from "./$types"
import {prisma} from "../lib/server/prisma"
import {fail} from "@sveltejs/kit"


export const load: PageServerLoad = async () => {
    return {
        articles: await prisma.article.findMany()
    }
}

export const actions: Actions = {

    createArticle: async ({request}) => {
        const {title, content} = Object.fromEntries(await request.formData()) as { title: string, content: string }
        try {
            await prisma.article.create({
                data: {
                    title,
                    content
                }
            })
        } catch (err) {
            console.error(err)
            return fail(500, {message: 'Could not create the article'})
        }

        return {
            status: 201
        }
    },

    deleteArticle: async (req) => {
        const id = req.url.searchParams.get("id")
        if (!id) {
            return fail(400, {message: "Invalid url"})
        }
        try {
            await prisma.article.delete({
                where: {
                    id: Number(id)
                }
            })
        } catch (err) {
            console.log(err)
            return fail(500, {message: "Something went wrong deleting article"})
        }

        return {
            status: 200,
        }

    }
}