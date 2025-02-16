import { useState, useEffect } from "react";
import Login from "./components/Login";
import SignUp from "./components/SignUp";
import MainPage from "./components/MainPage";
import "./app.css";

function App() {
  const [userData, setUserData] = useState(null);
  const [isLogin, setIsLogin] = useState(false);
  const [page, setPage] = useState(false);

  useEffect(() => {
    const storedUser = localStorage.getItem("currentUser");
    if (storedUser) {
      setUserData(JSON.parse(storedUser));
      setIsLogin(true);
    }
  }, []);

  const isLoginHandle = (user) => {
    setIsLogin(true);
    setUserData(user);
    localStorage.setItem("currentUser", JSON.stringify(user));
  };

  const handleLogout = () => {
    setIsLogin(false);
    setUserData(null);
    localStorage.removeItem("currentUser");
    window.location.reload();
  };

  return (
    <div>
      {!isLogin && (
        <button onClick={() => setPage(!page)}>
          {page ? "Login" : "Sign Up"}
        </button>
      )}
      {!isLogin ? (
        page ? (
          <SignUp />
        ) : (
          <Login loginSucces={isLoginHandle} />
        )
      ) : (
        <MainPage user={userData} handleLogout={handleLogout} />
      )}
    </div>
  );
}

export default App;
