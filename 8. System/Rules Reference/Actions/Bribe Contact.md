---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Cost** A bribe worth at least one-tenth of the Currency per Additional PC listed on Party Treasure by level. Doubling this amount grants a +2 circumstance bonus to the check.

**Requirements** You've successfully Gained a Contact.

You offer a bribe to your contact to help the heist in some way. Attempt a hard or very hard Deception or Diplomacy check.
- **Success** The contact accepts the bribe and you gain 1 EP.
- **Failure** You believe you successfully Bribed your Contact and gained 1 EP, but in fact the contact informs the opposition of the attempted bribery, adding 1 AP to the infiltration. The GM can reveal that this Edge Point grants no benefit at any point during the infiltration, as befits the story.
- **Critical Failure** As failure, but adding 2 AP to the infiltration.

**Source:** `= this.source` (`= this.source-type`)
