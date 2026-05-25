---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Emotion]]", "[[Manipulate]]", "[[Mental]]", "[[Psychic]]"]
cast: "`pf2:2`"
range: "30 feet (see text)"
targets: "1 or 2 creatures other than yourself (see text)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Nothing is so contagious as a thought. You place either a pleasant thought or a terrifying one in a creature's mind. You can then plant the same thought in a second creature's mind. You can't choose a creature that's already been a target of this casting of contagious idea, nor can you choose yourself. The second target can be beyond the range of the spell, but it must be within 30 feet of the first target.

- **Pleasant Thought** The target is soothed by a pleasant memory, gaining 5 temporary Hit Points that last for 1 minute. 

> [!danger] Effect: Spell Effect: Contagious Idea (Pleasant Thought)

- **Terrifying Thought** You plant a nameless unease in the target's mind. The target must attempt a Will save.
- **Critical Success** The target is unaffected and is temporarily immune for 1 minute.
- **Success** The target is [[Frightened]] 1 and is then temporarily immune for 1 minute.
- **Failure** The target becomes [[Frightened]] 2.
- **Critical Failure** The target becomes [[Frightened]] 3.

**Heightened (+1)** The temporary Hit Points for a pleasant thought increase by 1.

**Source:** `= this.source` (`= this.source-type`)
