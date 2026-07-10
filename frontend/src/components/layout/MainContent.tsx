import { Outlet } from "react-router-dom"

function MainContent() {

    return (

        <main className="flex-1 p-6">

            <Outlet />

        </main>

    )

}

export default MainContent