# django-spotdraft

## Stack
- Django
- DRF
- PostgreSQL
- Heroku

## Supported features

-   User should be able to `add Student`
-   User should be able to `get list of Students`
-   User should be able to `get Student by ID`
-   User should be able to `add Course`
-   User should be able to `get list of all courses`
-   User should be able to `get list of courses for a Student`
-   User should be able to `see count of courses for a Student`
-   User should be able to `see feedback and date joined for student list and course list apis`

## Usage

### List Students
```bash
curl -X GET https://django-spotdraft.herokuapp.com/api/v1/student
```

### List Courses
```bash
curl -X GET https://django-spotdraft.herokuapp.com/api/v1/course
```

### Get Student by ID
```bash
curl -X GET https://django-spotdraft.herokuapp.com/api/v1/student/1
```

### Get Course by ID
```bash
curl -X GET https://django-spotdraft.herokuapp.com/api/v1/course/4
```

### Create Student 
```bash
curl --header "Content-Type: application/json" -X POST -d '{"name": "Chuck Norris"}' https://django-spotdraft.herokuapp.com/api/v1/student
```

### Create Course 
```bash
curl --header "Content-Type: application/json" -X POST -d '{"name": "React tutorial for Beginners"}' https://django-spotdraft.herokuapp.com/api/v1/course
```

### Subscribe to a Course
```bash
curl -X POST https://django-spotdraft.herokuapp.com/api/v1/student/2/course/8
```

### Post a feedback to a subscribed course
```bash
curl --header "Content-Type: application/json" -X PATCH -d '{"feedback": "Awesome course"}' https://django-spotdraft.herokuapp.com/api/v1/student/2/course/7/feedback
```



