---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Focus]]", "[[Illusion]]", "[[Mental]]", "[[Visual]]"]
cast: "`pf2:1`"
defense: "basic Will"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You are surrounded by up to 3 mirrors that reflect twisted and distorted images of you, making it hard to tell where you actually are within your space and potentially causing those who attack you to hit one of the mirrors instead. You start with 1 mirror and gain an additional mirror each time you Sustain this spell, up to a maximum of 3 mirrors. Any attack that would hit you has a random chance of hitting one of your mirrors instead of you. With one mirror, the chances are 1 in 2 (1–3 on 1d6). With two mirrors, there is a 1 in 3 chance of hitting you (1–2 on 1d6). With three mirrors, there is a 1 in 4 chance of hitting you (1 on 1d4).

Once an image is hit, it is destroyed. If an attack roll fails to hit your AC but doesn't critically fail, it destroys a mirror. If the attacker was within 5 feet, they must succeed at a basic Will save or take 1d4 mental damage as they believe themselves cut by a shower of glass shards from the breaking mirror. A damaging effect that affects all targets within your space (such as [[Caustic Blast]]) destroys all of the mirrors.

**Heightened (+1)** The mental damage dealt by a broken mirror increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
