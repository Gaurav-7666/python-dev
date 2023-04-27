<%@ page language="java" import="java.sql.*" %>
<html>
<head>
  <title>Database Connection Example</title>
</head>
<body>
<%
   String url = "jdbc:mysql://localhost:3306/mydb"; // JDBC URL for the database
   String user = "myuser"; // username for the database
   String password = "mypassword"; // password for the database
   Connection conn = null;
   Statement stmt = null;
   ResultSet rs = null;
   try {
      // Connect to the database
      Class.forName("com.mysql.jdbc.Driver");
      conn = DriverManager.getConnection(url, user, password);
      // Execute a SELECT query
      stmt = conn.createStatement();
      rs = stmt.executeQuery("SELECT * FROM mytable");
      // Process the results
      while (rs.next()) {
         out.println(rs.getString("column1") + " " + rs.getString("column2"));
      }
   } catch (SQLException e) {
      out.println("SQL Exception: " + e.getMessage());
   } catch (ClassNotFoundException e) {
      out.println("Class Not Found Exception: " + e.getMessage());
   } finally {
      // Close the resources
      if (rs != null) rs.close();
      if (stmt != null) stmt.close();
      if (conn != null) conn.close();
   }
%>
</body>
</html>
