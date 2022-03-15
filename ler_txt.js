const fs = require('fs')
const readline = require('readline');

function importLayout(fileName) {
  layout = [];

  var lines = fs
    .readFileSync(`Sigtap/layout/${fileName}_layout.txt`, { encoding:'latin1', flag:'r' })
    .toString()
    .split(/\r?\n/);

  lines.forEach((line) => {
    
    if (line && !line.startsWith('Coluna')) {
      reg={};
      reg['campo'] = line.split(',')[0];
      reg['inicio'] = line.split(',')[2];
      reg['final'] = line.split(',')[3];
      layout.push(reg);
    }
  });

  return layout;
}

function importarReg(line, layout) {
  reg = {};

  layout.forEach((data) => {
    reg[data.campo] = line.slice(data.inicio-1, data.final).trim();
  });
  console.log(reg);

}

async function importFile(fileName) {
  const fileStream = fs.createReadStream(`Sigtap/${fileName}.txt`, { flags: 'r', encoding: 'latin1' });

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });
  
  file_layout = await importLayout(fileName);
  
  for await (const line of rl) {
    importarReg(line, file_layout);
  }
  
}

async function processar() {
  await importFile('tb_grupo');
  await importFile('tb_sub_grupo');
}

processar();