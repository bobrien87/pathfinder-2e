---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "8 hours"
area: "36960-foot emanation"
targets: "the outer walls of a settlement"
duration: "1 week"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The outer walls are a city's first defense against invaders, and you want to make certain no attackers can climb over them. Upon successful completion of this ritual, the surfaces of a settlement's walls within the area are covered with a thin, slippery sheen that can't be washed away.
- **Critical Success** The oil covering the walls also coats any climber's hands. The DC for Athletics checks to Climb the affected walls increases by 10, and a creature who fails a check to climb also drops anything they are carrying.
- **Success** The DC for Athletics checks to Climb the affected walls increases by 5.
- **Failure** The ritual has no effect.
- **Critical Failure** Phantom oil constantly pools around your feet during times of stress. For 1 week, the first time each encounter that a primary or secondary caster takes an action to move, they must attempt a Reflex save or Acrobatics check to [[Balance]] against the ritual's casting DC or fall [[Prone]]. A caster can Step or [[Crawl]] without having to attempt a check or save.

**Source:** `= this.source` (`= this.source-type`)
