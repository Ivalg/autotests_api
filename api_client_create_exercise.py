from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="qwert",
    lastName="Ivanov",
    firstName="Ivan",
    middleName="Ivanovich"
)
create_user_response = public_users_client.create_user(create_user_request)
authentication_user = AuthenticationUserSchema(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="avatar.png",
    directory="courses",
    upload_file="./testdata/files/avatar.png"
)
create_file_response = files_client.create_file(create_file_request)

create_course_request = CreateCourseRequestDict(
    title="Python automation",
    maxScore=100,
    minScore=10,
    description="Python API automation course",
    estimateTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)

create_exercise_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="10 minutes"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data", create_exercise_response)
