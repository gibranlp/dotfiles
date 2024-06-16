const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#131311", /* black   */
  [1] = "#4E7A8A", /* red     */
  [2] = "#4391A7", /* green   */
  [3] = "#A0A897", /* yellow  */
  [4] = "#C3BBA3", /* blue    */
  [5] = "#DACBA9", /* magenta */
  [6] = "#E4D3AE", /* cyan    */
  [7] = "#f3f0e2", /* white   */

  /* 8 bright colors */
  [8]  = "#aaa89e",  /* black   */
  [9]  = "#4E7A8A",  /* red     */
  [10] = "#4391A7", /* green   */
  [11] = "#A0A897", /* yellow  */
  [12] = "#C3BBA3", /* blue    */
  [13] = "#DACBA9", /* magenta */
  [14] = "#E4D3AE", /* cyan    */
  [15] = "#f3f0e2", /* white   */

  /* special colors */
  [256] = "#131311", /* background */
  [257] = "#f3f0e2", /* foreground */
  [258] = "#f3f0e2",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
