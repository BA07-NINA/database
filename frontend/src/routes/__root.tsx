import Sidebar from '@/components/Sidebar'
import { createRootRoute, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/router-devtools'

export const Route = createRootRoute({
  component: () => (
    <div className='flex flex-col'>
      <div className='min-w-full min-h-10 bg-green-500'></div>
      <div className='flex'>
        <Sidebar />
        <Outlet />
      </div>
    </div>
  ),
})