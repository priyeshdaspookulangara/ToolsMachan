import React from 'react';
import { ShellBar, ShellBarItem } from '@ui5/webcomponents-react';
import { SideNavigation, SideNavigationItem } from '@ui5/webcomponents-react';
import { Outlet, useNavigate } from 'react-router-dom';

const PrismAppShell = () => {
  const navigate = useNavigate();

  const handleNavigation = (e) => {
    navigate(e.detail.item.dataset.path);
  };

  return (
    <>
      <ShellBar
        primaryTitle="ARCA Prism UI"
        logo={<img src="https://sap.github.io/ui5-webcomponents/assets/images/sap-logo-svg.svg" alt="SAP Logo" />}
      >
        <ShellBarItem icon="add" text="Add" />
      </ShellBar>
      <div style={{ display: 'flex' }}>
        <SideNavigation onSelectionChange={handleNavigation}>
          <SideNavigationItem text="Home" icon="home" data-path="/" />
          <SideNavigationItem text="Finance" icon="sap-icon://account" data-path="/app/finance/chart-of-accounts" />
          <SideNavigationItem text="HR" icon="sap-icon://hr-approval" data-path="/app/hr/employees" />
        </SideNavigation>
        <main style={{ flexGrow: 1, padding: '2rem' }}>
          <Outlet />
        </main>
      </div>
    </>
  );
};

export default PrismAppShell;
