---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Occult]]", "[[Visual]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** You would be hit by a Strike

**Effect** You create an illusory duplicate at the last instant and attempt to trick your foe into striking it instead of you. The attacker attempts a DC 11 flat check; on a failure, the attack hits the duplicate, changing the result from a critical success to a success or a success to a failure.

**Source:** `= this.source` (`= this.source-type`)
