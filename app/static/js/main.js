// Main JavaScript for Trip Planner

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add page transition effect
    document.body.classList.add('page-transition');

    // Animate elements on scroll (fallback for browsers without AOS)
    function animateOnScroll() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 50) {
                element.classList.add('animated');
            }
        });
    }

    // Call once on load
    animateOnScroll();
    
    // Add scroll event listener
    window.addEventListener('scroll', animateOnScroll);

    // Trip date range validation
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');
    
    if (startDateInput && endDateInput) {
        startDateInput.addEventListener('change', function() {
            endDateInput.min = this.value;
            if (endDateInput.value && endDateInput.value < this.value) {
                endDateInput.value = this.value;
            }
        });
        
        endDateInput.addEventListener('change', function() {
            startDateInput.max = this.value;
            if (startDateInput.value && startDateInput.value > this.value) {
                startDateInput.value = this.value;
            }
        });
    }

    // Budget calculator
    const budgetInputs = document.querySelectorAll('.budget-item');
    const totalBudgetElement = document.getElementById('total-budget');
    
    if (budgetInputs.length > 0 && totalBudgetElement) {
        budgetInputs.forEach(input => {
            input.addEventListener('input', calculateTotalBudget);
        });
        
        function calculateTotalBudget() {
            let total = 0;
            budgetInputs.forEach(input => {
                const value = parseFloat(input.value) || 0;
                total += value;
            });
            totalBudgetElement.textContent = total.toFixed(2);
        }
        
        // Calculate initial total
        calculateTotalBudget();
    }

    // Countdown timer for trips
    const countdownElements = document.querySelectorAll('.trip-countdown');
    
    if (countdownElements.length > 0) {
        countdownElements.forEach(element => {
            const tripDate = new Date(element.dataset.date).getTime();
            
            const countdownInterval = setInterval(function() {
                const now = new Date().getTime();
                const distance = tripDate - now;
                
                if (distance < 0) {
                    clearInterval(countdownInterval);
                    element.innerHTML = 'Trip has started!';
                    return;
                }
                
                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                
                element.innerHTML = `${days}d ${hours}h ${minutes}m`;
            }, 1000);
        });
    }

    // Image preview for file inputs
    const imageInputs = document.querySelectorAll('.image-upload');
    
    if (imageInputs.length > 0) {
        imageInputs.forEach(input => {
            const previewElement = document.getElementById(input.dataset.preview);
            
            if (previewElement) {
                input.addEventListener('change', function() {
                    if (this.files && this.files[0]) {
                        const reader = new FileReader();
                        
                        reader.onload = function(e) {
                            previewElement.src = e.target.result;
                            previewElement.style.display = 'block';
                        };
                        
                        reader.readAsDataURL(this.files[0]);
                    }
                });
            }
        });
    }

    // Notification dismissal
    const notificationElements = document.querySelectorAll('.notification-dismiss');
    
    if (notificationElements.length > 0) {
        notificationElements.forEach(element => {
            element.addEventListener('click', function() {
                const notificationId = this.dataset.id;
                
                // Send AJAX request to mark notification as dismissed
                fetch(`/api/notifications/${notificationId}/dismiss`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => {
                    if (response.ok) {
                        // Remove notification from DOM
                        this.closest('.notification-item').remove();
                        
                        // Update notification counter
                        const counter = document.querySelector('.notification-counter');
                        if (counter) {
                            const count = parseInt(counter.textContent) - 1;
                            counter.textContent = count > 0 ? count : '';
                            if (count <= 0) {
                                counter.style.display = 'none';
                            }
                        }
                    }
                })
                .catch(error => console.error('Error dismissing notification:', error));
            });
        });
    }
}); 