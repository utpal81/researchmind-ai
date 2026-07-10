import Header from "./Header"
import Sidebar from "./Sidebar"
import MainContent from "./MainContent"

function AppLayout() {

    return (

        <div className="min-h-screen flex flex-col">

            <Header />

            <div className="flex flex-1">

                <Sidebar />

                <MainContent />

            </div>

        </div>

    )

}

export default AppLayout