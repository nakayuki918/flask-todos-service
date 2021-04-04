import Head from 'next/head'
// import styles from '../styles/Home.module.css'
import axios, { AxiosInstance } from "axios"

export const apiClient: AxiosInstance = axios.create({
  baseURL: 'http://0.0.0.0:8000/',
  withCredentials: true
});

// axios.defaults.baseURL = 'http://localhost:3000';
// axios.defaults.headers.post['Content-Type'] = 'application/json;charset=utf-8';
// axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
export default function Home() {
  const createUser = async () => {
    try {
       await apiClient.post('/api/users', {
        username: 'nakayuki',
        password: 'Password#7',
        email: 'yuki.n.0918@gmail.com',
        bio: 'hello world'
      })
    } catch (e) {
      console.error(e)
    }
  }

  return (
    <div>
      <button onClick={createUser}>create user</button>
    </div>
  )
}
