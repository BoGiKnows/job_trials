# job_trials
Тестовое задание по написанию запроса в SQL базу данных и 
написание простой программы по подсчету часов работы сотрудника.

Условие задачи:
https://gitlab.zvonok.in/-/snippets/28

1. first_task - Решение первой задачи 
2. second_task - Решение второй задачи

Отдельно ответ на первую задачу:
SELECT
    article.id,
    article.title,
   	article.text
FROM article
LEFT JOIN comment
    ON article.id = comment.article_id
WHERE comment.article_id IS NULL;
