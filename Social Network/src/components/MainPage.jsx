import { useEffect, useState } from "react";
import "../mainpage.css";

const MainPage = ({ user, handleLogout }) => {
  const [posts, setPosts] = useState([]);
  const [visibility, setVisibility] = useState("public");
  const [postContent, setPostContent] = useState("");

  useEffect(() => {
    const storedPosts = JSON.parse(localStorage.getItem("posts")) || [];
    setPosts(storedPosts);
  }, []);

  const handlePostSubmit = (e) => {
    e.preventDefault();

    const newPost = {
      content: postContent,
      visibility: visibility,
      userEmail: user.email,
    };

    const updatedPosts = [...posts, newPost];
    setPosts(updatedPosts);

    localStorage.setItem("posts", JSON.stringify(updatedPosts));
    setPostContent("");
  };

  const filterPosts = posts.filter(
    (post) => post.visibility === "public" || post.userEmail === user.email
  );

  const handleDelete = (index) => {
    const updatedPosts = posts.filter((_, i) => i !== index);
    setPosts(updatedPosts);
    localStorage.setItem("posts", JSON.stringify(updatedPosts));
  };

  return (
    <div className="containerr">
      <div className="header">
        <h1>Welcome {user.name} to your profile</h1>
        <p style={{ marginBottom: 10 }}>
          Here you can see your posts and other features.
        </p>
        <button onClick={handleLogout}>Log Out</button>
      </div>
      <form className="form" onSubmit={handlePostSubmit}>
        <textarea
          className="textarea"
          value={postContent}
          onChange={(e) => setPostContent(e.target.value)}
          required
          placeholder="What's on your mind..."
        ></textarea>
        <div className="visibility">
          <label>
            Visibility :
            <select
              className="select"
              value={visibility}
              onChange={(e) => setVisibility(e.target.value)}
            >
              <option value="public">Public</option>
              <option value="private">Private</option>
            </select>
          </label>
        </div>
        <button>Submit</button>
      </form>

      <h1>Posts</h1>
      <div className="posts">
        {filterPosts.length > 0 ? (
          filterPosts.map((post, index) => (
            <div className="postcard" key={index}>
              <p>{post.content}</p>
              <b className="postvisibility">
                {post.visibility === "public" ? "Public" : "Private"}
              </b>
              <button onClick={() => handleDelete(index)}>Delete</button>
            </div>
          ))
        ) : (
          <p>No posts available</p>
        )}
      </div>
    </div>
  );
};

export default MainPage;
