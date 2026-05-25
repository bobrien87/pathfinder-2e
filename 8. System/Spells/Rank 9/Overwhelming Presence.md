---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:2`"
area: "40-foot burst"
targets: "any number of creatures"
defense: "Will"
duration: "until full tribute is paid"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You surround yourself with supernatural splendor, appearing to be a god or similarly majestic being, with an appearance, regalia, and iconography of your choice. Targets must attempt a Will save. Regardless of the outcome, the target is then temporarily immune for 1 minute.
- **Critical Success** The target is unaffected.
- **Success** The target must pay tribute to you two times. Paying tribute requires that the target spend a single action, which has either the move trait (as they bow) or manipulate trait (as they offer up a token in their hands). They must pay tribute at least once on each of their turns, if possible. While affected, the target is [[Fascinated]] by you and can't use hostile actions against you.
- **Failure** As success, but the target must pay tribute a total of six times.
- **Critical Failure** As failure, but the target must spend all its actions paying tribute, and they cannot take other actions until the tribute is fully paid.

**Source:** `= this.source` (`= this.source-type`)
