function scrollToScannerSection() {
  const scannerSection = document.getElementById('scanner-section');
  const offsetTop = scannerSection.offsetTop;
  window.scrollTo({
    top: offsetTop,
    behavior: 'smooth'
  });
}
