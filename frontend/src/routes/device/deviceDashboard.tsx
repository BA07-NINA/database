import DeviceNav from '@/components/DeviceNav'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/device/deviceDashboard')({
  component: RouteComponent,
})

function RouteComponent() {
  return <DeviceNav />
}
