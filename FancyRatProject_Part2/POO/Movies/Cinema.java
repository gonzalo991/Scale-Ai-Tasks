package Movies;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Cinema {
    public static void main(String[] args) {
        List<Movie> movieList = movieMenu();

        System.out.println("Movies created:");
        for (Movie movie : movieList) {
            System.out.println("Title: " + movie.getTitle() +
                    ", Director: " + movie.getDirector() +
                    ", Duration: " + movie.getDuration() + " hours");
        }

    }

    public static List<Movie> movieMenu() {
        Scanner scanner = new Scanner(System.in).useDelimiter(" ");
        List<Movie> movieList = new ArrayList<>();

        while (true) {
            System.out.print("Do you want to create a new movie? (yes/no): ");
            String response = scanner.nextLine();

            if (!response.equalsIgnoreCase("yes")) {
                scanner.close();
                return movieList;
            }

            System.out.print("Enter the title of the movie: ");
            String title = scanner.nextLine();

            System.out.print("Enter the director of the movie: ");
            String director = scanner.nextLine();

            System.out.print("Enter the duration of the movie in hours: ");
            double duration = Double.parseDouble(scanner.nextLine());

            Movie newMovie = new Movie(title, director, duration);
            movieList.add(newMovie);

            System.out.print("Do you want to create another movie? (yes/no): ");
            response = scanner.nextLine();
        }
    }
}