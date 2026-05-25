---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You try to make contact with an individual who can aid you in the infiltration. Attempt a normal, hard, or very hard DC Diplomacy or Society check, or a check using a Lore skill appropriate to your prospective contact.
- **Success** You make contact and gain 1 EP.
- **Failure** You fail to make contact.
- **Critical Failure** You insult or spook the contact in some way. Future attempts take a -2 circumstance penalty.

**Special** Multiple critical failures might cause the contact to work against the PCs in some way, likely increasing the party's Awareness Points.

**Source:** `= this.source` (`= this.source-type`)
