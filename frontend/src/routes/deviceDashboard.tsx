import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/deviceDashboard')({
  component: RouteComponent,
})

function RouteComponent() {
  return <div>Hello "/deviceDashboard"!</div>
}
