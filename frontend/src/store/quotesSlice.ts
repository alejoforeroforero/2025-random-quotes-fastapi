import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import api from '../api/config';

interface Quote {
  text: string;
  author: string;
}

interface QuotesState {
  quotes: Quote[];
  currentQuote: Quote | null;
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
}

const initialState: QuotesState = {
  quotes: [],
  currentQuote: null,
  status: 'idle',
  error: null
};

export const fetchRandomQuote = createAsyncThunk(
  'quotes/fetchRandom',
  async () => {
    const response = await api.get<Quote>('/quotes/random');
    return response.data;
  }
);

export const fetchAllQuotes = createAsyncThunk(
  'quotes/fetchAll',
  async () => {
    const response = await api.get<Quote[]>('/quotes');
    return response.data;
  }
);

const quotesSlice = createSlice({
  name: 'quotes',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      // Handle fetchRandomQuote
      .addCase(fetchRandomQuote.pending, (state) => {
        state.status = 'loading';
      })
      .addCase(fetchRandomQuote.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.currentQuote = action.payload;
        state.error = null;
      })
      .addCase(fetchRandomQuote.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message || 'Failed to fetch quote';
      })
      // Handle fetchAllQuotes
      .addCase(fetchAllQuotes.fulfilled, (state, action) => {
        state.quotes = action.payload;
      });
  }
});

export default quotesSlice.reducer;
