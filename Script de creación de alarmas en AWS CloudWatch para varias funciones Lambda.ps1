# Requiere AWS.Tools.Installed (AWS Tools for PowerShell v4 o superior)

# Configura tus variables
$region = "us-east-1"
$lambdaNames = @("crearAnimal", "editarAnimal", "borrarAnimal")  # <- Añade tus Lambdas aquí
$namespace = "AWS/Lambda"
$metricName = "Errors"
$threshold = 1
$evaluationPeriods = 1
$alarmPeriod = 60  # en segundos
$comparisonOperator = "GreaterThanThreshold"
$statistic = "Sum"

# Crear un tema SNS si no existe
$snsTopicName = "PatitasLambdaErrors"
$email = "maria@email.com"

$topicArn = (Get-SNSTopicList -Region $region).Topics | Where-Object { $_.TopicArn -like "*$snsTopicName" } | Select-Object -ExpandProperty TopicArn

if (-not $topicArn) {
    $topicArn = (New-SNSTopic -Name $snsTopicName -Region $region).TopicArn
    Write-Output "✅ Tema SNS '$snsTopicName' creado: $topicArn"
    Write-Output "📧 Enviando subscripción a $email..."
    New-SNSSubscription -TopicArn $topicArn -Protocol email -Endpoint $email -Region $region
    Write-Output "⚠️ No olvides confirmar la suscripción por email"
} else {
    Write-Output "🔁 Tema SNS '$snsTopicName' ya existe: $topicArn"
}

# Crear alarmas para cada Lambda
foreach ($lambdaName in $lambdaNames) {
    $alarmName = "LambdaErrores_$lambdaName"

    Write-Output "📡 Creando alarma para función Lambda '$lambdaName'..."

    New-CWAlarm `
        -AlarmName $alarmName `
        -MetricName $metricName `
        -Namespace $namespace `
        -Dimensions @{ Name = "FunctionName"; Value = $lambdaName } `
        -Statistic $statistic `
        -Period $alarmPeriod `
        -EvaluationPeriods $evaluationPeriods `
        -Threshold $threshold `
        -ComparisonOperator $comparisonOperator `
        -AlarmActions $topicArn `
        -Region $region

    Write-Output "✅ Alarma '$alarmName' creada."
}
