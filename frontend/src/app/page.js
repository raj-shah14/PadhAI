export default function Home() {
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Welcome to AI Learning Assistant</h1>
      <form>
        <input type="email" placeholder="Email" required />
        <input type="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
