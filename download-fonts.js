const https = require('https');
const fs = require('fs');
const path = require('path');

const fonts = [
  {
    name: 'Poppins-Regular',
    url: 'https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf'
  },
  {
    name: 'Poppins-Medium',
    url: 'https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Medium.ttf'
  },
  {
    name: 'Poppins-SemiBold',
    url: 'https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-SemiBold.ttf'
  },
  {
    name: 'Poppins-Bold',
    url: 'https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Bold.ttf'
  }
];

const fontsDir = path.join(__dirname, '../assets/fonts');

if (!fs.existsSync(fontsDir)) {
  fs.mkdirSync(fontsDir, { recursive: true });
}

fonts.forEach(font => {
  const filePath = path.join(fontsDir, `${font.name}.ttf`);
  const file = fs.createWriteStream(filePath);
  
  https.get(font.url, response => {
    response.pipe(file);
    
    file.on('finish', () => {
      file.close();
      console.log(`Downloaded ${font.name}`);
    });
  }).on('error', err => {
    fs.unlink(filePath);
    console.error(`Error downloading ${font.name}:`, err.message);
  });
}); 