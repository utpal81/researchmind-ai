import { Link } from "react-router-dom"

function Sidebar() {

    return (

        <aside className="w-64 border-r p-4">

            <nav className="space-y-4">

                <Link
                    to="/"
                    className="block"
                >
                    Dashboard
                </Link>

                <Link
                    to="/upload"
                    className="block"
                >
                    Upload
                </Link>

                <Link
                    to="/chat"
                    className="block"
                >
                    Chat
                </Link>

            </nav>

        </aside>

    )

}

export default Sidebar