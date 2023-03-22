import mitt from 'mitt';
const emitter = mitt();

export default emitter;
export function isValidJwt(jwt) {
  console.log(jwt)
  if (!jwt || jwt.split(".").length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split(".")[1]));
  const exp = new Date(data.exp * 1000); // JS deals with dates in milliseconds since epoch
  const now = new Date();
  return now < exp;
}
