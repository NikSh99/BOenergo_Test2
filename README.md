# BOenergo_Test2
 
Есть группа из 100 предметов. Предметы могут быть синего, зелёного и красного цвета. Известно, что предметов синего цвета сильно больше, чем предметов зелёного цвета, а предметов зелёного цвета немного больше, чем предметов красного цвета. Напишите сервис, который будет принимать номер предмета и пытаться угадать его цвет. Логику работы сервиса определите самостоятельно.

Реализован Веб-сервис, который принимает номер предмета и пытается угадать его цвет. У сервиса есть ограничения на номер предмета - он должен быть не больше 100.

Сервис будет доступен по адресу http://localhost:5000/guess-color

Вы можете отправлять POST-запросы на эндпоинт /guess-color для угадывания цвета предмета. В запросе необходимо передать JSON-объект с ключом item_number, содержащим номер предмета.
Пример запроса с использованием PowerShell: 

```
$uri = "http://localhost:5000/guess-color"
$body = @{
    "item_number" = 45
} | ConvertTo-Json

try {
    $response = Invoke-WebRequest -Method POST -Uri $uri -Headers @{"Content-Type" = "application/json"} -Body $body -ErrorAction Stop
    $responseContent = $response.Content | ConvertFrom-Json
    
    if ($response.StatusCode -eq 200) {
        Write-Host "Угаданный цвет для предмета $($responseContent.item_number): $($responseContent.color)"
    } else {
        Write-Host "Ошибка: $($responseContent.error)"
    }
} catch {
    Write-Host "Ошибка при выполнении запроса: $($_.Exception.Message)"
}
```

![image](https://github.com/NikSh99/BOenergo_Test2/assets/43999726/31d68c74-f277-46e0-aa25-dab529fe07ca)

Для запуска тестов из дирректории проекта в командной строке ввести команду python test.py
![image](https://github.com/NikSh99/BOenergo_Test2/assets/43999726/e2e95659-739c-4862-9518-ee3dc02be090)
