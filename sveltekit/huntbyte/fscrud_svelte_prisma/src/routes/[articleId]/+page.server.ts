import type {PageServerLoad,Actions} from "../../../.svelte-kit/types/src/routes/$types";
import {prisma} from '$lib/server/prisma'
import  { error} from "@sveltejs/kit"



export const load: PageServerLoad = async ({params}) => {
    const getArticle = async () => {
        const article = await prisma.article.findUnique({
            where: {
                id: Number(params.articleId)
            }
        })
        if (!article) {
            throw error(404, "Article not found")
        }
        return article

    }

    return {
        article: getArticle()
    }
}
export const actions:Actions={

}