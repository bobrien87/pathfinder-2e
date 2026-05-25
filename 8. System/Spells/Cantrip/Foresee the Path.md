---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Psychic]]"]
cast: "`pf2:1`"
range: "60 feet"
targets: "1 ally and 1 enemy"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You see just a split second into the future and glean how an enemy will move, making it easier for your allies to strike it mid-action. Make a [[Perception]] check{Perception check} against the target enemy's Will DC or Deception DC, whichever is higher. The GM may judge a different DC is more appropriate if it's higher; for instance, using the Warfare Lore DC of a military captain. The target is then temporarily immune for 1 minute.
- **Critical Success** The target ally gains a reaction that lets it make a melee Strike against the target enemy, triggered if the enemy leaves a square within the ally's reach. If the ally already has an ability that lets it make melee Strikes as a reaction, such as Reactive Strike, the ally can forgo gaining the temporary reaction to instead gain a +2 status bonus to melee Strikes it makes as reactions.
- **Success** As critical success, but the status bonus an ally gets if it forgoes the reaction is +1.
- **Failure** The spell has no effect.

**Source:** `= this.source` (`= this.source-type`)
