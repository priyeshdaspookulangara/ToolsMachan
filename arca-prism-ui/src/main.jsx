import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PrismAppShell from './components/Layout/PrismAppShell';
import Launchpad from './components/Layout/Launchpad';
import ChartOfAccounts from './apps/finance/pages/ChartOfAccounts';
import '@ui5/webcomponents/dist/Assets.js';
import '@ui5/webcomponents-fiori/dist/Assets.js';
import 'fundamental-styles/dist/fundamental-styles.css';

const JournalEntryPage = () => <div><h2>Journal Entry</h2></div>;
const TrialBalancePage = () => <div><h2>Trial Balance</h2></div>;
const EmployeeMasterPage = () => <div><h2>Employee Master</h2></div>;

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<PrismAppShell />}>
          <Route index element={<Launchpad />} />
          <Route path="app/finance/chart-of-accounts" element={<ChartOfAccounts />} />
          <Route path="app/finance/journal-entry" element={<JournalEntryPage />} />
          <Route path="app/finance/trial-balance" element={<TrialBalancePage />} />
          <Route path="app/hr/employees" element={<EmployeeMasterPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
