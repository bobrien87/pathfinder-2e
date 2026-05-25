---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Mental]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You accuse the target of breaking its word to you and invoke the wrath of your patron to claim what's due, demanding the target pay you in currency, fulfill an order, or stand down. The demand can't be obviously self-destructive, or the spell fails. If the target resists, you take your payment from its life force. The target must attempt a Will save. Regardless of the result of its save, the target is temporarily immune for 1 day.
- **Critical Success** The target is unaffected and is immune to your pact broker cantrips for 1 day.
- **Success** If the target doesn't comply with your request by the end of its next turn, it takes 3d8 persistent,void damage. If it later complies, the spell automatically ends.
- **Failure** As success, but if the target doesn't comply, it is [[Drained]] 1 and takes 6d8 persistent,void damage.
- **Critical Failure** As success, but if the target doesn't comply, it is [[Drained]] 2 and [[Doomed]] 1, and takes 6d8 persistent,void damage. Even if the target completes your commands later, the spell doesn't end until all the conditions end.

**Heightened (9th)** You can target up to two creatures.

**Source:** `= this.source` (`= this.source-type`)
