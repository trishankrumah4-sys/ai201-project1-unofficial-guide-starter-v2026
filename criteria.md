# Acceptance criteria - The Unofficial Guide

## 1. Retrieved chunks contain the answer
For at least 4 of my 5 test questions, the retrieved chunks include one that contains the answer.
Why this target: My documents are short and single-topic, so most questions should retrieve cleanly. I left room for one miss since my library hours question depends on a distinction that a close but wrong chunk could plausibly beat out.
## 2. Every answer names a source
Every answer the system produces names at least one source document.
Why this target: This is a hard requirement, not a rate, because the grounding instruction either includes a source or it does not. If any answer skips this, the prompt itself needs fixing.
## 3. The relevance gate stops out-of-corpus questions
When I ask a question my documents clearly do not cover, the relevance gate stops it and the system returns an I do not know message, in at least 4 of 5 tries.
Why this target: I set this before seeing my actual distance numbers, so I am leaving room for one out-of-scope question to accidentally share enough vocabulary with campus topics to slip past the cutoff.
## 4. Chunks read as complete thoughts
At least 4 of 5 sampled chunks are a complete document, with no sentence cut off at the start or end.
Why this target: My campus_life documents average about 317 characters each, well under a typical chunk size, so most should come through as one whole document rather than being split.
## 5. Sources are accurate, not just present

For all 5 of my test questions, the source named in the answer is the document that actually contains the fact used to answer it.
Why this target: Naming a source is only useful if it is the right one. Since I already know which document answers each question, I can check this by eye.
