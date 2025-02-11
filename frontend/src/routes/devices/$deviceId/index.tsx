import { useState } from 'react';
import { audioFilesQueryOptions, deviceQueryOptions } from '@/api/query';
import DeviceNav from '@/components/pagenav/DeviceNav';
import { useSuspenseQuery } from '@tanstack/react-query';
import { createFileRoute, Link } from '@tanstack/react-router';

// Import table components and hooks from your UI and React Table libraries
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Button } from '@/components/ui/button';
import {
  type ColumnDef,
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
  type SortingState,
  useReactTable,
} from '@tanstack/react-table';
import { TbArrowsUpDown } from 'react-icons/tb';
import { AudioFile } from '@/types';

export const Route = createFileRoute('/devices/$deviceId/')({
  loader: async ({ params: { deviceId }, context: { queryClient } }) => {
    await queryClient.prefetchQuery(deviceQueryOptions(deviceId));
    await queryClient.prefetchQuery(audioFilesQueryOptions(deviceId));
    return { deviceId };
  },
  component: RouteComponent,
});

function RouteComponent() {
  const { deviceId } = Route.useParams();
  const { data: device } = useSuspenseQuery(deviceQueryOptions(deviceId));
  const { data: audioFiles } = useSuspenseQuery(audioFilesQueryOptions(deviceId));
  const [activeTab, setActiveTab] = useState<'details' | 'audioFiles'>('details');

  const columns: ColumnDef<AudioFile>[] = [
    {
      accessorKey: 'id',
      header: ({ column }) => (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          className="w-full justify-start"
        >
          ID
          <TbArrowsUpDown className="ml-2 h-4 w-4" />
        </Button>
      ),
      cell: ({ row }) => (
        <Link to="/devices/$deviceId/$audioFileId" params={{ deviceId: device.id, audioFileId: row.original.id }} className="text-blue-500 hover:underline">
          {row.original.id}
        </Link>
      ),
    },
    {
      accessorKey: 'config',
      header: 'Config',
    },
    {
      accessorKey: 'samplerate',
      header: ({ column }) => (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          className="w-full justify-start"
        >
          Sample Rate
          <TbArrowsUpDown className="ml-2 h-4 w-4" />
        </Button>
      ),
      cell: ({ row }) => `${row.original.samplerate} Hz`,
    },
    {
      accessorKey: 'fileLength',
      header: ({ column }) => (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          className="w-full justify-start"
        >
          File Length
          <TbArrowsUpDown className="ml-2 h-4 w-4" />
        </Button>
      ),
      // Note: If you need numerical sorting (e.g. sorting by duration in seconds)
      // you might want to provide a custom sortingFn that converts the "HH:MM:SS" string to seconds.
    },
    {
      accessorKey: 'fileSize',
      header: ({ column }) => (
        <Button
          variant="ghost"
          onClick={() => column.toggleSorting(column.getIsSorted() === 'asc')}
          className="w-full justify-start"
        >
          File Size (MB)
          <TbArrowsUpDown className="ml-2 h-4 w-4" />
        </Button>
      ),
      cell: ({ row }) => `${row.original.fileSize} MB`,
    },
  ];
  

  // Set up table state and instance for sorting and rendering
  const [sorting, setSorting] = useState<SortingState>([]);
  const table = useReactTable({
    data: audioFiles,
    columns,
    state: {
      sorting,
    },
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  return (
    <div>
      <DeviceNav
        deviceId={device.id}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {activeTab === 'details' && (
        <div>
          <h2>Device Details</h2>
          <p>ID: {device.id}</p>
          {/* Render additional device details as needed */}
        </div>
      )}

      {activeTab === 'audioFiles' && (
        <div>
          <div className="rounded-md border m-5 shadow-md">
            <Table>
              <TableHeader>
                {table.getHeaderGroups().map((headerGroup) => (
                  <TableRow key={headerGroup.id}>
                    {headerGroup.headers.map((header) => (
                      <TableHead key={header.id} className="px-0 py-0">
                        {header.isPlaceholder
                          ? null
                          : flexRender(
                              header.column.columnDef.header,
                              header.getContext()
                            )}
                      </TableHead>
                    ))}
                  </TableRow>
                ))}
              </TableHeader>
              <TableBody>
                {table.getRowModel().rows.map((row) => (
                  <TableRow key={row.id}>
                    {row.getVisibleCells().map((cell) => (
                      <TableCell key={cell.id} className="px-4 py-2">
                        {flexRender(
                          cell.column.columnDef.cell,
                          cell.getContext()
                        )}
                      </TableCell>
                    ))}
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        </div>
      )}
    </div>
  );
}

export default RouteComponent;
