import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class StudentList {
    public static void main(String[] args) {
        // Database connection information
        String dbUrl = "jdbc:mysql://localhost:3306/schooldb";
        String dbUser = "root";
        String dbPass = "password";

        // SQL query to retrieve student data
        String sql = "SELECT * FROM STUDENT";

        // List to store retrieved student objects
        List<Student> students = new ArrayList<>();
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            // Step 1: Load the MySQL JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 2: Open a connection to the database
            conn = DriverManager.getConnection(dbUrl, dbUser, dbPass);

            // Step 3: Create a statement for executing SQL queries
            stmt = conn.createStatement();

            // Step 4: Execute the query and retrieve results
            rs = stmt.executeQuery(sql);

            // Step 5: Extract and save student details in the list
            while (rs.next()) {
                int id = rs.getInt("ID");
                String name = rs.getString("NAME");
                int age = rs.getInt("AGE");
                String gender = rs.getString("GENDER");
                students.add(new Student(id, name, age, gender));
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Step 6: Close the resources in the finally block to release system resources
            try {
                if (rs != null) {
                    rs.close();
                }
                if (stmt != null) {
                    stmt.close();
                }
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}