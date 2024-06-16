static const char norm_fg[] = "#f3f0e2";
static const char norm_bg[] = "#131311";
static const char norm_border[] = "#aaa89e";

static const char sel_fg[] = "#f3f0e2";
static const char sel_bg[] = "#4391A7";
static const char sel_border[] = "#f3f0e2";

static const char urg_fg[] = "#f3f0e2";
static const char urg_bg[] = "#4E7A8A";
static const char urg_border[] = "#4E7A8A";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
