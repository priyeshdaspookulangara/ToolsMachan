import React from 'react';
import { Table, TableColumn, TableRow, TableCell, BusyIndicator, Bar, Pagination } from '@ui5/webcomponents-react';

const PrismTable = ({ columns, data, isLoading, page, totalPages, onPageChange }) => {
  if (isLoading) {
    return <BusyIndicator active />;
  }

  if (!data || data.length === 0) {
    return <div>No data available.</div>;
  }

  return (
    <>
      <Table
        columns={columns.map((col, index) => (
          <TableColumn key={index} style={{ width: col.width || 'auto' }}>
            <span>{col.header}</span>
          </TableColumn>
        ))}
        footer={
          <Bar endContent={
            <Pagination
              currentPage={page}
              onPageChange={onPageChange}
              totalPages={totalPages}
            />
          } />
        }
      >
        {data.map((row, rowIndex) => (
          <TableRow key={rowIndex}>
            {columns.map((col, colIndex) => (
              <TableCell key={colIndex}>
                <span>{row[col.accessor]}</span>
              </TableCell>
            ))}
          </TableRow>
        ))}
      </Table>
    </>
  );
};

export default PrismTable;
