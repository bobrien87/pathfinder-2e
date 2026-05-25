---
type: action
source-type: "Remaster"
traits: ["[[Emotion]]", "[[Healing]]", "[[Mental]]", "[[Psyche]]", "[[Psychic]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your unleashed psyche gives you closer connections to the emotions of your allies, letting you project reassurance and strength that replenishes their mind and body. Choose one of the two benefits to grant one ally within 30 feet that you can see. That ally is then temporarily immune for 10 minutes.

- The ally gains a +1 status bonus to saving throws against mental effects until your psyche ends.
- The ally regains Hit Points equal to @Damage[(2+2*@actor.level)[healing]]{2 + double your level}.

**Source:** `= this.source` (`= this.source-type`)
