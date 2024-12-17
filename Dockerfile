# 1. Use an Official Python Runtime as a Parent Image
#   If no need for Playwright, can swap with
#       - python:3.10-slim
FROM python:3.10-slim

# 2. Set Environment Variables
#   Configures Python's behavior inside the container
#       - Disables generate of .pyc files
#       - Ensures logs and outputs are immediately visible
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set Work Directory
#   All commands are executed relative to this director
WORKDIR /app

# 4. Install System Dependencies and sudo
#   - build-essential: Required for compiling Python packages
#   - sudo: Lets users execute commands with superuser privileges.
#   - psswd: Enables setting passwords for users
#   no-install-recommeands prevents installation of unecessary packages
#   rm -rf /var/lib/apt/lists/* cleans up local repo
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        sudo \
        passwd \
    && rm -rf /var/lib/apt/lists/*

# 5. Create Non-Root User and Group with sudo privileges
#   - Create system group 'appgroup'
#   - Create user 'appuser' in 'appgroup' with no initial password
#   - Set password for 'appuser'
#   - Give 'appuser' password-less 'sudo' privileges
RUN addgroup --system appgroup \
    && adduser --system --ingroup appgroup --disabled-password appuser \
    && echo "appuser:test" | chpasswd \
    && echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 6. Install Python Dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 7. Copy rest of application code
COPY . .

# 8. Change ownership of the application directory
#   - Changes ownership to 'appuser' and 'appgroup'
#   - Makes sure non-root user has perms
RUN chown -R appuser:appgroup /app

# 9. Expose the Port the app runs on
#   - FastAPI uses Port 8000
EXPOSE 8000

# 10. Install Playwright (if needed)
# RUN playwright install

# 11. Define Default Command to Run the Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# 12. Switch to Non-Root User
USER appuser