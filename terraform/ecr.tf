resource "aws_ecr_repository" "backend" {
  name         = "devops-project-backend"
  force_delete = true
}

resource "aws_ecr_repository" "frontend" {
  name         = "devops-project-frontend"
  force_delete = true
}
