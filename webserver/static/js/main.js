 // Modal functionality
    const modal = document.getElementById('addCctvModal');
    const addBtn = document.getElementById('addCctvBtn');
    const closeBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    
    // Show modal
    addBtn.addEventListener('click', () => {
      modal.classList.remove('modal-hidden');
    });
    
    // Hide modal
    function closeModal() {
      modal.classList.add('modal-hidden');
    }
    
    closeBtn.addEventListener('click', closeModal);
    cancelBtn.addEventListener('click', closeModal);
    
    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    }); 
