
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchRandomQuote } from './store/quotesSlice';
import type { RootState, AppDispatch } from './store/store';
import './App.css';

function App() {
  const dispatch = useDispatch<AppDispatch>();
  const { currentQuote, status, error } = useSelector((state: RootState) => state.quotes);

  useEffect(() => {
    dispatch(fetchRandomQuote());
  }, [dispatch]);

  const handleNewQuote = () => {
    dispatch(fetchRandomQuote());
  };

  const tweetQuote = () => {
    if (!currentQuote) return '#';
    const tweetText = encodeURIComponent(`"${currentQuote.text}" - ${currentQuote.author}`);
    return `https://twitter.com/intent/tweet?text=${tweetText}`;
  };

  if (status === 'loading') {
    return <div className="container">Loading...</div>;
  }

  if (status === 'failed') {
    return <div className="container">Error: {error}</div>;
  }

  return (
    <div className="container">
      <div id="quote-box">
        {currentQuote && (
          <>
            <div id="text">"{currentQuote.text}"</div>
            <div id="author">- {currentQuote.author}</div>
            <div className="buttons">
              <a
                id="tweet-quote"
                href={tweetQuote()}
                target="_blank"
                rel="noopener noreferrer"
              >
                Tweet Quote
              </a>
              <button id="new-quote" onClick={handleNewQuote}>
                New Quote
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
