#!/usr/bin/env pwsh
$ErrorActionPreference = 'Stop'

Write-Host "Exporting translations from Crowdin..."
./l10nUtil.exe exportTranslations -o _addonL10n -c addon

# Ensure base directories exist (excluding language-specific doc folders)
New-Item -ItemType Directory -Force -Path addon/locale | Out-Null
New-Item -ItemType Directory -Force -Path addon/doc | Out-Null

# Retrieve Add-on ID from environment variables
$addonId = $env:ADDON_ID.Trim()
if (-not $addonId) {
    Write-Error "Failed to get addon ID. Ensure buildVars.py and dependencies are present."
    exit 1
}

foreach ($dir in Get-ChildItem -Path "_addonL10n/$addonId" -Directory) {
    Write-Host "=============================="
    Write-Host "Processing language: $($dir.Name)"
    Write-Host "=============================="

    $langCode = $dir.Name
    $langShort = $langCode.Split('_')[0]

    # File Paths
    $poFile = Join-Path $dir.FullName "$addonId.po"
    $localPoPath = "addon/locale/$langCode/LC_MESSAGES/nvda.po"

    $xliffFile = Join-Path $dir.FullName "$addonId.xliff"
    $remoteMd = Join-Path $dir.FullName "$addonId.md"

    $targetDocDir = "addon/doc/$langCode"
    $localMd = "$targetDocDir/readme.md"

    # ----------------------------
    # SKIP ENGLISH (source language)
    # ----------------------------
    if ($langCode -eq "en") {
        Write-Host "Skipping English (source language) → no MD/XLIFF processing required"
        continue
    }

    # ----------------------------
    # PO PROCESSING
    # ----------------------------
    if (Test-Path $poFile) {
        Write-Host "Checking PO file..."
        uv run ./.github/scripts/checkTranslation.py "$poFile"
        $isPoTranslated = ($LASTEXITCODE -eq 0)
        
        Write-Host "PO translated: $isPoTranslated"
        if ($isPoTranslated) {
            Write-Host "Updating local PO"
            # Directory created only if PO is valid
            New-Item -ItemType Directory -Force -Path (Split-Path $localPoPath) | Out-Null
            Move-Item $poFile $localPoPath -Force
        } else {
            Write-Host "PO not translated"
            if (Test-Path $localPoPath) {
                Write-Host "Uploading local PO to Crowdin"
                ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.po" $localPoPath -c addon
            }
        }
    }

    # ----------------------------
    # XLIFF & MD DECISION ENGINE
    # ----------------------------
    $xliffValid = $false
    $tempMd = $null

    if (Test-Path $xliffFile) {
        Write-Host "Checking XLIFF..."
        uv run ./.github/scripts/checkTranslation.py "$xliffFile"
        $xliffValid = ($LASTEXITCODE -eq 0)
        Write-Host "XLIFF valid: $xliffValid"

        if ($xliffValid) {
            Write-Host "Converting XLIFF → MD"
            $tempMd = "$env:TEMP\readme_$langCode.md"
            ./l10nUtil.exe xliff2md $xliffFile $tempMd
        }
    }

    $remoteExists = Test-Path $remoteMd
    $localExists = Test-Path $localMd

    # CASE: XLIFF VALID
    if ($xliffValid) {
        Write-Host "Entering XLIFF-driven logic"

        if ($remoteExists -and $localExists) {
            Write-Host "3-way comparison (xliff, remote, local)"
            $scoreX = [double]((uv run python .github/scripts/checkTranslation.py "$tempMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])
            $scoreR = [double]((uv run python .github/scripts/checkTranslation.py "$remoteMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])
            $scoreL = [double]((uv run python .github/scripts/checkTranslation.py "$localMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])

            $best = [Math]::Max($scoreX, [Math]::Max($scoreR, $scoreL))

            if ($best -eq $scoreX) {
                Write-Host "Winner: XLIFF"
                New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
                Move-Item $tempMd $localMd -Force
            } elseif ($best -eq $scoreR) {
                Write-Host "Winner: Remote MD"
                New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
                Move-Item $remoteMd $localMd -Force
            } else {
                Write-Host "Winner: Local MD → uploading"
                ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.md" $localMd -c addon
            }
        } elseif ($remoteExists -and -not $localExists) {
            Write-Host "Comparing XLIFF vs Remote"
            $scoreX = [double]((uv run python .github/scripts/checkTranslation.py "$tempMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])
            $scoreR = [double]((uv run python .github/scripts/checkTranslation.py "$remoteMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])

            if ($scoreX -ge $scoreR) {
                Write-Host "Winner: XLIFF → creating local"
                New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
                Move-Item $tempMd $localMd -Force
            } else {
                Write-Host "Winner: Remote → creating local"
                New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
                Move-Item $remoteMd $localMd -Force
            }
        } elseif (-not $remoteExists -and $localExists) {
            Write-Host "Comparing XLIFF vs Local"
            $scoreX = [double]((uv run python .github/scripts/checkTranslation.py "$tempMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])
            $scoreL = [double]((uv run python .github/scripts/checkTranslation.py "$localMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])

            if ($scoreX -gt $scoreL) {
                Write-Host "Winner: XLIFF → overwrite local"
                New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
                Move-Item $tempMd $localMd -Force
            } else {
                Write-Host "Winner: Local → uploading"
                ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.md" $localMd -c addon
            }
        } else {
            Write-Host "Only XLIFF available → importing directly"
            New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
            Move-Item $tempMd $localMd -Force
        }
    } else {
        Write-Host "XLIFF not usable → fallback logic"
        if ($remoteExists -and $localExists) {
            Write-Host "Comparing Remote vs Local"
            $scoreR = [double]((uv run python .github/scripts/checkTranslation.py "$remoteMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])
            $scoreL = [double]((uv run python .github/scripts/checkTranslation.py "$localMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])

            if ($scoreR -gt $scoreL) {
                Write-Host "Winner: Remote → overwrite local"
                # Folder is already assumed to exist here because localExists is true
                Move-Item $remoteMd $localMd -Force
            } else {
                Write-Host "Winner: Local → uploading"
                ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.md" $localMd -c addon
            }
        } elseif ($remoteExists -and -not $localExists) {
            Write-Host "Remote only → checking quality"
            $scoreR = [double]((uv run python .github/scripts/checkTranslation.py "$remoteMd" $langShort | Select-String "md_score=").ToString().Split("=")[1])

            if ($scoreR -gt 0.5) {
                Write-Host "Remote is valid → importing"
                # Folder created ONLY after validation
                New-Item -ItemType Directory -Force -Path $targetDocDir | Out-Null
                Move-Item $remoteMd $localMd -Force
            }
        } elseif (-not $remoteExists -and $localExists) {
            Write-Host "Only local exists → uploading without scoring"
            ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.md" $localMd -c addon
        }
    }
} # End foreach

# ----------------------------
# COMMIT CHANGES
# ----------------------------
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

git add addon/locale addon/doc

git diff --staged --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Update translations for $addonId from Crowdin"
    $branch = $env:downloadTranslationsBranch
    git switch $branch 2>$null

    if ($LASTEXITCODE -ne 0) {
        git switch -c $branch
    }
    git push -f --set-upstream origin $branch
} else {
    Write-Host "Nothing to commit."
}