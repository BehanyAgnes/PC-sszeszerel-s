namespace DatabaseLesson2Example.DTO
{
    public class SubjectDto
    {
        public int SubjectId { get; set; }
        public string Name { get; set; }
        public TeacherDto Teacher { get; set; }
        public List<StudentDto> Students { get; set; }
    }

    public class TeacherDto
    {
        public int TeacherId { get; set; }
        public string Firstname { get; set; }
        public string Lastname { get; set; }
    }

    public class StudentDto
    {
        public int StudentId { get; set; }
        public string Firstname { get; set; }
        public string Lastname { get; set; }
    }
}
