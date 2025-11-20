import create from 'zustand';
import api from '../../../core/api/api';

const useChartOfAccountsStore = create((set) => ({
  accounts: [],
  isLoading: false,
  error: null,
  page: 1,
  totalPages: 1,
  searchTerm: '',

  fetchAccounts: async (page = 1, searchTerm = '') => {
    set({ isLoading: true, error: null, page, searchTerm });
    try {
      const response = await api.get(`/api/finance/accounts/?page=${page}&description__icontains=${searchTerm}`);
      const totalPages = Math.ceil(response.data.count / 10); // Assuming 10 items per page
      set({ accounts: response.data.results, totalPages, isLoading: false });
    } catch (error) {
      set({ error: error.message, isLoading: false });
    }
  },
}));

export default useChartOfAccountsStore;
