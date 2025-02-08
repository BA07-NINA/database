import Sidebar from '@/components/Sidebar'
import Navbar from '@/components/Navbar'
import { createRootRoute, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/router-devtools'

export const Route = createRootRoute({
  component: () => (
    <div className='flex flex-col'>
        <Navbar />
      <div className='flex'>
    
        <Sidebar />
        <Outlet />
      </div>
    </div>
  ),
})