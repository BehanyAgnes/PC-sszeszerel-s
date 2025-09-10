using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace DatabaseLesson2Example.Model
{
    public class Teacher
    {
        [Key]
        public int TeacherId { get; set; }
        public string Firstname { get; set; }
        public string Lastname { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }
        
        [JsonIgnore]
        public virtual ICollection<Subject>? Subjects { get; set; }

    }
}
