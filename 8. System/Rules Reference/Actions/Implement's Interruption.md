---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Thaumaturge]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** The target of your Exploit Vulnerability uses a concentrate, manipulate, or move action, or leaves a square during a move action it's using.

**Requirements** You're holding your weapon implement and are benefiting from Exploit Vulnerability against a creature. The creature must be within your reach if you're wielding a melee weapon, or within 10 feet if you're wielding a ranged weapon.

Your weapon senses a moment of weakness and guides your hand to strike down a foe. Make a Strike against the triggering creature with your weapon implement. If your attack is a critical hit, you disrupt the triggering action. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike.

**Source:** `= this.source` (`= this.source-type`)
