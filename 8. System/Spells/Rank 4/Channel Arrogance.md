---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "1 to 3"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You channel your heightened sense of self-worth into a creature, forcing them to acknowledge your true worth. You can Cast this Spell using 1 action if you know the target isn't worthy of you spending your time to generate the full force of this spell, or using 3 actions if you can't possibly hold back the majesty of your presence and must flood the target with your full attention.

The target takes 5d10 mental damage and other effects depending on its Will saving throw. If you Cast the Spell using 1 action, the target gets a result one degree of success better than it rolled.
- **Critical Success** The creature is unaffected.
- **Success** The target takes half damage and is [[Fascinated]] with you for 1 round.
- **Failure** The target takes full damage and is fascinated with you for 1 round. While fascinated with you, the target must succeed at a DC 5 flat check when attempting to Cast a Spell or use an action with the auditory trait. On a failure, the action is disrupted as the target blurts praise for you instead of saying what it intended.
- **Critical Failure** As failure, but double damage and the effect lasts for 1 minute.

**Heightened (+1)** The damage increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
