import type { Actions } from '@sveltejs/kit';

export const actions: Actions = {
  default: async({cookies})=>{
    cookies.set("access","true")
  }
};
