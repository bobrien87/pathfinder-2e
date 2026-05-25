---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
defense: "Will"
duration: "10 minutes (see text)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You announce yourself in the name of certain grim pacts that predate mortal life. This is not a compulsion, but rather an invitation of sorts. The invitation is understood by creatures in the area with telepathy and any who understand Aklo, Chthonian, Empyrean, Fey, or Utopian.

Those who accept the invitation cannot take hostile action against others who agreed until 10 minutes pass and can communicate telepathically with them during that time. This effect ends immediately if any hostile action is taken against a creature that agreed.

Those creatures who decline the choice or do not understand it must attempt a Will save.
- **Critical Success** Nothing happens.
- **Success** The creature is [[Frightened]] 1. If it understood the invitation, its frightened status doesn't decrease at the end of any turn in which it damaged a creature that agreed to the invitation.
- **Failure** As success, but the creature is [[Frightened]] 2.
- **Critical Failure** As success, but the creature is [[Frightened]] 3.

**Source:** `= this.source` (`= this.source-type`)
