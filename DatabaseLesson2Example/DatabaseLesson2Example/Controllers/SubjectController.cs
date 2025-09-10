using DatabaseLesson2Example.Data;
using DatabaseLesson2Example.DTO;
using DatabaseLesson2Example.Model;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace DatabaseLesson2Example.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SubjectController : ControllerBase
    {
        private readonly AppDbContext _context;

        public SubjectController(AppDbContext context)
        {
            _context = context;
        }

        // 1. Új tantárgy felvétele és tanár hozzárendelése
        [HttpPost]
        public async Task<ActionResult<Subject>> CreateSubject([FromBody] Subject subject)
        {
            if (subject == null)
            {
                return BadRequest("Invalid data.");
            }

            var teacher = await _context.Teachers.FindAsync(subject.TeacherId);
            if (teacher == null)
            {
                return NotFound("Teacher not found.");
            }

            // A tantárgy tanár hozzárendelése
            subject.Teacher = teacher;

            // Tantárgy mentése az adatbázisba
            _context.Subjects.Add(subject);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetSubjectById), new { id = subject.SubjectId }, subject);
        }

        // 2. Diák hozzáadása egy meglévő tantárgyhoz
        [HttpPost("{subjectId}/students")]
        public async Task<IActionResult> AddStudentToSubject(int subjectId, [FromBody] int studentId)
        {
            var subject = await _context.Subjects.Include(s => s.Students).FirstOrDefaultAsync(s => s.SubjectId == subjectId);
            if (subject == null)
            {
                return NotFound("Subject not found.");
            }

            var student = await _context.Students.FindAsync(studentId);
            if (student == null)
            {
                return NotFound("Student not found.");
            }

            // Diák hozzáadása a tantárgyhoz
            if (subject.Students == null)
            {
                subject.Students = new List<Student>();
            }

            subject.Students.Add(student);
            await _context.SaveChangesAsync();

            return Ok(subject);
        }

        // 3. Tantárgyak listázása
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Subject>>> GetSubjects()
        {
            var subjects = await _context.Subjects
                .Include(s => s.Teacher)
                .Include(s => s.Students)
                .ToListAsync();

            return Ok(subjects);
        }

        // 4. Tantárgy törlése
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteSubject(int id)
        {
            var subject = await _context.Subjects.FindAsync(id);
            if (subject == null)
            {
                return NotFound("Subject not found.");
            }

            // Tantárgy törlése
            _context.Subjects.Remove(subject);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        // Kiegészítő végpont: tantárgy lekérése ID alapján
        [HttpGet("{id}")]
        public async Task<ActionResult<SubjectDto>> GetSubjectById(int id)
        {
            var subject = await _context.Subjects
                .Include(s => s.Teacher)
                .Include(s => s.Students)
                .FirstOrDefaultAsync(s => s.SubjectId == id);

            if (subject == null)
            {
                return NotFound("Subject not found.");
            }

            // A Subject modelből SubjectDto-t készítünk
            var subjectDto = new SubjectDto
            {
                SubjectId = subject.SubjectId,
                Name = subject.Name,
                Teacher = new TeacherDto
                {
                    TeacherId = subject.Teacher.TeacherId,
                    Firstname = subject.Teacher.Firstname,
                    Lastname = subject.Teacher.Lastname
                },
                Students = subject.Students?.Select(s => new StudentDto
                {
                    StudentId = s.StudentId,
                    Firstname = s.Firstname,
                    Lastname = s.Lastname
                }).ToList()
            };

            return Ok(subjectDto);
        }
    }
}
