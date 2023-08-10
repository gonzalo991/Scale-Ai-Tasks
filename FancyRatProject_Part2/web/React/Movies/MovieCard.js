import React from 'react';

function MovieCard(props) {

    const { title, subtitle, image, explanation, text } = props;

    return (
        <div className="movie-card">
            <div className="card-header">
                <div className="card-header-text">
                    <h2 className="card-title">
                        {title}
                    </h2>
                    <span className="card-subtitle">
                        {subtitle}
                    </span>
                </div>
                <div className="card-header-image">
                    <img
                        className="card-header-image"
                        src={image}
                        alt={title}
                    />
                </div>
            </div>
            <div className="card-body">
                <p className="card-body-text">
                    {explanation}
                </p>
                <div className="card-body-button">
                    <button
                        className="card-body-button"
                    >
                        See more
                    </button>
                </div>
            </div>
        </div>
    );
}

export default MovieCard;