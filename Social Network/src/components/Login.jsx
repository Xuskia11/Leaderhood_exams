import "../login.css"

const Login = ({ loginSucces }) => {

    const handleSubmit = (e) => {
        e.preventDefault();

        const email = e.target.email.value;
        const password = e.target.password.value;

        const storedUser = localStorage.getItem(email);

        if (storedUser){
            const parsedUser = JSON.parse(storedUser);
            if (parsedUser.password === password){
                alert(`Welcome ${parsedUser.name}`)
                loginSucces(parsedUser);
            } else {
                alert("Incorrect Password")
            }
        } else {
            alert("User not found")
        }
    }

    return (
        <div className="container">
            <div className="container2">
                <h1>Login</h1>
                <form className="form1" onSubmit={handleSubmit}>
                    <input type="text" placeholder="Email: " name="email"/>
                    <input type="password" placeholder="Password: " name="password"/>
                    <button>Login</button>
                </form>
            </div>
        </div>
        
    )
}

export default Login