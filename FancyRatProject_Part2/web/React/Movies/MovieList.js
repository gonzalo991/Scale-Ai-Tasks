import React from 'react';
import MovieCard from './MovieCard';

function MovieList(props) {

    const { movies } = props;

    return (
        <div className="movie-list">
            {movies.map(movie => (
                <MovieCard key={movie.id} props={...movie} />
            ))}
        </div>
    );
}

export default MovieList;