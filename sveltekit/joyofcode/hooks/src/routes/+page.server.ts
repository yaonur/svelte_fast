import type {PageServerLoad} from './$types';
import type {Actions} from "./$types";

export const load:PageServerLoad =async()=>{
  // throw new Error("Banana")
  console.log('banana')
}