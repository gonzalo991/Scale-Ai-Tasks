import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Movie {
    private String title;
    private String director;
    private double duration;

    public Movie(String title, String director, double duration) {
        this.title = title;
        this.director = director;
        this.duration = duration;
    }

    public String getTitle() {
        return title;
    }

    public String getDirector() {
        return director;
    }

    public double getDuration() {
        return duration;
    }

    @Override
    public String toString() {
        return "Movie [title=" + title + ", director=" + director + ", duration=" + duration + "]";
    }
}