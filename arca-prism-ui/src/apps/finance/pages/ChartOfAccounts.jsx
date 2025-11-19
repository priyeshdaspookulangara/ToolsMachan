import React, { useEffect, useState } from 'react';
import PrismTable from '../../../components/PrismTable/PrismTable';
import useChartOfAccountsStore from '../stores/chartOfAccountsStore';
import { Title, Input, Bar, Button } from '@ui5/webcomponents-react';

const ChartOfAccounts = () => {
  const { accounts, isLoading, error, page, totalPages, fetchAccounts } = useChartOfAccountsStore();
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchAccounts(page, searchTerm);
  }, [fetchAccounts, page]);

  const handlePageChange = (e) => {
    fetchAccounts(e.detail.page, searchTerm);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearch = () => {
    fetchAccounts(1, searchTerm); // Reset to page 1 for new search
  };

  const columns = [
    { header: 'Account ID', accessor: 'id', width: '100px' },
    { header: 'Description', accessor: 'description', width: '300px' },
    { header: 'Type', accessor: 'type', width: '150px' },
    { header: 'Is Active', accessor: 'isActive', width: '100px' },
  ];

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <Title>Chart of Accounts</Title>
      <Bar
        startContent={
          <>
            <Input
              placeholder="Search by description..."
              value={searchTerm}
              onInput={handleSearchChange}
            />
            <Button onClick={handleSearch} style={{ marginLeft: '8px' }}>Search</Button>
          </>
        }
      />
      <PrismTable
        columns={columns}
        data={accounts}
        isLoading={isLoading}
        page={page}
        totalPages={totalPages}
        onPageChange={handlePageChange}
      />
    </div>
  );
};

export default ChartOfAccounts;
