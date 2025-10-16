        // Data storage (in-memory)
        let students = [];
        let courses = [];
        let faculty = [];
        let attendance = [];
        let results = [];
        let fees = [];
        let timetable = [];
        let idCounters = {
            attendance: 1,
            results: 1
        };

        // Tab switching
        function showTab(tabName) {
            const tabs = document.querySelectorAll('.tab-content');
            const buttons = document.querySelectorAll('.tab-btn');
            
            tabs.forEach(tab => tab.classList.remove('active'));
            buttons.forEach(btn => btn.classList.remove('active'));
            
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
            
            updateDashboard();
            updateDropdowns();
        }

        // Update dashboard statistics
        function updateDashboard() {
            document.getElementById('totalStudents').textContent = students.length;
            document.getElementById('totalCourses').textContent = courses.length;
            document.getElementById('totalFaculty').textContent = faculty.length;
            document.getElementById('pendingFees').textContent = fees.filter(f => f.status === 'Pending').length;
        }

        // Update dropdowns
        function updateDropdowns() {
            // Update student dropdowns
            const studentSelects = ['attendanceStudentSelect', 'resultStudentSelect', 'feeStudentSelect'];
            studentSelects.forEach(selectId => {
                const select = document.getElementById(selectId);
                if (select) {
                    select.innerHTML = '<option value="">Select Student</option>';
                    students.forEach(s => {
                        select.innerHTML += `<option value="${s.student_id}">${s.name} (${s.student_id})</option>`;
                    });
                }
            });

            // Update course dropdowns
            const courseSelects = ['attendanceCourseSelect', 'resultCourseSelect', 'timetableCourseSelect'];
            courseSelects.forEach(selectId => {
                const select = document.getElementById(selectId);
                if (select) {
                    select.innerHTML = '<option value="">Select Course</option>';
                    courses.forEach(c => {
                        select.innerHTML += `<option value="${c.course_id}">${c.course_name} (${c.course_id})</option>`;
                    });
                }
            });

            // Update faculty dropdown
            const facultySelect = document.getElementById('timetableFacultySelect');
            if (facultySelect) {
                facultySelect.innerHTML = '<option value="">Select Faculty</option>';
                faculty.forEach(f => {
                    facultySelect.innerHTML += `<option value="${f.faculty_id}">${f.name} (${f.faculty_id})</option>`;
                });
            }
        }

        // Student functions
        function addStudent(e) {
            e.preventDefault();
            const formData = new FormData(e.target);
            const student = Object.fromEntries(formData.entries());
            students.push(student);
            updateStudentTable();
            e.target.reset();
            updateDashboard();
            updateDropdowns();
        }

        function updateStudentTable() {
            const tbody = document.getElementById('studentTableBody');
            tbody.innerHTML = '';
            students.forEach((student, index) => {
                tbody.innerHTML += 
                    <tr>
                        <td>${student.student_id}</td>
                        <td>${student.name}</td>
                        <td>${student.roll_no}</td>
                        <td>${student.email}</td>
                        <td>${student.phone}</td>
                        <td>Year ${student.year}</td>
                        <td>${student.branch}</td>
                        <td>
                            <button class="action-btn edit-btn" onclick="editItem('student', ${index})">Edit</button>
                            <button class="action-btn delete-btn" onclick="deleteItem('student', ${index})">Delete</button>
                        </td>
                    </tr>
                ;
            });
        }

        // Course functions
        function addCourse(e) {
            e.preventDefault();
            const formData = new FormData(e.target);
            const course = Object.fromEntries(formData.entries());
            courses.push(course);
            updateCourseTable();
            e.target.reset();
            updateDashboard();
            updateDropdowns();
        }

        function updateCourseTable() {
            const tbody = document.getElementById('courseTableBody');
            tbody.innerHTML = '';
            courses.forEach((course, index) => {
                tbody.innerHTML += 
                    <tr>
                        <td>${course.course_id}</td>
                        <td>${course.course_name}</td>
                        <td>${course.credits}</td>
                        <td>
                            <button class="action-btn edit-btn" onclick="editItem('course', ${index})">Edit</button>
                            <button class="action-btn delete-btn" onclick="deleteItem('course', ${index})">Delete</button>
                        </td>
                    </tr>
                ;
            });
        }

        // Faculty functions
        function addFaculty(e) {
            e.preventDefault();}