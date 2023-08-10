import React from 'react';
import { useHistory } from 'react-router-dom';
import { useParams } from 'react-router';
import MovieDetails from './MovieDetails';

function MovieDetailsPage(props) {
    const { movieId } = useParams();
    const history = useHistory();

    return (
        <div className="movie-details-page">
            <h1>Movie Details</h1>
            <MovieDetails movieId={movieId} onBackClick={() => history.goBack()} />
        </div>
    );
}

export default MovieDetailsPage;