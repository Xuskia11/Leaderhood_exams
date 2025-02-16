import "../signup.css"

const SignUp = () => {

    const handleSubmit = (e) => {
        e.preventDefault();

        const userInfo = {
            name: e.target.username.value,
            email: e.target.email.value,
            password: e.target.password.value
        }

        // Save userInfo in localStorage
        const storedUser = localStorage.getItem(userInfo.email);
        if (storedUser){
            alert("This account already existed");
        } else {
            localStorage.setItem(userInfo.email, JSON.stringify(userInfo));
            alert("Account succesfully created!!!")
        }
    }

    return (
        <div className="container">
            <div className="container2">
                <h1>Sign Up</h1>
                <form className="form1" onSubmit={handleSubmit}>
                    <input type="text" placeholder="Username" name="username" required/>
                    <input type="email" placeholder="Email: " name="email" required/>
                    <input type="password" placeholder="Password" name="password" required/>
                    <button>Sign Up</button>
                </form>
            </div>
        </div>
        
    )
}


export default SignUp;