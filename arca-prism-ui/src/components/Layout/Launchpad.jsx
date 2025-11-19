import React from 'react';
import PrismTile from '../Tiles/PrismTile';
import { FlexBox, Title } from '@ui5/webcomponents-react';

const Launchpad = () => {
  return (
    <div>
      <Title level="H2">Finance</Title>
      <FlexBox wrap="Wrap">
        <PrismTile title="Chart of Accounts" icon="sap-icon://account-public" path="/app/finance/chart-of-accounts" />
        <PrismTile title="Journal Entry" icon="sap-icon://journal-entry" path="/app/finance/journal-entry" />
        <PrismTile title="Trial Balance" icon="sap-icon://business-objects-experience" path="/app/finance/trial-balance" />
      </FlexBox>
      <Title level="H2">HR</Title>
      <FlexBox wrap="Wrap">
        <PrismTile title="Employee Master" icon="sap-icon://employee" path="/app/hr/employees" />
      </FlexBox>
    </div>
  );
};

export default Launchpad;
