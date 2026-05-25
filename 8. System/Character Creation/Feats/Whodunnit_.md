---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Investigator]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You carefully consider your case and narrow down some of the details. When you [[Pursue a Lead]] and learn there's a larger mystery, you can ask two questions related to your investigation when you open it. The GM must answer truthfully with "yes" or "no," though if the answer would be misleading or have no practical application to your investigation, the GM can answer "immaterial." You can't use Whodunnit? more than once for the same lead, even across different days. Your questions must come from the following list, applying to the detail that spurred your investigation.

- Was this clue left by a [creature trait]? (Choose a creature trait such as humanoid, undead, or dwarf; this trait must be accurate as of the time the clue was left.)
- Was this clue left within the last hour?
- Was this clue left within the last day?
- Was the creature that left this clue in a heightened emotional state when it left the clue?
- Did anyone attempt to conceal this clue?

**Source:** `= this.source` (`= this.source-type`)
