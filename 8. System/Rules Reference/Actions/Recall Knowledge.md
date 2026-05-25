---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Secret]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You attempt a skill check to try to remember a bit of knowledge regarding a topic related to that skill. Suggest which skill you'd like to use and ask the GM one question. The GM determines the DC. You might need to collaborate with the GM to narrow down the question or skills, and you can decide not to Recall Knowledge before committing to the action if you don't like your options.
- **Critical Success** You recall the knowledge accurately. The GM answers your question truthfully and either tells you additional information or context, or answers one follow-up question.
- **Success** You recall the knowledge accurately. The GM answers your question truthfully.
- **Critical Failure** You recall incorrect information. The GM answers your question falsely (or decides to give you no information, as on a failure).

**Source:** `= this.source` (`= this.source-type`)
