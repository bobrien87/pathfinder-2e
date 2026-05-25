---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Unexpected Sharpshooter|Unexpected Sharpshooter]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Unexpected Sharpshooter Dedication, master in Deception"
frequency: "once per round"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Requirements** Either you used Accidental Shot and hit your opponent with the Strike this turn, or you used Lucky Escape since your last turn and the triggering attack missed you.

You laugh innocently about the inexplicable luck of your last shot hitting its mark or how close the attack that just missed you came to taking your head off, causing your foes to second guess whether it's a good idea to oppose you in battle. Attempt to [[Demoralize]] either the foe you hit with Accidental Shot or the foe that missed you due to Lucky Escape. You use Deception instead of Intimidation to attempt the check to Demoralize.

**Source:** `= this.source` (`= this.source-type`)
