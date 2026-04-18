# PowerShell script to run batch notebook queries
# This activates the virtual environment and runs the batch processor

$ErrorActionPreference = "Continue"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "NotebookLM Batch Query Processor" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
$venvPath = "C:\Users\Lindsay\.venvs\workbench_env"
if (-not (Test-Path $venvPath)) {
    Write-Host "Error: Virtual environment not found at $venvPath" -ForegroundColor Red
    exit 1
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "$venvPath\Scripts\Activate.ps1"

# Check if notebooklm is installed
try {
    $null = python -c "import notebooklm" 2>$null
    Write-Host "notebooklm-py is installed ✓" -ForegroundColor Green
} catch {
    Write-Host "Installing notebooklm-py..." -ForegroundColor Yellow
    pip install 'notebooklm-py[browser]'
}

# Run the batch processor
Write-Host ""
Write-Host "Starting batch query processor..." -ForegroundColor Green
Write-Host "This will process all notebooks. Press Ctrl+C to stop." -ForegroundColor Yellow
Write-Host ""

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logFile = "docs/data/conference-papers/batch_log_$timestamp.txt"

Write-Host "Logging to: $logFile" -ForegroundColor Cyan
Write-Host ""

# Run with logging
python scripts/batch_query_all_notebooks.py | Tee-Object -FilePath $logFile

# Deactivate (optional)
# deactivate

Write-Host ""
Write-Host "Batch processing complete!" -ForegroundColor Green
Write-Host "Check the log file for details: $logFile" -ForegroundColor Cyan
