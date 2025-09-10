using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace DatabaseLesson2Example.Model
{
    public class Subject
    {
        [Key]
        public int SubjectId { get; set; }
        public string Name { get; set; }

        public int TeacherId { get; set; }
       
        [JsonIgnore]
        public Teacher? Teacher { get; set; }

        [JsonIgnore]
        public virtual ICollection<Student>? Students { get; set; }
    }
}
