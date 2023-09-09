import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentDB {
    public static void main(String[] args) {
        String dbUrl = "jdbc:mysql://localhost:3306/schooldb";
        String dbUser = "root";
        String dbPass = "password";
        String sql = "INSERT INTO STUDENT (NAME, AGE, GENDER) VALUES (?, ?, ?)";
        

        try {
            // Step 1: Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 2: Open a connection
            Connection conn = DriverManager.getConnection(dbUrl, dbUser, dbPass);

            // Step 3: Create a prepared statement
            PreparedStatement pstmt = conn.prepareStatement(sql);

            // Step 4: Add the student details
            pstmt.setString(1, "John Smith");
            pstmt.setInt(2, 20);
            pstmt.setString(3, "Male");

            // Step 5: Execute the insertion
            pstmt.executeUpdate();

            // Step 6: Close the resources
            pstmt.close();
            conn.close();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}