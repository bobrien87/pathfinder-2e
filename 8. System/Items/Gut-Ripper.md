---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Mythic]]", "[[Trip]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking ogre hook* causes its owner to dream of past murders conducted with the weapon. *Gut-Ripper*'s mythic magic is tied to the bloodlust of the ogre boss who was holding it upon becoming mythic. If *Gut-Ripper* doesn't kill a creature each day by midnight, it becomes a non-magical ogre hook.

**Activate—Rip Guts! Rip Guts!** `pf2:2` **Cost** 1 Mythic Point

**Effect** You throw *Gut-Ripper* in a line of any length up to 60 feet, then it returns to your hands. Each creature in the line takes @Damage[2d10[piercing]|options:area-damage] damage with a DC 25 [[Fortitude]] save. If there's a creature at the end of the line, you instead make a melee Strike against it with the hook that deals an additional 2d10 persistent,bleed damage. Each time a creature takes this bleed damage, you regain that many HP; this is a healing vitality effect. This activation can't be used again for 1d4 rounds.

**Source:** `= this.source` (`= this.source-type`)
