---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You make the spell's target believe they had something incredibly important to say but forgot to say it, and now they've missed their opportunity. Sensations of overwhelming panic akin to stage fright flood the target's mind, causing them to suffer excruciating mental anguish and take 12d6 mental damage. The target might even become filled with the conviction that they've doomed themselves by missing their cue. The target must attempt a Will save.
- **Critical Success** The conviction of a missed cue is only a fleeting notion that passes quickly without any effect on the target.
- **Success** The target takes half damage and is [[Frightened]] 1.
- **Failure** The target takes full damage and becomes [[Frightened]] 2. In addition, the target is [[Slowed]] 1 for as long as they remain frightened.
- **Critical Failure** The target takes double damage and becomes [[Frightened]] 3. In addition, the target is slowed 1 for as long as they remain frightened.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
