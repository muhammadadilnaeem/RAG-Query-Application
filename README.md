# **Query Application Documentation**

## **Introduction**
The Query Application allows users to input questions and receive answers based on the data provided. The application utilizes a RAG (Retrieval-Augmented Generation) model to process the questions and generate responses. Users interact with the application through a web interface designed with a focus on professional and user-friendly UX/UI design, including hover effects and bold fonts for emphasis.

## **Features**
- User-friendly web interface for querying.
- Processes questions using a RAG model.
- Displays answers in a bold and clear format.
- Enhanced user experience with hover effects.

## **How to Use the App**

https://github.com/muhammadadilnaeem/Practice-Projects/assets/162784706/474c9b69-8bd8-4f3c-9272-69708cdb6e81

### **Home Page**
#### **Enter a Question**
1. **Input Field**: Users can type their question into the input field labeled "Enter your question".
2. **Submit Button**: Once a question is entered, users click the "Ask" button to submit their query.

### **Displaying the Response**
- **Answer Display**: After submitting a question, the response from the RAG model is displayed on the same page in a highlighted format.
- **Real-time Processing**: The application processes the question in real-time and updates the answer dynamically.

## **Code Structure**
### **Flask Application Setup**
1. **Import Libraries**: The application imports necessary libraries including Flask and the RAG model components.
2. **Initialize Flask**: A Flask application is created and configured.

### **HTML Template**
- **Form for Input**: The HTML template includes a form with an input field for questions and a submit button.
- **Response Display**: The response section dynamically shows the answer after the form is submitted.

### **CSS Styling**
- **Responsive Design**: The CSS ensures the application is responsive and visually appealing.
- **Hover Effects**: Buttons and interactive elements have hover effects for better UX.
- **Bold Fonts**: Answers are displayed in bold fonts to make them stand out.

## **Example Usage**

### **Entering a Question**
1. **Open the Application**: Navigate to the home page of the Query Application.
2. **Type a Question**: In the input field, type a question like "List down names of all candidates?".
3. **Submit**: Click the "Ask" button to submit your question.

### **Viewing the Response**
- **Response Section**: The answer to your question will be displayed below the input field in a bold and clear format.

## **Conclusion**
This documentation provides a comprehensive overview of the Query Application. Users can enter questions, receive answers, and enjoy a professional and engaging user experience. The application leverages a RAG model for processing queries and provides real-time responses with enhanced UX/UI features.
