// Compiles pages the way Docusaurus 3.10 actually does.
// markdown.format defaults to 'mdx', so .md files are MDX-compiled too, with
// mdx1Compat.comments enabling <!-- --> via @slorber/remark-comment.
import { compile } from '@mdx-js/mdx';
import comment from '@slorber/remark-comment';
import gfm from 'remark-gfm';
import fs from 'fs';
let bad = 0;
for (const f of process.argv.slice(2)) {
  let s = fs.readFileSync(f, 'utf8').replace(/^---\n[\s\S]*?\n---\n/, '');
  try { await compile(s, { remarkPlugins: [gfm, [comment, { ast: true }]] }); }
  catch (e) { bad++; console.log('FAIL\t' + f + '\t' + String(e.message).split('\n')[0]); }
}
console.log('compiled ' + (process.argv.length - 2) + ' files, ' + bad + ' failing');
