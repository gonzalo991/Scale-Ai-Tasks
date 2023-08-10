import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

function MovieDetails(props) {
    const { id } = props;
    const [description, setDescription] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get(`/api/movie/${id}`)
            .then(response => response.data)
            .then(data => {
                setDescription(data);
                setLoading(false);
            })
            .catch(error => {
                console.error("Error fetching movie details:", error);
                setError("An error occurred while fetching movie details.");
                setLoading(false);
            });
    }, [id]);

    const handleBackClick = () => {
        if (props.onBackClick) {
            props.onBackClick();
        }
    };

    return (
        <div className="movie-details">
            {loading ? (
                <p>Loading...</p>
            ) : error ? (
                <p>{error}</p>
            ) : (
                <>
                    <h1 className="movie-title">
                        {description.title}
                    </h1>
                    <div className="movie-image">
                        <img alt={description.explanation} src={description.image} />
                    </div>
                    <h3 className="movie-title">
                        {description.subtitle}
                    </h3>
                    <p className="movie-description">
                        {description.text}
                    </p>
                    <div className="movie-button">
                        <button
                            className="back-button"
                            onClick={handleBackClick}
                        >
                            Back
                        </button>
                    </div>
                </>
            )}
        </div>
    );
}

MovieDetails.propTypes = {
    id: PropTypes.number.isRequired,
    onBackClick: PropTypes.func
};

export default MovieDetails;