# About

This project came about because I wanted to get experience deploying an NLP model
in the wild, and I also needed to update my personal site. I thought, "Why not a Resume/CV
QA system?" So here it is. I built the system from the publicly released weights for
[Unified QA](https://github.com/allenai/unifiedqa). It's versatility in QA formatting
makes it ideal for an open-ended system.


I baked my personal bio/factoids so my compute dollars doesn't go to fund random
T5 queries.

## Notes
The language generation doesn't seem to gather facts from separate areas, so I
had to write my info so lists were kept together.